# auth_db.py
"""
Database helpers for the Authentication CLI.
Uses SQLite and PBKDF2-HMAC-SHA256 for password hashing (no external deps).
"""

import sqlite3
import os
import hashlib
import binascii
from typing import Optional, Dict

DB_PATH = os.getenv("AUTH_DB_PATH", "auth.db")
PBKDF2_ITER = 100_000  # number of iterations for PBKDF2


def get_conn():
    return sqlite3.connect(DB_PATH)


def create_users_table():
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                iterations INTEGER NOT NULL
            )
            """
        )
        conn.commit()


def _hash_password(password: str, salt: bytes | None = None, iterations: int = PBKDF2_ITER):
    """Return tuple (hash_hex, salt_hex, iterations). If salt is None, generate a new 16-byte salt."""
    if salt is None:
        salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return binascii.hexlify(dk).decode(), binascii.hexlify(salt).decode(), iterations


def add_user(username: str, password: str) -> bool:
    """Add a new user. Returns True on success, False if username already exists or error."""
    try:
        password_hash, salt_hex, iterations = _hash_password(password)
        with get_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (username, password_hash, salt, iterations) VALUES (?, ?, ?, ?)",
                (username, password_hash, salt_hex, iterations),
            )
            conn.commit()
        return True
    except sqlite3.IntegrityError:
        # username already exists
        return False
    except Exception as e:
        print(f"Error adding user: {e}")
        return False


def get_user(username: str) -> Optional[Dict]:
    """Return user row as dict or None if not found."""
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, username, password_hash, salt, iterations FROM users WHERE username = ? LIMIT 1", (username,))
        row = cur.fetchone()
        if not row:
            return None
        return {
            "id": row[0],
            "username": row[1],
            "password_hash": row[2],
            "salt": row[3],
            "iterations": row[4],
        }


def verify_password(stored_hash_hex: str, salt_hex: str, iterations: int, password_attempt: str) -> bool:
    """Return True if password_attempt matches stored hash."""
    try:
        salt = binascii.unhexlify(salt_hex.encode())
        computed_hash_hex, _, _ = _hash_password(password_attempt, salt=salt, iterations=iterations)
        # constant-time compare:
        return hashlib.compare_digest(computed_hash_hex, stored_hash_hex)
    except Exception as e:
        print(f"Error verifying password: {e}")
        return False


def ensure_initial_users():
    """If users table is empty, create 3 initial users (sample)."""
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM users")
        count = cur.fetchone()[0]
        if count == 0:
            # Add three initial users
            initial = [("alice", "alice123"), ("bob", "bob123"), ("carol", "carol123")]
            for u, p in initial:
                add_user(u, p)
# auth_cli.py
"""
Command-line Authentication program using auth_db.py
Commands:
 - login  : login with username & password
 - signup : create a new account
 - exit   : quit program
"""

from auth_db import create_users_table, ensure_initial_users, get_user, add_user, verify_password
import getpass

def login_procedure():
    username = input("Username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return None
    user = get_user(username)
    if not user:
        print("User not found.")
        return None
    # use getpass so password is not echoed
    pwd = getpass.getpass("Password: ")
    if verify_password(user["password_hash"], user["salt"], user["iterations"], pwd):
        print("You are now logged in.")
        return user["username"]
    else:
        print("Incorrect password.")
        return None

def signup_procedure():
    while True:
        username = input("Choose a username: ").strip()
        if not username:
            print("Username cannot be empty.")
            continue
        if get_user(username):
            print("That username already exists. Try a different one.")
            continue
        break
    while True:
        pwd = getpass.getpass("Choose a password: ")
        if not pwd:
            print("Password cannot be empty.")
            continue
        pwd_confirm = getpass.getpass("Confirm password: ")
        if pwd != pwd_confirm:
            print("Passwords do not match. Try again.")
            continue
        break
    ok = add_user(username, pwd)
    if ok:
        print("Signup successful. You can now login.")
    else:
        print("There was an error creating the account.")

def show_menu():
    print("\nAvailable commands:")
    print(" - login  : Log in")
    print(" - signup : Create an account")
    print(" - exit   : Quit program\n")

def main():
    create_users_table()
    ensure_initial_users()  # creates 3 sample users if table empty

    logged_in = None
    print("Welcome to the Authentication CLI (type 'exit' to quit).")
    while True:
        show_menu()
        cmd = input("Enter command (login/signup/exit): ").strip().lower()
        if cmd == "exit":
            if logged_in:
                print(f"Goodbye — user '{logged_in}' was logged in.")
            else:
                print("Goodbye.")
            break
        elif cmd == "login":
            if logged_in:
                print(f"Already logged in as '{logged_in}'. If you want to change user, type 'logout' or restart the program.")
                continue
            result = login_procedure()
            if result:
                logged_in = result
        elif cmd == "signup":
            signup_procedure()
        elif cmd == "logout":
            if logged_in:
                print(f"User '{logged_in}' logged out.")
                logged_in = None
            else:
                print("No user currently logged in.")
        else:
            print("Unknown command. Please choose login, signup, logout or exit.")

if __name__ == "__main__":
    main()

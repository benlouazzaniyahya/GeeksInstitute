"""
countries_to_db.py

Fetch 10 random countries from REST Countries API and store them in a local SQLite DB.

No external packages required (uses urllib and sqlite3 from the stdlib).
"""

import json
import random
import sqlite3
import urllib.request
from typing import List, Dict

# API endpoint with field filtering (keeps payload small)
API_URL = "https://restcountries.com/v3.1/all?fields=name,capital,flags,subregion,population"

DB_PATH = "countries.db"
TABLE_NAME = "countries"


def fetch_all_countries() -> List[Dict]:
    """Fetch country list (only the requested fields) from REST Countries API."""
    with urllib.request.urlopen(API_URL, timeout=20) as resp:
        data = resp.read()
        return json.loads(data)


def normalize_country(raw: Dict) -> Dict:
    """Return a normalized dict with keys: name, capital, flag, subregion, population."""
    # name.common exists in v3.1 response
    name = raw.get("name", {}).get("common", None)

    # capital may be a list (take first) or missing
    capital_list = raw.get("capital")
    capital = capital_list[0] if isinstance(capital_list, list) and capital_list else None

    # flags may contain 'png' or 'svg'
    flags = raw.get("flags", {})
    flag = flags.get("png") or flags.get("svg") or None

    subregion = raw.get("subregion")
    population = raw.get("population") if isinstance(raw.get("population"), int) else 0

    return {
        "name": name,
        "capital": capital,
        "flag": flag,
        "subregion": subregion,
        "population": population,
    }


def create_table(conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            capital TEXT,
            flag TEXT,
            subregion TEXT,
            population INTEGER
        )
    """)
    conn.commit()


def insert_countries(conn: sqlite3.Connection, countries: List[Dict]):
    cur = conn.cursor()
    for c in countries:
        try:
            cur.execute(f"""
                INSERT OR IGNORE INTO {TABLE_NAME} (name, capital, flag, subregion, population)
                VALUES (?, ?, ?, ?, ?)
            """, (c["name"], c["capital"], c["flag"], c["subregion"], c["population"]))
        except Exception as e:
            print(f"Error inserting {c['name']!r}: {e}")
    conn.commit()


def main(n: int = 10):
    print("Fetching countries from REST Countries API...")
    all_raw = fetch_all_countries()
    print(f"Total countries fetched: {len(all_raw)}")

    # normalize and filter out any entries missing a name
    normalized = [normalize_country(r) for r in all_raw]
    normalized = [n for n in normalized if n["name"]]

    # pick n random countries (if there are fewer than n, pick all)
    chosen = random.sample(normalized, k=min(n, len(normalized)))

    print("Chosen countries:")
    for c in chosen:
        print(f" - {c['name']} (capital: {c['capital']}, population: {c['population']})")

    # write to SQLite
    conn = sqlite3.connect(DB_PATH)
    create_table(conn)
    insert_countries(conn, chosen)
    conn.close()
    print(f"Inserted {len(chosen)} countries into {DB_PATH} -> table '{TABLE_NAME}'.")


if __name__ == "__main__":
    main(10)

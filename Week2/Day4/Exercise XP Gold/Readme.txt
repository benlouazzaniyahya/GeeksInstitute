How it works / notes

The DB file auth.db (default) is created in the current folder. You can change path with environment variable AUTH_DB_PATH.

auth_db.create_users_table() ensures the users table exists.

auth_db.ensure_initial_users() creates three initial users (Alice/Bob/Carol with passwords alice123, bob123, carol123) only if the table is empty — useful for testing.

Passwords are hashed with PBKDF2-HMAC-SHA256 and a random 16-byte salt; the salt and iterations are stored with the user row.

The CLI uses getpass.getpass() so password input is hidden.

logged_in variable stores current username on successful login (as requested).

To run

Save both files in the same folder.

python auth_cli.py

Try login with one of the sample users: alice / alice123

Try signup to create a new user, then login.
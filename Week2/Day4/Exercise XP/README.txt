Install dependencies:

pip install psycopg2-binary

Run the SQL in db_setup.sql (in psql or pgAdmin) to create database and table.

Configure DB connection:

Option A (recommended): set DATABASE_URL environment variable (e.g. postgresql://user:pass@localhost:5432/restaurant_db).

Option B: edit the DEFAULT_CONN dict in menu_item.py to match your local PostgreSQL credentials.

Run the CLI:python menu_editor.py
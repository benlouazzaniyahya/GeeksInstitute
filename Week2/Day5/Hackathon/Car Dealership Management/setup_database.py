
import os
import psycopg2
from dotenv import load_dotenv

def setup_database():
    """Create the PostgreSQL database and tables if they don't exist"""
    load_dotenv()

    # Get database connection details from environment variables
    db_url = os.getenv('DATABASE_URL', 'postgresql://postgres:Oceanbyte@localhost/car_dealership')

    # Parse the database URL
    dbname = 'car_dealership'
    if '//' in db_url:
        # Extract database name from URL
        db_url_parts = db_url.split('//')[1].split('/')
        if len(db_url_parts) > 1:
            dbname = db_url_parts[1].split('?')[0]

    # Connect to default PostgreSQL database to create our database
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Oceanbyte',  # Replace with your PostgreSQL password
        database='car_dealership'  # Connect to default postgres database
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # Create the database if it doesn't exist
    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{dbname}'")
    if not cursor.fetchone():
        cursor.execute(f'CREATE DATABASE {dbname}')
        print(f"Database '{dbname}' created successfully!")
    else:
        print(f"Database '{dbname}' already exists.")

    # Close the connection to default database
    cursor.close()
    conn.close()

    # Connect to our newly created database and run the SQL schema
    try:
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()

        # Read the SQL schema from the seed file
        seed_file_path = os.path.join(os.path.dirname(__file__), 'database', 'seed', 'index.sql')
        with open(seed_file_path, 'r') as f:
            sql = f.read()

        # Execute the SQL commands
        cursor.execute(sql)
        print("Database tables created successfully!")

        # Close the connection
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error setting up database: {e}")

if __name__ == '__main__':
    setup_database()

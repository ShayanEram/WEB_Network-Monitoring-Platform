import os
import sqlite3

import config


def get_db_connection():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    db_path = os.path.join(base_dir, config.DATABASE_PATH)

    # Ensure the database directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    db_path = config.DATABASE_PATH
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)

    # Path to schema.sql relative to project root
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")

    with open(schema_path, "r") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()
    print("Database initialized successfully!")


def show_db():

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    db_path = os.path.join(base_dir, config.DATABASE_PATH)

    # 1. Connect to database file
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 2. Get a list of all tables in the file
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in database:", tables)

    # 3. Read data from a specific table (replace 'table_name')
    # Change 'table_name' to one of the tables printed above!
    try:
        cursor.execute("SELECT * FROM devices LIMIT 10;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.OperationalError:
        print(
            "\nTo see data, replace 'table_name' with a real table from the list above."
        )

    try:
        cursor.execute("SELECT * FROM traffic_logs LIMIT 10;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.OperationalError:
        print(
            "\nTo see data, replace 'table_name' with a real table from the list above."
        )

    try:
        cursor.execute("SELECT * FROM alerts LIMIT 10;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.OperationalError:
        print(
            "\nTo see data, replace 'table_name' with a real table from the list above."
        )

    # 4. Close the connection
    conn.close()

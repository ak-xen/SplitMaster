import sqlite3

conn = sqlite3.connect('data/DB.db')
with conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS orders
    (id INTEGER PRIMARY KEY,
    task TEXT,
    description TEXT,
    lead_time TEXT,
    address TEXT,
    price INTEGER,
    telephone_number INTEGER,
    master INTEGER,
    time_created TEXT,
    time_completed TEXT,
    status INTEGER)
"""),

    conn.execute("""
        CREATE TABLE IF NOT EXISTS master
        (id INTEGER PRIMARY KEY,
        name TEXT,
        family TEXT,
        telephone_number INTEGER)
        """)


conn.close()
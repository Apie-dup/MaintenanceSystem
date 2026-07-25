from app.database.connection import Database

conn = Database.connect()
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    fullname TEXT,
    role TEXT,
    active INTEGER DEFAULT 1,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT
)
""")

conn.commit()
conn.close()

print("Users table recreated successfully.")

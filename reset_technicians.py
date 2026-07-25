from app.database.connection import Database

conn = Database.connect()
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS technicians")

cursor.execute("""
CREATE TABLE technicians (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_number TEXT UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    trade TEXT,
    department TEXT,
    hourly_rate REAL,
    status TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Technicians table recreated successfully.")


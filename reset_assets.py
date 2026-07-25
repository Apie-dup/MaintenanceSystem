from app.database.connection import Database

conn = Database.connect()
cursor = conn.cursor()

# Drop the old table
cursor.execute("DROP TABLE IF EXISTS assets")

# Create the correct assets table
cursor.execute("""
CREATE TABLE assets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    asset_number TEXT NOT NULL,
    asset_name TEXT NOT NULL,
    description TEXT,
    category TEXT,
    location TEXT,
    manufacturer TEXT,
    model TEXT,
    serial_number TEXT,
    purchase_date TEXT,
    warranty_expiry TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Assets table recreated successfully.")

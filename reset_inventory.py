from app.database.connection import Database

conn = Database.connect()
cursor = conn.cursor()

# Drop teh old table

cursor.execute("DROP TABLE IF EXISTS inventory")

# Create the correct inventory table

cursor.execute("""
    CREATE TABLE inventory(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    part_number TEXT NOT NULL,
    part_name TEXT NOT NULL,
    description TEXT,
    category TEXT,
    supplier_id INTEGER,
    unit TEXT,
    quantity INTEGER,
    minimum_quantity INTEGER,
    reorder_quantity INTEGER,
    unit_cost REAL,
    location TEXT,
    barcode TEXT,
    status TEXT,
    notes TEXT
)
""")

conn.commit()
conn.close()

print("Inventory table recreated successfully.")



from app.database.connection import Database


def create_tables():

    conn = Database.connect()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT,
        fullname TEXT,
        role TEXT,
        active INTEGER DEFAULT 1,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
""")

    Database._ensure_columns(
        conn,
        "users",
        {
            "password_hash": "TEXT",
            "fullname": "TEXT",
            "role": "TEXT",
            "active": "INTEGER DEFAULT 1",
        },
    )

    # Assets table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asset_number TEXT UNIQUE NOT NULL,
        asset_name TEXT NOT NULL,
        description TEXT,
        category TEXT,
        location TEXT,
        manufacturer TEXT,
        model TEXT,
        serial_number TEXT,
        purchase_date TEXT,
        warranty_expiry TEXT,
        status TEXT DEFAULT 'Active'
    )
""")
    
# Work Orders table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS work_orders (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    work_order_number TEXT UNIQUE NOT NULL,

    asset_id INTEGER NOT NULL,

    title TEXT NOT NULL,

    description TEXT,

    priority TEXT,

    status TEXT,

    technician_id INTEGER,

    requested_by TEXT,

    date_created TEXT,

    due_date TEXT,

    completion_date TEXT,

    labour_hours REAL DEFAULT 0,

    estimated_cost REAL DEFAULT 0,

    actual_cost REAL DEFAULT 0,

    notes TEXT,

    FOREIGN KEY(asset_id)
        REFERENCES assets(id)

)
""")
    
# Technicians Table
    cursor.execute("""
    CREATE TABLE IF NOT EXIST technicians (
                   
        id INTEGER PRIMARY KEY AUTOINCREMENT,
                
        employee_number TEXT UNIQUE NOT NULL,
                   
        first_name TEXT NOT NULL,
                   
        last_name TEXT NOT NULL,
                   
        phone TEXT,
                   
        email TEXT,
                   
        trade TEXT,
                   
        department TEXT,
                   
        status TEXT DEFAULT 'Active',
                   
        hourly_rate REAL DEFAULT 0,
                   
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    
    )
    """)

    Database._ensure_columns(
        conn,
        "assets",
        {
            "description": "TEXT",
            "purchase_date": "TEXT",
            "warranty_expiry": "TEXT",
            "status": "TEXT DEFAULT 'Active'",
        },
    )

    # Application settings table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS app_settings (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL
    )
""")
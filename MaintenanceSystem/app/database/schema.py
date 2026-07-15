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

    wo_number TEXT UNIQUE NOT NULL,
                   
    asset_id INTEGER,

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
    CREATE TABLE IF NOT EXISTS technicians (
                   
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

    # Trades
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        trade_name TEXT UNIQUE NOT NULL
)
""")

# Departments
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        department_name TEXT UNIQUE NOT NULL
)
""")

# Work Order Priorities
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS priorities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        priority_name TEXT UNIQUE NOT NULL
)
""")

# Statuses
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS statuses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        status_name TEXT UNIQUE NOT NULL
)
""")

    # Application settings table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS app_settings (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL
    )
""")
    
    # Asset Categories
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS asset_categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT UNIQUE NOT NULL
    )
""")

    # Asset Locations
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS asset_locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location_name TEXT UNIQUE NOT NULL
    )
""")

    # Manufacturers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS manufacturers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        manufacturer_name TEXT UNIQUE NOT NULL
    )
""")

    # Inventory Categories
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory_categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT UNIQUE NOT NULL
    )
""")

    # Units of Measure
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS units_of_measure (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        unit_name TEXT UNIQUE NOT NULL
)
""")
    
    # Preventive Maintenance Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS preventive_maintenance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pm_number TEXT UNIQUE NOT NULL,
        asset_id INTEGER NOT NULL,
        task TEXT NOT NULL,
        description TEXT,
        frequency_type TEXT NOT NULL,
        frequency_value INTEGER DEFAULT 1,
        last_service_date TEXT,
        next_due_date TEXT NOT NULL,
        estimated_hours REAL DEFAULT 0,
        estimated_cost REAL DEFAULT 0,
        priority TEXT DEFAULT 'Medium',
        active INTEGER DEFAULT 1,
        notes TEXT,
        FOREIGN KEY(asset_id) REFERENCES assets(id)
    )
""")
    
    conn.commit()
    conn.close()
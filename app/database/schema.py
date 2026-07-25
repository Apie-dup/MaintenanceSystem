from app.database.connection import Database


class DatabaseSchema:

    @staticmethod
    def create_tables():

        conn = Database.connect()
        cursor = conn.cursor()

        # Enable foreign keys
        cursor.execute("PRAGMA foreign_keys = ON;")

        # =====================================================
        # USERS
        # =====================================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            fullname TEXT NOT NULL,
            role TEXT NOT NULL,
            active INTEGER NOT NULL DEFAULT 1,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # =====================================================
        # LOOKUPS
        # =====================================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS lookups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lookup_type TEXT NOT NULL,
            value TEXT NOT NULL,
            sort_order INTEGER DEFAULT 0,
            active INTEGER DEFAULT 1,
            UNIQUE(lookup_type, value)
        )
        """)

        # =====================================================
        # ASSETS
        # =====================================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_number TEXT NOT NULL UNIQUE,
            asset_name TEXT NOT NULL,
            description TEXT,
            category TEXT,
            location TEXT,
            manufacturer TEXT,
            model TEXT,
            serial_number TEXT,
            purchase_date TEXT,
            warranty_expiry TEXT,
            status TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # =====================================================
        # TECHNICIANS
        # =====================================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS technicians (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_number TEXT NOT NULL UNIQUE,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT,
            email TEXT,
            trade TEXT,
            department TEXT,
            hourly_rate REAL DEFAULT 0,
            status TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # =====================================================
        # SUPPLIERS
        # =====================================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            supplier_code TEXT NOT NULL UNIQUE,
            supplier_name TEXT NOT NULL,
            contact_person TEXT,
            phone TEXT,
            email TEXT,
            address TEXT,
            status TEXT,
            notes TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # =====================================================
        # INVENTORY
        # =====================================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            part_number TEXT NOT NULL UNIQUE,
            part_name TEXT NOT NULL,
            description TEXT,
            category TEXT,
            supplier_id INTEGER,
            unit TEXT,
            quantity INTEGER DEFAULT 0,
            minimum_quantity INTEGER DEFAULT 0,
            reorder_quantity INTEGER DEFAULT 0,
            unit_cost REAL DEFAULT 0,
            location TEXT,
            barcode TEXT,
            status TEXT,
            notes TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (supplier_id)
                REFERENCES suppliers(id)
                ON DELETE SET NULL
        )
        """)

        # =====================================================
        # WORK ORDERS
        # =====================================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS work_orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            work_order_number TEXT NOT NULL UNIQUE,
            asset_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT,
            status TEXT,
            technician_id INTEGER,
            requested_by TEXT,
            date_created TEXT,
            due_date TEXT,
            estimated_cost REAL DEFAULT 0,
            actual_cost REAL DEFAULT 0,
            labour_hours REAL DEFAULT 0,
            notes TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(asset_id)
                REFERENCES assets(id)
                ON DELETE CASCADE,
            FOREIGN KEY(technician_id)
                REFERENCES technicians(id)
                ON DELETE SET NULL
        )
        """)

        # =====================================================
        # PREVENTIVE MAINTENANCE
        # =====================================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS preventive_maintenance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pm_number TEXT NOT NULL UNIQUE,
            asset_id INTEGER NOT NULL,
            task TEXT NOT NULL,
            description TEXT,
            frequency_type TEXT,
            frequency_value INTEGER,
            last_service_date TEXT,
            next_due_date TEXT,
            estimated_hours REAL DEFAULT 0,
            estimated_cost REAL DEFAULT 0,
            priority TEXT,
            active INTEGER DEFAULT 1,
            notes TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(asset_id)
                REFERENCES assets(id)
                ON DELETE CASCADE
        )
        """)

        conn.commit()
        conn.close()
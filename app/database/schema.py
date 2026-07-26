from app.database.connection import Database


class DatabaseSchema:

    @staticmethod
    def create_tables():

        conn = Database.connect()
        cursor = conn.cursor()

        # Enable foreign keys
        cursor.execute("PRAGMA foreign_keys = ON;")

        # =====================================================
        # DATABASE VERSION
        # =====================================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS schema_version
        (
            version INTEGER NOT NULL
        )
        """)

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
            category TEXT NOT NULL,
            location TEXT NOT NULL,
            manufacturer TEXT,
            model TEXT,
            serial_number TEXT,
            purchase_date TEXT,
            warranty_expiry TEXT,
            status TEXT NOT NULL,
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
            trade TEXT NOT NULL,
            department TEXT NOT NULL,
            hourly_rate REAL DEFAULT 0,
            status TEXT NOT NULL,
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
            category TEXT NOT NULL,
            supplier_id INTEGER,
            unit TEXT NOT NULL,
            quantity INTEGER DEFAULT 0,
            minimum_quantity INTEGER DEFAULT 0,
            reorder_quantity INTEGER DEFAULT 0,
            unit_cost REAL DEFAULT 0,
            location TEXT,
            barcode TEXT,
            status TEXT NOT NULL,
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
            priority TEXT NOT NULL,
            status TEXT NOT NULL,
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
        # WORK ORDER PARTS
        # =====================================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS work_order_parts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        work_order_id INTEGER NOT NULL,

        inventory_id INTEGER NOT NULL,

        quantity REAL NOT NULL DEFAULT 1,

        unit_cost REAL NOT NULL DEFAULT 0,

        total_cost REAL NOT NULL DEFAULT 0,

        notes TEXT,

        created_at TEXT DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(work_order_id)
            REFERENCES work_orders(id)
            ON DELETE CASCADE,

        FOREIGN KEY(inventory_id)
            REFERENCES inventory(id)
            ON DELETE RESTRICT
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
            frequency_type TEXT NOT NULL,
            frequency_value INTEGER,
            last_service_date TEXT,
            next_due_date TEXT,
            estimated_hours REAL DEFAULT 0,
            estimated_cost REAL DEFAULT 0,
            priority TEXT NOT NULL,
            active INTEGER DEFAULT 1 CHECK (active IN (0,1)),
            notes TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(asset_id)
                REFERENCES assets(id)
                ON DELETE CASCADE
        )
        """)

        # =====================================================
        # MAINTENANCE HISTORY
        # =====================================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS maintenance_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        history_number TEXT NOT NULL UNIQUE,

        asset_id INTEGER NOT NULL,

        work_order_id INTEGER,

        pm_id INTEGER,

        technician_id INTEGER,

        maintenance_type TEXT NOT NULL,

        title TEXT NOT NULL,

        description TEXT,

        work_performed TEXT,

        completion_date TEXT NOT NULL,

        labour_hours REAL DEFAULT 0,

        labour_cost REAL DEFAULT 0,

        parts_cost REAL DEFAULT 0,

        total_cost REAL DEFAULT 0,

        completed_by TEXT,

        remarks TEXT,

        created_at TEXT DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(asset_id)
            REFERENCES assets(id)
            ON DELETE CASCADE,

        FOREIGN KEY(work_order_id)
            REFERENCES work_orders(id)
            ON DELETE SET NULL,

        FOREIGN KEY(pm_id)
            REFERENCES preventive_maintenance(id)
            ON DELETE SET NULL,

        FOREIGN KEY(technician_id)
            REFERENCES technicians(id)
            ON DELETE SET NULL
        )
        """)

        # Assets
        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_asset_number
        ON assets(asset_number)
        """)

        # Technicians
        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_employee_number
        ON technicians(employee_number)
        """)

        # Inventory
        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_part_number
        ON inventory(part_number)
        """)

        # Suppliers
        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_supplier_code
        ON suppliers(supplier_code)
        """)

        # Work Orders
        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_work_order_number
        ON work_orders(work_order_number)
        """)

        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_work_order_asset
        ON work_orders(asset_id)
        """)

        # Preventive Maintenance
        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_pm_number
        ON preventive_maintenance(pm_number)
        """)

        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_pm_asset
        ON preventive_maintenance(asset_id)
        """)

        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_history_asset
        ON maintenance_history(asset_id)
        """)

        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_history_work_order
        ON maintenance_history(work_order_id)
        """)

        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_history_pm
        ON maintenance_history(pm_id)
        """)

        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_history_completion
        ON maintenance_history(completion_date)
        """)

        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_work_order_parts_work_order
        ON work_order_parts(work_order_id)
        """)

        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_work_order_parts_inventory
        ON work_order_parts(inventory_id)
        """)

        cursor.execute("""
        SELECT COUNT (*)
        FROM schema_version
        """)

        if cursor.fetchone()[0] == 0:
            cursor.execute("""
            INSERT INTO schema_version
            VALUES (1)
            """)

        conn.commit()
        conn.close()
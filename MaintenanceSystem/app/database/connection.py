import sqlite3
from pathlib import Path
import bcrypt

DATABASE = Path("database") / "maintenance.db"

# Ensure the database folder exists
DATABASE.parent.mkdir(exist_ok=True)


class Database:
    DATABASE = DATABASE

    @staticmethod
    def connect():
        return sqlite3.connect(Database.DATABASE)

    @staticmethod
    def _ensure_columns(conn, table_name, columns):
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        existing_columns = {row[1] for row in cursor.fetchall()}

        for column_name, definition in columns.items():
            if column_name not in existing_columns:
                cursor.execute(
                    f"ALTER TABLE {table_name} ADD COLUMN {column_name} {definition}"
                )

    @staticmethod
    def initialize():
        conn = Database.connect()
        cursor = conn.cursor()

        # -----------------------------
        # USERS TABLE
        # -----------------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                fullname TEXT NOT NULL,
                role TEXT NOT NULL,
                active INTEGER DEFAULT 1
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

        # -----------------------------
        # ASSETS TABLE
        # -----------------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS assets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                asset_number TEXT UNIQUE NOT NULL,
                asset_name TEXT NOT NULL,
                category TEXT,
                location TEXT,
                manufacturer TEXT,
                model TEXT,
                serial_number TEXT,
                purchase_date TEXT,
                warranty_expiry TEXT,
                status TEXT DEFAULT 'Active',
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
                "created_at": "TEXT DEFAULT CURRENT_TIMESTAMP",
            },
        )

        # -----------------------------
        # WORK ORDERS
        # -----------------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS work_orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                wo_number TEXT UNIQUE,
                asset_id INTEGER,
                title TEXT,
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
                notes TEXT
            )
        """)

        Database._ensure_columns(
            conn,
            "work_orders",
            {
                "title": "TEXT",
                "technician_id": "INTEGER",
                "requested_by": "TEXT",
                "date_created": "TEXT",
                "due_date": "TEXT",
                "completion_date": "TEXT",
                "labour_hours": "REAL DEFAULT 0",
                "estimated_cost": "REAL DEFAULT 0",
                "actual_cost": "REAL DEFAULT 0",
                "notes": "TEXT",
            },
        )

        # -----------------------------
        # PREVENTIVE MAINTENANCE
        # -----------------------------
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

        # -----------------------------
        # INVENTORY
        # -----------------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                part_number TEXT,
                description TEXT,
                quantity INTEGER DEFAULT 0,
                minimum_quantity INTEGER DEFAULT 0,
                location TEXT
            )
        """)

        # -----------------------------
        # SETTINGS
        # -----------------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT,
                company_logo TEXT,
                theme TEXT
            )
        """)

        # -----------------------------
        # CREATE DEFAULT ADMIN
        # -----------------------------
        cursor.execute(
            "SELECT id FROM users WHERE username=?",
            ("admin",)
        )

        if cursor.fetchone() is None:

            password_hash = bcrypt.hashpw(
                "admin123".encode(),
                bcrypt.gensalt()
            ).decode()

            cursor.execute("""
                INSERT INTO users
                (username, password_hash, fullname, role, active)
                VALUES (?, ?, ?, ?, ?)
            """, (
                "admin",
                password_hash,
                "Administrator",
                "Administrator",
                1
            ))

            print("Default administrator created")

        conn.commit()
        conn.close()

    @staticmethod
    def is_connected():
        try:
            conn = Database.connect()
            conn.close()
            return True
        except Exception:
            return False
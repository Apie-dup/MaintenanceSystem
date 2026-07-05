import sqlite3
from pathlib import Path
import bcrypt

DATABASE = Path("database") / "maintenance.db"

# Ensure the database folder exists
DATABASE.parent.mkdir(exist_ok=True)


class Database:

    @staticmethod
    def connect():
        return sqlite3.connect(DATABASE)

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

        # -----------------------------
        # WORK ORDERS
        # -----------------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS work_orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                wo_number TEXT UNIQUE,
                asset_id INTEGER,
                description TEXT,
                priority TEXT,
                status TEXT,
                assigned_to TEXT,
                date_created TEXT,
                date_completed TEXT
            )
        """)

        # -----------------------------
        # PREVENTIVE MAINTENANCE
        # -----------------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS preventive_maintenance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                asset_id INTEGER,
                task TEXT,
                frequency TEXT,
                next_due TEXT,
                last_completed TEXT,
                status TEXT
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
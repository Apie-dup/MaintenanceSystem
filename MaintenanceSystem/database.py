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

        # Create users table
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

        # Check if an admin user already exists
        cursor.execute(
            "SELECT id FROM users WHERE username = ?",
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

            print("Default administrator created.")
            print("Username: admin")
            print("Password: admin123")

        conn.commit()
        conn.close()
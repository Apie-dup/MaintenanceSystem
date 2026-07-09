import bcrypt

from app.database.connection import Database


def seed_default_admin():

    conn = Database.connect()
    cursor = conn.cursor()

    password_hash = bcrypt.hashpw(
        "admin123".encode(),
        bcrypt.gensalt()
    ).decode()

    cursor.execute("""
        INSERT INTO users
        (
            username,
            password_hash,
            fullname,
            role,
            active
        )
        VALUES
        (
            ?,
            ?,
            ?,
            ?,
            ?
        )
        ON CONFLICT(username) DO UPDATE SET
            password_hash = excluded.password_hash,
            fullname = excluded.fullname,
            role = excluded.role,
            active = excluded.active
    """, (
        "admin",
        password_hash,
        "Administrator",
        "Administrator",
        1,
    ))

    conn.commit()
    conn.close()

def seed_app_settings():

    conn = Database.connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO app_settings
        (
            key,
            value
        )
        VALUES
        (
            'database_version',
            '1'
        )
    """)

    conn.commit()
    conn.close()
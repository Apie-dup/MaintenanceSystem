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

def seed_preventive_maintenance():
    pass

def seed_lookup_tables():
    conn = Database.connect()
    cursor = conn.cursor()

    trades = [
        "Electrician",
        "Mechanic",
        "Plumber",
        "Welder",
        "Carpenter",
        "Painter",
        "General Maintenance",
        "HVAC Technician"
    ]

    for trade in trades:
        cursor.execute("""
            INSERT OR IGNORE INTO trades (trade_name)
            VALUES (?)
        """, (trade,))

    departments = [
        "Maintenance",
        "Housekeeping",
        "Reception",
        "Kitchen",
        "Laundry",
        "Administration"
    ]

    for department in departments:
        cursor.execute("""
            INSERT OR IGNORE INTO departments (department_name)
            VALUES (?)
        """, (department,))

    priorities = [
        "Low",
        "Medium",
        "High",
        "Critical"
    ]

    for priority in priorities:
        cursor.execute("""
            INSERT OR IGNORE INTO priorities (priority_name)
            VALUES (?)
        """, (priority,))

    statuses = [
        "Active",
        "Inactive",
        "Open",
        "In Progress",
        "Completed",
        "Cancelled"
    ]

    for status in statuses:
        cursor.execute("""
            INSERT OR IGNORE INTO statuses (status_name)
            VALUES (?)
        """, (status,))
    
    categories = [
        "Electrical",
        "Mechanical",
        "HVAC",
        "Plumbing",
        "Building",
        "Vehicles",
        "IT Equipment"
    ]

    for category in categories:
        cursor.execute("""
            INSERT OR IGNORE INTO asset_categories(category_name)
            VALUES(?)
        """, (category,))
    locations = [
        "Workshop",
        "Production",
        "Warehouse",
        "Office",
        "Reception"
    ]

    for location in locations:
        cursor.execute("""
            INSERT OR IGNORE INTO asset_locations(location_name)
            VALUES(?)
        """, (location,))
    manufacturers = [
        "Siemens",
        "ABB",
        "Schneider Electric",
        "Bosch",
        "Caterpillar",
        "John Deere"
    ]

    for manufacturer in manufacturers:
        cursor.execute("""
            INSERT OR IGNORE INTO manufacturers(manufacturer_name)
            VALUES(?)
        """, (manufacturer,))
    units = [
        "Each",
        "Box",
        "Pack",
        "Metre",
        "Kilogram",
        "Litre"
    ]

    for unit in units:
        cursor.execute("""
            INSERT OR IGNORE INTO units_of_measure(unit_name)
            VALUES(?)
        """, (unit,))

    conn.commit()
    conn.close()
    
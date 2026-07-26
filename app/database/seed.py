import bcrypt
from app.database.connection import Database

class DatabaseSeeder:

    LOOKUPS = {
        "Trades": [
            "Electrician",
            "Welder",
            "Plumber",
            "Mechanic"
        ],

        "Departments": [
            "Maintenance",
            "Production",
            "Stores"
        ],

        "Asset Categories": [
            "Electrical",
            "Mechanical",
            "Building",
            "Vehicle"
        ],

        "Asset Locations": [
            "Workshop",
            "Factory",
            "Warehouse",
            "Office"
        ],

        "Statuses": [
            "Active",
            "Inactive"
        ],

        "Priorities": [
            "Low",
            "Medium",
            "High",
            "Critical"
        ],

        "Frequency Types": [
            "Dayly",
            "Weekly",
            "Monthly",
            "Quarterly",
            "Semi-Annual",
            "Annual",
            "Running Hours",
            "Cycle"

        ]

    }

    @staticmethod
    def seed():
        DatabaseSeeder.seed_admin_user()
        DatabaseSeeder.seed_lookup_values()
        DatabaseSeeder.seed_sample_assets()
        DatabaseSeeder.seed_sample_technicians()
        DatabaseSeeder.seed_sample_inventory()
        DatabaseSeeder.seed_sample_suppliers()

    # ---------------------------------------------------------
    # ADMIN USER
    # ---------------------------------------------------------
    @staticmethod
    def seed_admin_user():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM users")

        if cursor.fetchone()[0] == 0:
            password = bcrypt.hashpw("admin".encode(), bcrypt.gensalt()).decode()

            cursor.execute("""
                INSERT INTO users
                (username, password_hash, fullname, role, active)
                VALUES (?, ?, ?, ?, ?)
            """, (
                "admin",
                password,
                "System Administrator",
                "Administrator",
                1
            ))

            conn.commit()

        conn.close()

    # ---------------------------------------------------------
    # LOOKUPS
    # ---------------------------------------------------------
    @staticmethod
    def seed_lookup_values():
        conn = Database.connect()
        cursor = conn.cursor()

        for lookup_type, values in DatabaseSeeder.LOOKUPS.items():
            for value in values:
                cursor.execute("""
                    SELECT id FROM lookups
                    WHERE lookup_type = ? AND value = ?
                """, (lookup_type, value))

                if cursor.fetchone() is None:
                    cursor.execute("""
                        INSERT INTO lookups (lookup_type, value)
                        VALUES (?, ?)
                    """, (lookup_type, value))

        conn.commit()
        conn.close()

    # ---------------------------------------------------------
    # ASSETS
    # ---------------------------------------------------------
    @staticmethod
    def seed_sample_assets():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM assets")

        if cursor.fetchone()[0] == 0:

            assets = [
                (
                    "AST-000001",
                    "Main Pump",
                    "Water pump",
                    "Mechanical",
                    "Workshop",
                    "Grundfos",
                    "CR45",
                    "SN0001",
                    "2024-01-01",
                    "2026-01-01",
                    "Active"
                ),
                (
                    "AST-000002",
                    "Generator",
                    "Backup Generator",
                    "Electrical",
                    "Factory",
                    "Cummins",
                    "C200",
                    "SN1002",
                    "2023-03-01",
                    "2026-03-01",
                    "Active"
                )
            ]

            cursor.executemany("""
                INSERT INTO assets
                (
                    asset_number,
                    asset_name,
                    description,
                    category,
                    location,
                    manufacturer,
                    model,
                    serial_number,
                    purchase_date,
                    warranty_expiry,
                    status
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, assets)

        conn.commit()
        conn.close()

    # ---------------------------------------------------------
    # TECHNICIANS
    # ---------------------------------------------------------
    @staticmethod
    def seed_sample_technicians():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM technicians")

        if cursor.fetchone()[0] == 0:

            technicians = [
                (
                    "EMP-000001",
                    "John",
                    "Doe",
                    "612-55-0162",
                    "jhondoe@example.com",
                    "Welder",
                    "Workshop",
                    42.05,
                    "Active"
                ),
                (
                    "EMP-000002",
                    "Jane",
                    "Doe",
                    "441-555-0144",
                    "janedoe@example.com",
                    "Receptionist",
                    "Office",
                    32.00,
                    "Active"
                )
            ]

            cursor.executemany("""
                INSERT INTO technicians
                (
                    employee_number,
                    first_name,
                    last_name,
                    phone,
                    email,
                    trade,
                    department,
                    hourly_rate,
                    status
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, technicians)

        conn.commit()
        conn.close()

    # ---------------------------------------------------------
    # INVENTORY
    # ---------------------------------------------------------
    @staticmethod
    def seed_sample_inventory():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM inventory")

        if cursor.fetchone()[0] == 0:

            # Get supplier IDs
            cursor.execute(
                "SELECT id FROM suppliers WHERE supplier_code = ?",
                ("SUP-000001",)
            )
            supplier1 = cursor.fetchone()[0]
            
            cursor.execute(
                "SELECT id FROM suppliers WHERE supplier_code = ?",
                ("SUP-000002",)
            )
            supplier2 = cursor.fetchone()[0]

            inventory = [
                (
                    "PRT-000001",
                    "Bulb",
                    "Light Bulb",
                    "Electrical",
                    "suplier1",
                    "Box",
                    20,
                    10,
                    5,
                    50.00,
                    "Store Room",
                    "123456789",
                    "Active",
                    "Notes"
                ),
                (
                    "PRT-000002",
                    "Siliphos",
                    "Water purification crystals",
                    "Plumbing",
                    "supplier2",
                    "Bag",
                    10,
                    5,
                    2,
                    100.00,
                    "Workshop",
                    "987654321",
                    "Active",
                    "Notes"
                )
            ]

            cursor.executemany("""
                INSERT INTO inventory
                (
                    part_number,
                    part_name,
                    description,
                    category,
                    supplier_id,
                    unit,
                    quantity,
                    minimum_quantity,
                    reorder_quantity,
                    unit_cost,
                    location,
                    barcode,
                    status,
                    notes
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, inventory)

        conn.commit()
        conn.close()

    # ---------------------------------------------------------
    # SUPPLIERS
    # ---------------------------------------------------------
    @staticmethod
    def seed_sample_suppliers():
        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM suppliers")

        if cursor.fetchone()[0] == 0:

            suppliers = [
                (
                    "SUP-000001",
                    "Electrical Equipment cc",
                    "John Doe",
                    "444-220-1446",
                    "jhondoe@example.com",
                    "Mariental Portion 90",
                    "Active",
                    "Notes"
                ),
                (
                    "SUP-000002",
                    "Water Purification Suppliers",
                    "Jane Doe",
                    "333-251-789",
                    "janedoe@example.com",
                    "Windhoek Industrial 05",
                    "Active",
                    "Notes"
                )
            ]

            cursor.executemany("""
                INSERT INTO suppliers
                (
                    supplier_code,
                    supplier_name,
                    contact_person,
                    phone,
                    email,
                    address,
                    status,
                    notes
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, suppliers)

        conn.commit()
        conn.close()

    
import bcrypt

from app.database.connection import Database


LOOKUPS = {
    "Trades": [
        "Electrical",
        "Fitter",
        "Welder",
        "Plumber",
        "Mechanic",
        "Instrument Technisian"
    ],

    "Departments": [
        "Maintenance",
        "Production",
        "Warehouse",
        "Administration",
        "Operations"
    ],

    "Asset Categories": [
        "Electrical",
        "Mechanical",
        "Building",
        "Vehicle",
        "Prodution"
    ],

    "Asset Locations": [
        "Workshop",
        "Factory",
        "Warehouse",
        "Office",
    ],

    "Stauses": [
        "Active",
        "Inactive"
    ],

    "Prorities": [
        "Low",
        "Medium",
        "High",
        "Critical"
    ],

    "Frequency Types": [
        "Daily",
        "Weekly",
        "Monthly",
        "Quarterly",
        "Semi Annual",
        "Annual",
        "Running Hours"
    ],
}

DEFAULT_ADMIN = (
    "admin",
    "admin123",
    "System Administrator",
    "Administrator"
)

SAMPLE_SUPPLIERS = [

    (
        "SUP-0001",
        "ABC Industrial Suppliers",
        "John Smith",
        "0811234567",
        "sales@abcindustrial.com",
        "Windhoek",
        "Active",
        ""
    )

    (
        "SUP-0002",
        "Namibia Bearings",
        "Peter Jones",
        "0812345678",
        "info@nambearings.com",
        "Walvis Bay",
        "Active",
        ""
    )

    (
        "SUP-0003",
        "Electric World",
        "Sarah Brown",
        "0813456789",
        "sales@electricworld.com",
        "Widhoek",
        "Active",
        ""
    )
]

SAMPLE_ASSETS = [

    (
        "AST-0001",
        "Air Compressor",
        "Workshop air compressor",
        "Mechanical",
        "Workshop",
        "Atlas Copco",
        "GA30",
        "AC123456",
        "2022-01-15",
        "2027-01-15",
        "Active"
    ),

    (
        "AST-0002",
        "Generator",
        "Backup diesel generator",
        "Electrical",
        "Factory",
        "Cummins",
        "C550D5",
        "GEN987654",
        "2021-06-20",
        "2026-06-20",
        "Active"
    ),

    (
        "AST-0003",
        "Forklift",
        "3 Ton Diesel Forklift",
        "Vehicle",
        "Warehouse",
        "Toyota",
        "8FD30",
        "FL654321",
        "2020-09-01",
        "2025-09-01",
        "Active"
    ),

    (
        "AST-0004",
        "Conveyor Belt",
        "Production conveyor line",
        "Production",
        "Factory",
        "Siemens",
        "CV200",
        "CV123789",
        "2023-03-10",
        "2028-03-10",
        "Active"
    )

]

SAMPLE_TECHNICIANS = [

    (
        "EMP-0001",
        "John",
        "Smith",
        "0811111111",
        "john.smith@abc.com",
        "Electrician",
        "Maintenance",
        250.00,
        "Active"
    ),

    (
        "EMP-0002",
        "Peter",
        "Jones",
        "0812222222",
        "peter.jones@abc.com",
        "Mechanic",
        "Maintenance",
        240.00,
        "Active"
    ),

    (
        "EMP-0003",
        "Sarah",
        "Brown",
        "0813333333",
        "sarah.brown@abc.com",
        "Fitter",
        "Maintenance",
        230.00,
        "Active"
    ),

    (
        "EMP-0004",
        "Michael",
        "Williams",
        "0814444444",
        "michael.williams@abc.com",
        "Welder",
        "Maintenance",
        220.00,
        "Active"
    ),

    (
        "EMP-0005",
        "David",
        "Adams",
        "0815555555",
        "david.adams@abc.com",
        "Instrument Technician",
        "Maintenance",
        260.00,
        "Active"
    )

]

SUPPLIER_ABC = 1
SUPPLIER_BEARINGS = 2
SUPPLIER_ELECTRIC = 3
SUPPLIER_HYDRAULIC = 4
SUPPLIER_FASTENERS = 5

SAMPLE_INVENTORY = [

    (
        "PRT-0001",
        "Drive Belt",
        "Compressor drive belt",
        "Mechanical",
        SUPPLIER_ABC,
        "Each",
        10,
        2,
        5,
        350.00,
        "Store A",
        "",
        "Active",
        ""
    ),

    (
        "PRT-0002",
        "Bearing 6205",
        "Standard bearing",
        "Mechanical",
        SUPPLIER_BEARINGS,
        "Each",
        25,
        5,
        10,
        120.00,
        "Store A",
        "",
        "Active",
        ""
    ),

    (
        "PRT-0003",
        "Hydraulic Oil",
        "Hydraulic oil 20L",
        "Lubricants",
        SUPPLIER_HYDRAULIC,
        "Container",
        15,
        3,
        5,
        850.00,
        "Store B",
        "",
        "Active",
        ""
    ),

    (
        "PRT-0004",
        "Contactor 32A",
        "Electrical contactor",
        "Electrical",
        SUPPLIER_ELECTRIC,
        "Each",
        8,
        2,
        5,
        420.00,
        "Store C",
        "",
        "Active",
        ""
    )

]

AIR_COMPRESSOR = 1
GENERATOR = 2
FORKLIFT = 3
CONVEYOR = 4
COOLING_PUMP = 5
DISTRIBUTION_BOARD = 6

JOHN = 1
PETER = 2
SARAH = 3
MICHAEL = 4
DAVID = 5

SAMPLE_WORK_ORDERS = [

    (
        "WO-0001",
        AIR_COMPRESSOR,
        "Replace compressor belt",
        "Drive belt worn and slipping",
        "High",
        "Open",
        PETER,
        "Production Manager",
        "2026-07-01",
        "2026-07-10",
        1200.00,
        0,
        0,
        ""
    ),

    (
        "WO-0002",
        GENERATOR,
        "Replace generator battery",
        "Battery not holding charge",
        "Medium",
        "Assigned",
        JOHN,
        "Maintenance Manager",
        "2026-07-02",
        "2026-07-12",
        3500.00,
        0,
        0,
        ""
    ),

    (
        "WO-0003",
        CONVEYOR,
        "Replace conveyor bearing",
        "Bearing noise detected",
        "High",
        "In Progress",
        SARAH,
        "Production Supervisor",
        "2026-07-05",
        "2026-07-15",
        2000.00,
        0,
        3.5,
        ""
    )

]

SAMPLE_PM = [

    (
        "PM-0001",
        AIR_COMPRESSOR,
        "Inspect belts",
        "Check tension and wear",
        "Monthly",
        1,
        "2026-06-01",
        "2026-07-01",
        1.0,
        0,
        "Medium",
        1,
        ""
    ),

    (
        "PM-0002",
        GENERATOR,
        "Weekly generator test",
        "Run generator under load",
        "Weekly",
        1,
        "2026-07-01",
        "2026-07-08",
        1.5,
        0,
        "High",
        1,
        ""
    ),

    (
        "PM-0003",
        FORKLIFT,
        "Hydraulic inspection",
        "Check hoses and cylinders",
        "Monthly",
        1,
        "2026-06-15",
        "2026-07-15",
        2.0,
        0,
        "Medium",
        1,
        ""
    )

]

DATA_TABLES = [
    "preventive_maintenance",
    "work_orders",
    "inventory",
    "assets",
    "suppliers",
    "technicians"
]

SYSTEM_TABLES = [
    "lookups",
    "users"
]

class DatabaseSeeder:

    @staticmethod
    def seed():

        print("Seeding database...")

        DatabaseSeeder.seed_default_admin()
        DatabaseSeeder.seed_lookup_values()
        DatabaseSeeder.seed_suppliers()
        DatabaseSeeder.seed_assets()
        DatabaseSeeder.seed_technicians()
        DatabaseSeeder.seed_inventory()
        DatabaseSeeder.seed_work_orders()
        DatabaseSeeder.seed_preventive_maintenance()

        print("Database seeding complete.")

    @staticmethod
    def seed_default_admin():

        conn = Database.connect()
        cursor = conn.cursor()

        username, password, fullname, role = DEFAULT_ADMIN

        password_hash = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        ).decode()

        cursor.execute("""
            INSERT OR IGNORE INTO users
            (
                username,
                password_hash,
                fullname,
                role,
                active
            )
            VALUES(?, ?, ?, ?, )
        """, (
            username,
            password_hash,
            fullname,
            role
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def seed_suppliers():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.executemany("""
            INSERT OR IGNORE INTO suppliers
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
            VALUES
            (
                ?, ?, ?, ?, ?, ?, ?, ?
            )
        """, SAMPLE_SUPPLIERS)

        conn.commit()
        conn.close()

    @staticmethod
    def seed_assets():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.executemany("""
            INSERT OR IGNORE INTO assets
            (
                asste_number,
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
            VALUES
            (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
        """, SAMPLE_ASSETS)

        conn.commit()
        conn.close()

    @staticmethod
    def seed_technicians():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.executemany("""
            INSERT OR IGNORE INTO technicians
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
            VALUES
            (
                ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
        """, SAMPLE_TECHNICIANS)

        conn.commit()
        conn.close()

    @staticmethod
    def seed_inventory():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.executemany("""
            INSERT OR IGNORE INTO inventory
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
            VALUES
            (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
        """, SAMPLE_INVENTORY)

        conn.commit()
        conn.close()

    @staticmethod
    def seed_work_orders():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.executemany("""
            INSERT OR IGNORE INTO work_orders
            (
                work_order_number,
                asset_id,
                description,
                priority,
                satatus,
                technician_id,
                requested_by
                date_created,
                estimated_cost,
                actual_cost,
                labour_hours,
                notes
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
        """, SAMPLE_WORK_ORDERS)

        conn.commit()
        conn.close()

    @staticmethod
    def seed_preventive_maintenance():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.executemany("""
            INSERT OR IGNORE INTO preventive maintenance
            (
                pm_number,
                asset_id,
                task,
                description,
                frequenct_type,
                frequency_value,
                last_service_date,
                next_due_date,
                estimated_hours,
                estimated_cost,
                priority,
                active,
                notes
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
        """, SAMPLE_PM)

        conn.commit()
        conn.close()

    @staticmethod
    def clear_demo_data():

        conn = Database.connect()
        cursor = conn.cursor()

        # Foreign kyes must be disabled while deleting
        cursor.execute("PRAGMA foreign_kyes = OFF")

        tables = [
            "prevntive_maintenance",
            "work_orders",
            "inventory",
            "assets",
            "suppliers",
            "technicians"
        ]

        for table in DatabaseSeeder.DATA_TABLES:
            cursor.execute(f"DELETE from {table}")

        # Remove lookup values
        cursor.execute("DELETE FROM lookups")

        # Keep the default administrator
        cursor.execute("""
            DELETE FROM users
            WHERE username <> 'admin'
        """)

        cursor.execute("PRAGMA foreign_keys = ON")

        conn.commit()
        conn.close()

        print("Demmo data deleted")

    @staticmethod
    def reset_demo_data():

        DatabaseSeeder.clear_demo_data()

        DatabaseSeeder.seed_lookup_values()
        DatabaseSeeder.seed_suppliers()
        DatabaseSeeder.seed_assets()
        DatabaseSeeder.seed_technicians()
        DatabaseSeeder.seed_inventory()
        DatabaseSeeder.seed_work_orders()
        DatabaseSeeder.seed_preventive_maintenance()

        print("Demo data recreated.")

    @staticmethod
    def clear_all():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_keys = OFF")

        tables = [
            "preventive_maintenance",
            "work_orders",
            "inventory",
            "assets",
            "suppliers",
            "technicians",
            "lookups",
            "users"
        ]

        for table in DatabaseSeeder.DATA_TABLES:
            cursor.execute(f"DELETE FROM {table}")

        cursor.execute("PRAGMA foreign_keys = ON")

        conn.commit()
        conn.close()

        print("Database cleared.")
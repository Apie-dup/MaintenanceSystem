# Database Documentation

The Maintenance Management System uses a SQLite database.

All database access is performed through

Database.connect()

Foreign keys are enabled.

---

# Database Overview

```
Users
 │
 ├── Assets
 │      │
 │      ├── Preventive Maintenance
 │      │
 │      └── Work Orders
 │               │
 │               └── Work Order Parts
 │
 ├── Inventory
 │        │
 │        └── Suppliers
 │
 └── Technicians
```

---

# Users

Purpose

Stores application login accounts.

| Column | Type | Description |
|---------|------|-------------|
| id | INTEGER | Primary Key |
| username | TEXT | Login name |
| password_hash | TEXT | bcrypt password hash |
| full_name | TEXT | Display name |
| role | TEXT | User role |
| active | INTEGER | Active account |
| created_at | TEXT | Creation date |

---

# Assets

Purpose

Stores company assets.

| Column | Type |
|---------|------|
| id | INTEGER |
| asset_number | TEXT |
| asset_name | TEXT |
| description | TEXT |
| category | TEXT |
| location | TEXT |
| manufacturer | TEXT |
| model | TEXT |
| serial_number | TEXT |
| purchase_date | TEXT |
| warranty_expiry | TEXT |
| status | TEXT |
| created_at | TEXT |

---

# Suppliers

Purpose

Stores approved suppliers.

| Column | Type |
|---------|------|
| id | INTEGER |
| supplier_code | TEXT |
| supplier_name | TEXT |
| contact_person | TEXT |
| phone | TEXT |
| email | TEXT |
| address | TEXT |
| status | TEXT |
| notes | TEXT |
| created_at | TEXT |

---

# Inventory

Purpose

Stores spare parts inventory.

| Column | Type |
|---------|------|
| id | INTEGER |
| part_number | TEXT |
| part_name | TEXT |
| description | TEXT |
| category | TEXT |
| supplier_id | INTEGER |
| unit | TEXT |
| quantity | REAL |
| minimum_quantity | REAL |
| reorder_quantity | REAL |
| unit_cost | REAL |
| location | TEXT |
| barcode | TEXT |
| status | TEXT |
| notes | TEXT |
| created_at | TEXT |

Foreign Keys

supplier_id → suppliers.id

---

# Technicians

Purpose

Stores maintenance personnel.

| Column | Type |
|---------|------|
| id | INTEGER |
| employee_number | TEXT |
| first_name | TEXT |
| last_name | TEXT |
| phone | TEXT |
| email | TEXT |
| trade | TEXT |
| department | TEXT |
| hourly_rate | REAL |
| status | TEXT |
| created_at | TEXT |

---

# Work Orders

Purpose

Stores corrective maintenance work.

| Column | Type |
|---------|------|
| id | INTEGER |
| work_order_number | TEXT |
| asset_id | INTEGER |
| title | TEXT |
| description | TEXT |
| priority | TEXT |
| status | TEXT |
| technician_id | INTEGER |
| requested_by | TEXT |
| date_created | TEXT |
| due_date | TEXT |
| estimated_cost | REAL |
| actual_cost | REAL |
| labour_hours | REAL |
| notes | TEXT |
| created_at | TEXT |

Foreign Keys

asset_id → assets.id

technician_id → technicians.id

---

# Work Order Parts

Purpose

Tracks inventory issued to work orders.

| Column | Type |
|---------|------|
| id | INTEGER |
| work_order_id | INTEGER |
| inventory_id | INTEGER |
| quantity | REAL |
| unit_cost | REAL |
| total_cost | REAL |
| notes | TEXT |
| created_at | TEXT |

Foreign Keys

work_order_id → work_orders.id

inventory_id → inventory.id

---

# Preventive Maintenance

Purpose

Stores recurring maintenance schedules.

| Column | Type |
|---------|------|
| id | INTEGER |
| pm_number | TEXT |
| asset_id | INTEGER |
| task | TEXT |
| description | TEXT |
| frequency_type | TEXT |
| frequency_value | INTEGER |
| last_service_date | TEXT |
| next_due_date | TEXT |
| estimated_hours | REAL |
| estimated_cost | REAL |
| priority | TEXT |
| active | INTEGER |
| notes | TEXT |
| created_at | TEXT |

Foreign Keys

asset_id → assets.id
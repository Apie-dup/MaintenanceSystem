# Application Architecture

## Overview

The application follows a layered architecture that separates
the User Interface, Business Logic and Database.

```
Main Window
      │
      ▼
 Pages / Dialogs
      │
      ▼
   Services
      │
      ▼
    Models
      │
      ▼
 SQLite Database
```

---

## User Interface

Pages

- Dashboard
- Assets
- Inventory
- Suppliers
- Technicians
- Work Orders

Dialogs

- AssetDialog
- InventoryDialog
- SupplierDialog
- TechnicianDialog
- WorkOrderDialog
- IssuePartDialog

---

## Base Classes

BasePage

Common functionality shared by all pages.

CrudPage

Provides:

- Add
- Edit
- Delete
- Refresh
- Search
- Table handling

BaseDialog

Provides:

- Add/Edit mode
- Validation
- Save
- Message helpers

---

## Services

Business logic belongs in services.

Services never communicate directly with the UI.

---

## Models

Models contain all SQL.

Models never communicate with the UI.

---

## Database

SQLite

All database access is centralized through

Database.connect()

---

## Helpers

TableHelper

LookupManager

FormatHelper

DateHelper

Logger

Settings

CodeGenerator
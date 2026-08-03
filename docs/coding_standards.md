# Coding Standards

This document defines the coding standards used throughout the
Maintenance Management System project.

Following these standards keeps the codebase clean,
consistent and maintainable.

---

# Python Style

The project follows the PEP 8 Python style guide where practical.

Examples

Good

asset_name

work_order_number

supplier_id

Avoid

AssetName

WorkOrderNumber

SupplierID

---

# Naming Conventions

## Classes

Use PascalCase.

Examples

AssetDialog

InventoryService

SupplierModel

CrudPage

BaseDialog

---

## Functions

Use snake_case.

Examples

load_data()

get_all()

save()

delete_record()

---

## Variables

Use snake_case.

Examples

asset_number

supplier_name

estimated_cost

---

## Constants

Use UPPER_CASE.

Examples

PAGE_TITLE

TABLE_COLUMNS

SEARCH_FIELDS

BUTTON_WIDTH

---

# File Naming

Use snake_case.

Examples

asset_dialog.py

inventory_service.py

supplier_model.py

work_order_page.py

Avoid

AssetDialog.py

InventoryService.py

---

# Folder Responsibilities

Pages

User interface pages.

Dialogs

Add/Edit dialogs.

Services

Business logic.

Models

Database access.

Helpers

Reusable helper functions.

Core

Infrastructure.

Database

Connection, setup, migrations.

---

# Database Rules

Never execute SQL inside:

Pages

Dialogs

Services

SQL belongs only inside Models.

Example

Page

↓

Service

↓

Model

↓

Database

---

# Service Rules

Services contain business logic.

Services communicate with Models.

Services never communicate directly with the database.

Standard CRUD methods

get_all()

get_by_id()

search()

create()

update()

delete()

---

# Model Rules

Models contain SQL only.

Standard methods

get_all()

get_by_id()

insert()

update()

delete()

search()

Helper methods are allowed.

Examples

get_next_asset_number()

get_low_stock()

get_active_suppliers()

---

# Dialog Rules

Every CRUD dialog inherits from

BaseDialog

Required methods

clear_fields()

get_form_data()

set_form_data()

load_record()

validate()

save()

---

# Page Rules

Every CRUD page inherits from

CrudPage

Required methods

__init__()

setup_page()

connect_signals()

Avoid duplicating CRUD functionality already provided by CrudPage.

---

# Qt Designer

Always edit

.ui

files.

Never edit generated

ui_*.py

files.

Regenerate after every UI change.

---

# Widget Naming

Buttons

btnSave

btnDelete

btnRefresh

Text boxes

txtAssetName

txtSupplierCode

Combo boxes

cmbStatus

cmbPriority

Tables

tblInventory

tblAssets

Labels

lblTitle

lblStatus

Check boxes

chkActive

Spin boxes

spnQuantity

Double spin boxes

dsbUnitCost

Date edits

dtPurchaseDate

Text edits

teDescription

---

# Comments

Use section comments.

Example

# -------------------------------------------------
# Load Data
# -------------------------------------------------

Avoid excessive inline comments.

Write self-explanatory code.

---

# Docstrings

Public classes should include docstrings.

Example

"""
Inventory service.

Contains business logic for inventory.
"""

Public helper methods should include short descriptions.

---

# Error Handling

Never ignore exceptions.

Catch expected exceptions.

Show user-friendly messages.

Log unexpected exceptions.

---

# Logging

Use

logger.info()

logger.warning()

logger.exception()

Avoid using

print()

except for temporary debugging.

---

# Formatting

Use FormatHelper for

Currency

Quantities

Percentages

Dates

Avoid formatting values directly inside pages.

---

# Date Handling

Use DateHelper whenever possible.

Avoid duplicating date calculations.

---

# Lookups

Use LookupManager.

Avoid hard-coded combo box values inside dialogs.

---

# Code Generation

Use CodeGenerator for

Assets

Suppliers

Inventory

Technicians

Work Orders

Preventive Maintenance

Avoid duplicate numbering logic.

---

# Imports

Standard Library

Third-party Libraries

Application Imports

Example

import sqlite3

from PySide6.QtWidgets import QWidget

from app.services.asset_service import AssetService

---

# Maximum Method Size

Aim for

20–40 lines

If a method grows much larger, consider splitting it into helper methods.

---

# Git

Commit frequently.

Use meaningful commit messages.

Examples

Added inventory module

Refactored CrudPage

Added Work Order Parts

Improved logging

Avoid commits like

Update

Changes

Fix

---

# General Principle

Prefer reusable code over duplicated code.

If code appears in more than one place,
consider moving it into a helper,
base class,
or service.
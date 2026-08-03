# Design Principles

The project follows these principles.

---

## Separation of Concerns

UI

Displays data only.

Services

Business logic.

Models

Database access.

---

## CRUD Standard

Every CRUD page inherits from CrudPage.

Every CRUD dialog inherits from BaseDialog.

Every service exposes

- get_all()
- get_by_id()
- search()
- create()
- update()
- delete()

Every model exposes

- get_all()
- get_by_id()
- insert()
- update()
- delete()
- search()

---

## Database Rules

Never execute SQL from a page.

Never execute SQL from a dialog.

All SQL belongs in Models.

---

## User Interface

Use Qt Designer.

Never edit generated ui_*.py files.

Always edit .ui files and regenerate.

---

## Reuse

Common functionality belongs in helper classes.

Avoid duplicate code.

---

## Naming

Classes

PascalCase

Functions

snake_case

Constants

UPPER_CASE

Database columns

snake_case

Widget names

camelCase with prefixes.

Examples

txtAssetName

cmbStatus

tblInventory

btnSave

lblTitle
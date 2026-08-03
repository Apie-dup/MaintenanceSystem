# Project Structure

The Maintenance Management System follows a modular architecture.

Each folder has a specific responsibility.

---

MaintenanceSystem

│
├── app
├── database
├── docs
├── logs
├── resources
├── requirements.txt
├── main.py
└── README.md

---

# app

Contains all application source code.

---

## base

Shared base classes.

Files

base_dialog.py

Generic dialog functionality.

base_page.py

Common page functionality.

crud_page.py

Reusable CRUD operations.

---

## controllers

Application controllers.

login_controller.py

Handles user authentication.

main_controller.py

Main application window.

Controllers are only used for application flow.

Business logic belongs in Services.

---

## dialogs

All Add/Edit dialogs.

Examples

AssetDialog

InventoryDialog

SupplierDialog

TechnicianDialog

WorkOrderDialog

IssuePartDialog

Dialogs communicate only with Services.

---

## models

Database layer.

Contains SQL statements only.

Models never communicate with the UI.

Typical methods

get_all()

get_by_id()

insert()

update()

delete()

search()

---

## services

Business logic layer.

Services communicate between the UI and Models.

Examples

AssetService

InventoryService

SupplierService

TechnicianService

WorkOrderService

---

## pages

Main pages displayed inside the Main Window.

Examples

DashboardPage

AssetsPage

InventoryPage

SuppliersPage

TechniciansPage

WorkOrdersPage

PreventiveMaintenancePage

Pages inherit from CrudPage whenever possible.

---

## helpers

Reusable helper classes.

Examples

TableHelper

LookupHelper

FormatHelper

DateHelper

CodeGenerator

Helpers contain no business logic.

---

## core

Application infrastructure.

Examples

Database Connection

Logger

Settings

LookupManager

IconManager

Signals

---

## ui

Qt Designer files.

ui/

    forms/

        *.ui

    generated/

        ui_*.py

Never edit generated Python files.

Always edit the .ui files.

---

## utils

General utility classes.

Examples

Validators

Converters

File utilities

---

# database

SQLite database.

maintenance.db

Database setup

Database migrations

Seed data

---

# resources

Application resources.

icons/

images/

styles/

future translations

---

# docs

Project documentation.

README

Architecture

Database

Roadmap

Coding Standards

Project Structure

Deployment

Backup Procedures

---

# logs

Application log files.

Example

maintenance.log

---

# main.py

Application entry point.

Responsible for

Creating QApplication

Initializing database

Showing Login Window

Launching Main Window

---

# Design Rules

Pages never execute SQL.

Dialogs never execute SQL.

Services contain business logic.

Models contain SQL.

Helpers contain reusable functionality.

Generated UI files are never edited.

Business logic is never duplicated.
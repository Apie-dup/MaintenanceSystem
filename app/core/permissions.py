class Permissions:

    ROLE_PERMISSIONS = {

        # =================================================
        # Administrator
        # =================================================

        "Administrator": {

            # Pages
            "dashboard",
            "assets",
            "work_orders",
            "pm",
            "technicians",
            "inventory",
            "suppliers",
            "reports",
            "lookups",
            "settings",
            "users",

            # Assets
            "assets.create",
            "assets.edit",
            "assets.delete",

            # Work Orders
            "work_orders.create",
            "work_orders.edit",
            "work_orders.complete",
            "work_orders.close",
            "work_orders.reopen",
            "work_orders.issue_parts",
            "work_orders.remove_parts",

            # Preventive Maintenance
            "pm.create",
            "pm.edit",
            "pm.delete",
            "pm.generate_work_order",

            # Technicians
            "technicians.create",
            "technicians.edit",
            "technicians.delete",

            # Inventory
            "inventory.create",
            "inventory.edit",
            "inventory.delete",

            # Suppliers
            "suppliers.create",
            "suppliers.edit",
            "suppliers.delete",

            # Reports
            "reports.export",

            # Administration
            "lookups.manage",
            "settings.edit",

            "users.create",
            "users.edit",
            "users.activate",
        },

        # =================================================
        # Maintenance Manager
        # =================================================

        "Maintenance Manager": {

            # Pages
            "dashboard",
            "assets",
            "work_orders",
            "pm",
            "technicians",
            "inventory",
            "suppliers",
            "reports",

            # Assets
            "assets.create",
            "assets.edit",

            # Work Orders
            "work_orders.create",
            "work_orders.edit",
            "work_orders.complete",
            "work_orders.close",
            "work_orders.reopen",
            "work_orders.issue_parts",
            "work_orders.remove_parts",

            # Preventive Maintenance
            "pm.create",
            "pm.edit",

            # Technicians
            "technicians.create",
            "technicians.edit",

            # Inventory
            "inventory.create",
            "inventory.edit",

            # Suppliers
            "suppliers.create",
            "suppliers.edit",

            # Reports
            "reports.export",
        },

        # =================================================
        # Technician
        # =================================================

        "Technician": {

            # Pages
            "dashboard",
            "work_orders",
            "inventory",

            # Work Orders
            "work_orders.update",
            "work_orders.complete",
            "work_orders.issue_parts",

            # Inventory is view-only through the
            # Inventory page for now.
        },

        # =================================================
        # Viewer
        # =================================================

        "Viewer": {

            # Pages only
            "dashboard",
            "assets",
            "work_orders",
            "pm",
            "reports",

            # Viewer may export reports.
            "reports.export",
        },
    }

    # -------------------------------------------------
    # Permission check
    # -------------------------------------------------

    @staticmethod
    def has_permission(
        role,
        permission
    ):

        permissions = (
            Permissions
            .ROLE_PERMISSIONS
            .get(role, set())
        )

        return (
            permission in permissions
        )
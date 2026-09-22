from app.database.connection import Database

from app.models.work_order_labour_model import (
    WorkOrderLabourModel
)
from app.models.work_order_model import WorkOrderModel
from app.services.work_order_history_service import (
    WorkOrderHistoryService
)


class WorkOrderLabourService:

    @staticmethod
    def get_by_work_order(work_order_id):
        return WorkOrderLabourModel.get_by_work_order(
            work_order_id
        )

    @staticmethod
    def get_by_id(labour_id):
        return WorkOrderLabourModel.get_by_id(
            labour_id
        )

    @staticmethod
    def get_total_hours(
        work_order_id,
        connection=None
    ):
        return WorkOrderLabourModel.get_total_hours(
            work_order_id,
            connection=connection
        )

    @staticmethod
    def get_total_cost(
        work_order_id,
        connection=None
    ):
        return WorkOrderLabourModel.get_total_cost(
            work_order_id,
            connection=connection
        )

    @staticmethod
    def add_labour(data):
        work_order_id = data.get(
        "work_order_id"
    )

        technician_id = data.get(
            "technician_id"
        )

        work_date = (
            data.get("work_date") or ""
        ).strip()

        hours = float(
            data.get("hours") or 0
        )

        hourly_rate = float(
            data.get("hourly_rate") or 0
        )

        if work_order_id is None:
            raise ValueError(
                "Work Order is required."
            )

        if technician_id is None:
            raise ValueError(
                "Technician is required."
            )

        if not work_date:
            raise ValueError(
                "Work Date is required."
            )

        if hours <= 0:
            raise ValueError(
                "Labour Hours must be greater than zero."
            )

        if hourly_rate < 0:
            raise ValueError(
                "Hourly Rate cannot be negative."
            )

        labour_cost = (
            hours * hourly_rate
        )

        labour_data = dict(data)

        labour_data["hours"] = hours
        labour_data["hourly_rate"] = hourly_rate
        labour_data["labour_cost"] = labour_cost

        conn = Database.connect()

        try:
            # ---------------------------------------------
            # Work Order
            # ---------------------------------------------

            work_order = (
                WorkOrderModel.get_by_id(
                    work_order_id,
                    connection=conn
                )
            )

            if work_order is None:
                raise ValueError(
                    "Work Order was not found."
                )

            # ---------------------------------------------
            # Technician
            # ---------------------------------------------

            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    first_name,
                    last_name
                FROM technicians
                WHERE id = ?
            """, (
                technician_id,
            ))

            technician = cursor.fetchone()

            if technician is None:
                raise ValueError(
                    "Technician was not found."
                )
            technician_name = (
                f"{technician['first_name']} "
                f"{technician['last_name']}"
            ).strip()

            # ---------------------------------------------
            # Existing detailed labour
            # ---------------------------------------------

            existing_hours = (
                WorkOrderLabourModel.get_total_hours(
                    work_order_id,
                    connection=conn
                )
            )

            legacy_hours = float(
                work_order["labour_hours"] or 0
            )

            # ---------------------------------------------
            # Protect legacy labour
            # ---------------------------------------------

            if (
                existing_hours <= 0
                and legacy_hours > 0
            ):
                raise ValueError(
                    "This Work Order already contains "
                    "legacy labour hours. Clear or migrate "
                    "the existing labour hours before "
                    "adding detailed labour entries."
                )

            # ---------------------------------------------
            # Add labour
            # ---------------------------------------------

            labour_id = (
                WorkOrderLabourModel.insert(
                    labour_data,
                    connection=conn
                )
            )

            # ---------------------------------------------
            # Synchronize Work Order
            # ---------------------------------------------

            WorkOrderLabourService.synchronize_work_order(
                work_order_id,
                connection=conn
            )

            # ---------------------------------------------
            # Audit History
            # ---------------------------------------------

            WorkOrderHistoryService.add(
                work_order_id,
                action="Labour Added",
                field_name="Labour",
                old_value=None,
                new_value=(
                    f"{hours:g} hrs"
                ),
                notes=(
                    f"{technician_name} - "
                    f"{hours:g} hours @ "
                    f"{hourly_rate:.2f} = "
                    f"{labour_cost:.2f}."
                ),
                user_id=data.get(
                    "user_id"
                ),
                username=data.get(
                    "username"
                ),
                conn=conn
            )

            # ---------------------------------------------
            # Everything succeeded
            # ---------------------------------------------

            conn.commit()

            return labour_id

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()    

    @staticmethod
    def delete_labour(
        labour_id,
        user=None
    ):
        conn = Database.connect()

        try:
            # ---------------------------------------------
            # Labour Entry
            # ---------------------------------------------

            labour = (
                WorkOrderLabourModel.get_by_id(
                    labour_id,
                    connection=conn
                )
            )

            if labour is None:
                raise ValueError(
                    "Labour entry was not found."
                )

            work_order_id = (
                labour["work_order_id"]
            )

            hours = float(
                labour["hours"] or 0
            )

            hourly_rate = float(
                labour["hourly_rate"] or 0
            )

            labour_cost = float(
                labour["labour_cost"] or 0
            )

            # ---------------------------------------------
            # Technician
            # ---------------------------------------------

            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    first_name,
                    last_name
                FROM technicians
                WHERE id = ?
            """, (
                labour["technician_id"],
            ))

            technician = cursor.fetchone()

            technician_name = ""

            if technician is not None:
                technician_name = (
                    f"{technician['first_name']} "
                    f"{technician['last_name']}"
                ).strip()

            # ---------------------------------------------
            # Delete Labour
            # ---------------------------------------------

            WorkOrderLabourModel.delete(
                labour_id,
                connection=conn
            )

            # ---------------------------------------------
            # Synchronize Work Order
            # ---------------------------------------------

            WorkOrderLabourService.synchronize_work_order(
                work_order_id,
                connection=conn
            )

            # ---------------------------------------------
            # Audit History
            # ---------------------------------------------

            WorkOrderHistoryService.add(
                work_order_id,
                action="Labour Removed",
                field_name="Labour",
                old_value=(
                    f"{hours:g} hrs"
                ),
                new_value=None,
                notes=(
                    f"{technician_name} - "
                    f"{hours:g} hours @ "
                    f"{hourly_rate:.2f} = "
                    f"{labour_cost:.2f}."
                ),
                user_id=(
                    user.get("id")
                    if user
                    else None
                ),
                username=(
                    user.get("username")
                    if user
                    else None
                ),
                conn=conn
            )

            # ---------------------------------------------
            # Everything succeeded
            # ---------------------------------------------

            conn.commit()

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    @staticmethod
    def synchronize_work_order(
        work_order_id,
        connection
    ):
        total_hours = (
            WorkOrderLabourModel.get_total_hours(
                work_order_id,
                connection=connection
            )
        )

        WorkOrderModel.update_labour_hours(
            work_order_id,
            total_hours,
            connection=connection
        )

        actual_cost = (
            WorkOrderModel.calculate_actual_cost(
                work_order_id,
                connection=connection
            )
        )

        WorkOrderModel.update_actual_cost(
            work_order_id,
            actual_cost,
            connection=connection
        )
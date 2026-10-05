from app.models.vehicle_sop_inspection_model import (
    VehicleSopInspectionModel
)
from app.models.vehicle_sop_inspection_item_model import (
    VehicleSopInspectionItemModel
)
from app.models.vehicle_sop_model import (
    VehicleSopModel
)
from app.models.vehicle_sop_item_model import (
    VehicleSopItemModel
)
from app.database.connection import Database

from app.services.asset_meter_reading_service import (
    AssetMeterReadingService
)
from app.services.work_order_service import WorkOrderService


class VehicleSopInspectionService:

    RESULTS = [
        "Pass",
        "Fail",
        "N/A",
    ]

    STATUSES = [
        "In Progress",
        "Completed",
    ]

    # ---------------------------------------------------------
    # Read
    # ---------------------------------------------------------

    @staticmethod
    def get_all():

        return (
            VehicleSopInspectionModel.get_all()
        )

    @staticmethod
    def get_by_id(inspection_id):

        return (
            VehicleSopInspectionModel.get_by_id(
                inspection_id
            )
        )

    @staticmethod
    def get_items(inspection_id):

        return (
            VehicleSopInspectionItemModel
            .get_by_inspection_id(
                inspection_id
            )
        )

    @staticmethod
    def search(text):

        text = (text or "").strip()

        if not text:
            return (
                VehicleSopInspectionModel.get_all()
            )

        return (
            VehicleSopInspectionModel.search(
                text
            )
        )

    # ---------------------------------------------------------
    # Lookups
    # ---------------------------------------------------------

    @staticmethod
    def get_next_inspection_number():

        return (
            VehicleSopInspectionModel
            .get_next_inspection_number()
        )

    @staticmethod
    def get_results():

        return list(
            VehicleSopInspectionService.RESULTS
        )

    @staticmethod
    def get_statuses():

        return list(
            VehicleSopInspectionService.STATUSES
        )

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    @staticmethod
    def validate_new_inspection(data):

        sop_id = data.get("sop_id")

        if not sop_id:
            raise ValueError(
                "Vehicle SOP is required."
            )

        sop = VehicleSopModel.get_by_id(
            sop_id
        )

        if not sop:
            raise ValueError(
                "Vehicle SOP was not found."
            )

        if not sop["active"]:
            raise ValueError(
                "The selected Vehicle SOP is inactive."
            )

        if not data.get("inspection_date"):
            raise ValueError(
                "Inspection Date is required."
            )

        return sop

    # ---------------------------------------------------------
    # Create inspection
    # ---------------------------------------------------------

    @staticmethod
    def create(data):

        sop = (
            VehicleSopInspectionService
            .validate_new_inspection(data)
        )

        sop_items = (
            VehicleSopItemModel.get_by_sop_id(
                sop["id"]
            )
        )

        if not sop_items:
            raise ValueError(
                "The selected Vehicle SOP has no "
                "checklist items."
            )

        inspection_data = {
            "inspection_number":
                VehicleSopInspectionService
                .get_next_inspection_number(),

            "sop_id":
                sop["id"],

            "asset_id":
                sop["asset_id"],

            "sop_number":
                sop["sop_number"],

            "sop_name":
                sop["sop_name"],

            "frequency":
                sop["frequency"],

            "inspection_date":
                data["inspection_date"],

            "operator_name":
                (
                    data.get("operator_name")
                    or ""
                ).strip(),

            "meter_type":
                data.get("meter_type"),

            "meter_reading":
                data.get("meter_reading"),

            "status":
                "In Progress",

            "comments":
                (
                    data.get("comments")
                    or ""
                ).strip(),
        }

        snapshot_items = []

        for sop_item in sop_items:
            snapshot_items.append({
                "sop_item_id":
                    sop_item["id"],

                "sequence":
                    sop_item["sequence"],

                "check_description":
                    sop_item[
                        "check_description"
                    ],

                "required":
                    sop_item["required"],

                "result":
                    None,

                "comments":
                    "",
            })

        inspection_id = (
            VehicleSopInspectionModel
            .create_with_items(
                inspection_data,
                snapshot_items,
            )
        )

        return inspection_id

    # ---------------------------------------------------------
    # Update inspection header
    # ---------------------------------------------------------

    @staticmethod
    def update(data):

        inspection_id = data.get("id")

        if not inspection_id:
            raise ValueError(
                "Inspection ID is required."
            )

        inspection = (
            VehicleSopInspectionModel.get_by_id(
                inspection_id
            )
        )

        if not inspection:
            raise ValueError(
                "Vehicle SOP inspection was not found."
            )

        if inspection["status"] == "Completed":
            raise ValueError(
                "Completed inspections cannot be modified."
        )

        status = data.get(
            "status",
            inspection["status"]
        )

        if status not in (
            VehicleSopInspectionService.STATUSES
        ):
            raise ValueError(
                "Invalid inspection status."
            )

        update_data = {
            "id":
                inspection_id,

            "inspection_date":
                data.get(
                    "inspection_date",
                    inspection["inspection_date"]
                ),

            "operator_name":
                data.get(
                    "operator_name",
                    inspection["operator_name"]
                ),

            "meter_type":
                data.get(
                    "meter_type",
                    inspection["meter_type"]
                ),

            "meter_reading":
                data.get(
                    "meter_reading",
                    inspection["meter_reading"]
                ),

            "status": inspection["status"],

            "comments":
                data.get(
                    "comments",
                    inspection["comments"]
                ),
        }

        VehicleSopInspectionModel.update(
            update_data
        )

    # ---------------------------------------------------------
    # Update checklist result
    # ---------------------------------------------------------

    @staticmethod
    def update_item_result(
        item_id,
        result,
        comments=None,
    ):

        item = (
            VehicleSopInspectionItemModel
            .get_by_id(
                item_id
            )
        )

        if not item:
            raise ValueError(
                "Inspection checklist item "
                "was not found."
            )

        inspection = (
            VehicleSopInspectionModel.get_by_id(
                item["inspection_id"]
            )
        )

        if not inspection:
            raise ValueError(
                "Vehicle SOP inspection was not found."
            )

        if inspection["status"] == "Completed":
            raise ValueError(
                "Completed inspections cannot be modified."
            )

        if result not in (
            VehicleSopInspectionService.RESULTS
        ):
            raise ValueError(
                "Result must be Pass, Fail, "
                "or N/A."
            )

        VehicleSopInspectionItemModel.update_result(
            item_id,
            result,
            (comments or "").strip(),
        )

    # ---------------------------------------------------------
    # Complete inspection
    # ---------------------------------------------------------

    @staticmethod
    def complete(inspection_id):

        inspection = (
            VehicleSopInspectionModel.get_by_id(
                inspection_id
            )
        )

        if not inspection:
            raise ValueError(
                "Vehicle SOP inspection was not found."
            )

        if inspection["status"] == "Completed":
            raise ValueError(
                "The inspection is already completed."
            )

        items = (
            VehicleSopInspectionItemModel
            .get_by_inspection_id(
                inspection_id
            )
        )

        if not items:
            raise ValueError(
                "The inspection has no checklist items."
            )

        for item in items:

            result = item["result"]

            if item["required"] and not result:
                raise ValueError(
                    "All required checklist items "
                    "must have a result before the "
                    "inspection can be completed."
                )

            if (
                result
                and result
                not in VehicleSopInspectionService.RESULTS
            ):
                raise ValueError(
                    "One or more checklist items "
                    "contain an invalid result."
                )

        update_data = {
            "id": inspection_id,
            "inspection_date":
                inspection["inspection_date"],
            "operator_name":
                inspection["operator_name"],
            "meter_type":
                inspection["meter_type"],
            "meter_reading":
                inspection["meter_reading"],
            "status": "Completed",
            "comments":
                inspection["comments"],
        }

        conn = Database.connect()

        try:

            meter_type = inspection["meter_type"]
            meter_reading = inspection["meter_reading"]

            if (
                meter_type
                and meter_reading is not None
            ):
                AssetMeterReadingService.add_reading(
                    asset_id=inspection["asset_id"],
                    meter_type=meter_type,
                    reading=meter_reading,
                    reading_date=(
                        inspection["inspection_date"]
                    ),
                    notes=(
                        "Recorded from SOP inspection "
                        f"{inspection['inspection_number']}."
                    ),
                    source_type="SOP Inspection",
                    sop_inspection_id=inspection_id,
                    conn=conn,
                )

            VehicleSopInspectionModel.update(
                update_data,
                conn=conn,
            )

            conn.commit()

        except Exception:

            conn.rollback()
            raise

        finally:
            conn.close()

    # ----------------------------------------------------------------
    # Delete
    # ----------------------------------------------------------------

    @staticmethod
    def delete(inspection_id):

        inspection = (
            VehicleSopInspectionModel.get_by_id(
                inspection_id
            )
        )

        if not inspection:
            raise ValueError(
                "SOP inspection was not found."
            )

        if inspection["status"] == "Completed":
            raise ValueError(
                "Completed inspections cannot be deleted."
            )

        VehicleSopInspectionModel.delete(
            inspection_id
        )


    @staticmethod
    def create_work_order_for_failed_item(
        inspection_id,
        inspection_item_id,
        user=None
    ):
        inspection = (
            VehicleSopInspectionService.get_by_id(
                inspection_id
            )
        )

        if inspection is None:
            raise ValueError(
                "SOP inspection not found."
            )

        if inspection["status"] != "Completed":
            raise ValueError(
                "A Work Order can only be created "
                "from a completed SOP inspection."
            )

        inspection_item = (
            VehicleSopInspectionItemModel.get_by_id(
                inspection_item_id
            )
        )

        if inspection_item is None:
            raise ValueError(
                "SOP inspection item not found."
            )

        if (
            inspection_item["inspection_id"]
            != inspection_id
        ):
            raise ValueError(
                "The checklist item does not belong "
                "to this SOP inspection."
            )

        if inspection_item["result"] != "Fail":
            raise ValueError(
                "A Work Order can only be created "
                "from a failed checklist item."
            )

        return WorkOrderService.create_from_sop_failure(
            inspection,
            inspection_item,
            user=user
        )
from app.models.work_order_parts_model import WorkOrderPartsModel

class WorkOrderPartsService:

    @staticmethod
    def add(part):
        WorkOrderPartsModel.add(part)

    @staticmethod
    def get_by_work_order(work_order_id):
        return WorkOrderPartsModel.get_by_work_order(work_order_id)

    @staticmethod
    def delete(work_order_part_id):
        WorkOrderPartsModel.delete(work_order_part_id)

    @staticmethod
    def delete_by_work_order(work_order_id):
        WorkOrderPartsModel.delete_by_work_order(work_order_id)


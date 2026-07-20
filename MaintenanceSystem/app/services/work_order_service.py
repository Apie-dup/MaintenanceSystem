from app.models.work_order_model import WorkOrderModel

class WorkOrderService:
    
    @staticmethod
    def get_all():
        return WorkOrderModel.get_all()
    
    @staticmethod
    def get(work_order_id):
        return WorkOrderModel.get_by_id(work_order_id)
    
    @staticmethod
    def add(record):
        WorkOrderModel.insert(record)

    @staticmethod
    def update(record):
        WorkOrderModel.update(record)

    @staticmethod
    def delete(work_order_id):
        WorkOrderModel.delete(work_order_id)

    @staticmethod
    def search(text):
        return WorkOrderModel.search(text)
    
    @staticmethod
    def get_next_work_order_number():
        return WorkOrderModel.get_next_work_order_number()
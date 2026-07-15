from app.models.work_order_model import WorkOrderModel

class WorkOrderService:
    
    @staticmethod
    def get_work_orders():
        return WorkOrderModel.get_all()
    
    @staticmethod
    def get_work_order(work_order_id):
        return WorkOrderModel.get_by_id(work_order_id)
    
    @staticmethod
    def add_work_order(work_order):
        WorkOrderModel.insert(work_order)

    @staticmethod
    def update_work_order(work_order):
        WorkOrderModel.update(work_order)

    @staticmethod
    def delete_work_order(work_order_id):
        WorkOrderModel.delete(work_order_id)

    @staticmethod
    def search_work_order(search_text):
        return WorkOrderModel.search(search_text)
    
    @staticmethod
    def get_next_work_order_number():
        return WorkOrderModel.get_next_work_order_number()
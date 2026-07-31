from app.models.supplier_model import SupplierModel


class SupplierService:

    # ---------------------------------------------------------
    # GET ALL SUPPLIERS
    # ---------------------------------------------------------
    @staticmethod
    def get_all():
        return SupplierModel.get_all()

    # ---------------------------------------------------------
    # GET ACTIVE SUPPLIERS
    # ---------------------------------------------------------
    @staticmethod
    def get_active_suppliers():
        return SupplierModel.get_active_suppliers()

    # ---------------------------------------------------------
    # GET SUPPLIER BY ID
    # ---------------------------------------------------------
    @staticmethod
    def get_by_id(supplier_id):
        return SupplierModel.get_by_id(supplier_id)

    # ---------------------------------------------------------
    # SEARCH SUPPLIERS
    # ---------------------------------------------------------
    @staticmethod
    def search(search_text):
        return SupplierModel.search(search_text)

    # ---------------------------------------------------------
    # NEXT SUPPLIER CODE
    # ---------------------------------------------------------
    @staticmethod
    def get_next_supplier_code():
        return SupplierModel.get_next_supplier_code()

    # ---------------------------------------------------------
    # CREATE DATA
    # ---------------------------------------------------------
    @staticmethod
    def create(data):

        if not data["supplier_name"].strip():
            raise ValueError("Supplier name is required.")

        if SupplierModel.get_by_code(data["supplier_code"]):
            raise ValueError("Supplier code already exists.")

        SupplierModel.insert(data)


    # ---------------------------------------------------------
    # UPDATE SUPPLIER
    # ---------------------------------------------------------
    @staticmethod
    def update(supplier_id, data):

        if not data["supplier_name"].strip():
            raise ValueError("Supplier name is required.")

        SupplierModel.update(
            supplier_id,
            data
        )

    # ---------------------------------------------------------
    # DELETE SUPPLIER
    # ---------------------------------------------------------
    @staticmethod
    def delete(supplier_id):

        SupplierModel.delete(supplier_id)

    @staticmethod
    def delete_supplier(supplier_id):

        SupplierService.delete(supplier_id)
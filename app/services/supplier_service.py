from app.models.supplier_model import SupplierModel


class SupplierService:

    @staticmethod
    def get_all():
        return SupplierModel.get_all()

    @staticmethod
    def get_active_suppliers():
        return SupplierModel.get_active_suppliers()

    @staticmethod
    def get_by_id(supplier_id):
        return SupplierModel.get_by_id(
            supplier_id
        )

    @staticmethod
    def search(search_text):
        return SupplierModel.search(
            search_text
        )

    @staticmethod
    def get_next_supplier_code():
        return SupplierModel.get_next_supplier_code()

    @staticmethod
    def create(data):

        if not data["supplier_name"].strip():
            raise ValueError(
                "Supplier name is required."
            )

        if SupplierModel.code_exists(
            data["supplier_code"]
        ):
            raise ValueError(
                "Supplier code already exists."
            )

        return SupplierModel.insert(data)

    @staticmethod
    def update(supplier_id, data):

        if not data["supplier_name"].strip():
            raise ValueError(
                "Supplier name is required."
            )

        if SupplierModel.code_exists(
            data["supplier_code"],
            exclude_id=supplier_id,
        ):
            raise ValueError(
                "Supplier code already exists."
            )

        SupplierModel.update(
            supplier_id,
            data
        )

    @staticmethod
    def delete(supplier_id):
        SupplierModel.delete(
            supplier_id
        )
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
    # ADD SUPPLIER
    # ---------------------------------------------------------
    @staticmethod
    def add_supplier(
        supplier_code,
        supplier_name,
        contact_person,
        phone,
        email,
        address,
        status,
        notes
    ):

        if supplier_name.strip() == "":
            raise ValueError("Supplier name is required.")

        if SupplierModel.get_by_code(supplier_code):
            raise ValueError("Supplier code already exists.")

        SupplierModel.insert(
            (
                supplier_code,
                supplier_name,
                contact_person,
                phone,
                email,
                address,
                status,
                notes
            )
        )

    # ---------------------------------------------------------
    # UPDATE SUPPLIER
    # ---------------------------------------------------------
    @staticmethod
    def update_supplier(
        supplier_id,
        supplier_code,
        supplier_name,
        contact_person,
        phone,
        email,
        address,
        status,
        notes
    ):

        if supplier_name.strip() == "":
            raise ValueError("Supplier name is required.")

        SupplierModel.update(
            (
                supplier_code,
                supplier_name,
                contact_person,
                phone,
                email,
                address,
                status,
                notes,
                supplier_id
            )
        )

    # ---------------------------------------------------------
    # DELETE SUPPLIER
    # ---------------------------------------------------------
    @staticmethod
    def delete_supplier(supplier_id):
        SupplierModel.delete(supplier_id)

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QHeaderView,
    QMessageBox,
    QTableWidgetItem,
)

from app.services.asset_service import AssetService
from app.services.asset_document_service import AssetDocumentService
from app.ui.generated.ui_asset_documents_dialog import (
    Ui_AssetDocumentsDialog,
)
from app.dialogs.asset_document_dialog import AssetDocumentDialog
from app.core.permissions import Permissions


class AssetDocumentsDialog(QDialog):

    DOCUMENT_TYPES = [
        "Manual",
        "Technical Document",
        "Maintenance Document",
        "Certificate",
        "Warranty",
        "Drawing",
        "Photograph",
        "Invoice",
        "Other",
    ]

    def __init__(self, asset_id, user=None, parent=None):
        super().__init__(parent)

        self.asset_id = asset_id
        self.user = user or {}
        self.role = self.user.get("role", "")

        if not Permissions.has_permission(
            self.role,
            "asset_documents"
        ):
            raise PermissionError(
                "You do not have permission to view asset documents."
            )

        self.ui = Ui_AssetDocumentsDialog()
        self.ui.setupUi(self)

        self.setup_asset()
        self.setup_table()
        self.setup_filters()
        self.connect_signals()
        self.apply_permissions()
        self.load_documents()

    # ---------------------------------------------------------
    # Asset information
    # ---------------------------------------------------------

    def setup_asset(self):
        asset = AssetService.get_by_id(self.asset_id)

        if asset is None:
            raise ValueError("Asset not found.")

        self.ui.lblAsset.setText(
            f"Asset: {asset['asset_number']} - "
            f"{asset['asset_name']}"
        )

    # ---------------------------------------------------------
    # Configure document table
    # ---------------------------------------------------------

    def setup_table(self):
        table = self.ui.tblDocuments

        table.setColumnCount(5)
        table.setHorizontalHeaderLabels([
            "Document Name",
            "Type",
            "Filename",
            "Uploaded",
            "Expiry Date",
        ])

        table.setSelectionBehavior(
            table.SelectionBehavior.SelectRows
        )
        table.setSelectionMode(
            table.SelectionMode.SingleSelection
        )
        table.setEditTriggers(
            table.EditTrigger.NoEditTriggers
        )

        table.verticalHeader().setVisible(False)

        header = table.horizontalHeader()

        header.setSectionResizeMode(
            0, QHeaderView.ResizeMode.Stretch
        )

        header.setSectionResizeMode(
            1, QHeaderView.ResizeMode.Interactive
        )

        header.setSectionResizeMode(
            2, QHeaderView.ResizeMode.Stretch
        )

        header.setSectionResizeMode(
            3, QHeaderView.ResizeMode.Interactive
        )

        header.setSectionResizeMode(
            4, QHeaderView.ResizeMode.Interactive
        )

        table.setColumnWidth(1, 160)
        table.setColumnWidth(3, 150)
        table.setColumnWidth(4, 120)

        header.setMinimumSectionSize(80)

    # ---------------------------------------------------------
    # Document type filter
    # ---------------------------------------------------------

    def setup_filters(self):
        self.ui.cmbDocumentType.clear()
        self.ui.cmbDocumentType.addItem("All Types")

        self.ui.cmbDocumentType.addItems(
            self.DOCUMENT_TYPES
        )

        self.ui.cmbDocumentType.setCurrentIndex(0)

    # ---------------------------------------------------------
    # Connect signals
    # ---------------------------------------------------------

    def connect_signals(self):
        self.ui.txtSearch.textChanged.connect(
            self.load_documents
        )

        self.ui.cmbDocumentType.currentIndexChanged.connect(
            self.load_documents
        )

        self.ui.btnRefresh.clicked.connect(
            self.refresh
        )

        self.ui.btnOpen.clicked.connect(
            self.open_selected_document
        )

        self.ui.btnClose.clicked.connect(
            self.reject
        )

        self.ui.tblDocuments.itemDoubleClicked.connect(
            self.open_selected_document
        )

        self.ui.btnAdd.clicked.connect(
            self.add_document
        )

        self.ui.btnEdit.clicked.connect(
            self.edit_document
        )

        self.ui.btnDelete.clicked.connect(
            self.delete_document
        )
    # ---------------------------------------------------------
    # Load and filter documents
    # ---------------------------------------------------------

    def load_documents(self, *_):
        search_text = self.ui.txtSearch.text().strip()

        document_type = (
            self.ui.cmbDocumentType.currentText()
        )

        if search_text:
            documents = AssetDocumentService.search(
                self.asset_id,
                search_text,
                user=self.user,
            )
        else:
            documents = AssetDocumentService.get_by_asset(
                self.asset_id,
                user=self.user,
            )

        if document_type != "All Types":
            documents = [
                document
                for document in documents
                if document["document_type"] == document_type
            ]

        table = self.ui.tblDocuments
        table.setRowCount(0)

        for document in documents:
            row = table.rowCount()
            table.insertRow(row)

            values = [
                document["document_name"],
                document["document_type"],
                document["file_name"],
                document["upload_date"],
                document["expiry_date"] or "",
            ]

            for column, value in enumerate(values):
                item = QTableWidgetItem(
                    str(value if value is not None else "")
                )

                if column == 0:
                    item.setData(
                        Qt.ItemDataRole.UserRole,
                        document["id"]
                    )

                table.setItem(row, column, item)

    # ---------------------------------------------------------
    # Selected document
    # ---------------------------------------------------------

    def selected_document_id(self):
        row = self.ui.tblDocuments.currentRow()

        if row < 0:
            return None

        item = self.ui.tblDocuments.item(row, 0)

        if item is None:
            return None

        return item.data(Qt.ItemDataRole.UserRole)

    # ---------------------------------------------------------
    # Open document
    # ---------------------------------------------------------

    def open_selected_document(self, *_):
        document_id = self.selected_document_id()

        if document_id is None:
            QMessageBox.warning(
                self,
                "Asset Documentation",
                "Please select a document."
            )
            return

        try:
            AssetDocumentService.open_document(
                document_id,
                asset_id=self.asset_id,
                user=self.user,
            )

        except Exception as error:
            QMessageBox.critical(
                self,
                "Open Document",
                str(error)
            )

        if not self.require_permission(
            "asset_documents"
        ):
            return

    # ---------------------------------------------------------
    # Refresh
    # ---------------------------------------------------------

    def refresh(self):
        self.load_documents()

    # ---------------------------------------------------------
    # Check document permission
    # ---------------------------------------------------------

    def require_permission(self, permission):

        if Permissions.has_permission(
            self.role,
            permission
        ):
            return True

        QMessageBox.warning(
            self,
            "Asset Documentation",
            "You do not have permission to perform this action."
        )

        return False

    # ---------------------------------------------------------
    # Add document
    # ---------------------------------------------------------

    def add_document(self):
        dialog = AssetDocumentDialog(
            asset_id=self.asset_id,
            user=self.user,
            parent=self,
        )

        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_documents()

        if not self.require_permission(
            "asset_documents.create"
        ):
            return

    # ---------------------------------------------------------
    # Edit document
    # ---------------------------------------------------------

    def edit_document(self):
        document_id = self.selected_document_id()

        if document_id is None:
            QMessageBox.warning(
                self,
                "Asset Documentation",
                "Please select a document to edit."
            )
            return

        try:
            dialog = AssetDocumentDialog(
                asset_id=self.asset_id,
                document_id=document_id,
                parent=self,
                user=self.user,
            )

            if dialog.exec() == QDialog.DialogCode.Accepted:
                self.load_documents()

        except Exception as error:
            QMessageBox.critical(
                self,
                "Edit Document",
                str(error)
            )

        if not self.require_permission(
            "asset_documents.edit"
        ):
            return

    # ---------------------------------------------------------
    # Delete document
    # ---------------------------------------------------------

    def delete_document(self):
        document_id = self.selected_document_id()

        if document_id is None:
            QMessageBox.warning(
                self,
                "Asset Documentation",
                "Please select a document to delete."
            )
            return

        document = AssetDocumentService.get_by_id(
            document_id,
            asset_id=self.asset_id,
            user=self.user,
        )

        if document is None:
            QMessageBox.warning(
                self,
                "Asset Documentation",
                "Document not found."
            )
            self.load_documents()
            return

        if document["asset_id"] != self.asset_id:
            QMessageBox.warning(
                self,
                "Asset Documentation",
                "Document does not belong to this asset."
            )
            return

        reply = QMessageBox.question(
            self,
            "Delete Document",
            (
                f"Delete document '{document['document_name']}'?\n\n"
                "This will remove the document record and its "
                "stored file."
            ),
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        try:
            AssetDocumentService.delete_document(
                document_id,
                asset_id=self.asset_id,
                user=self.user,
            )

            self.load_documents()

        except Exception as error:
            QMessageBox.critical(
                self,
                "Delete Document",
                str(error)
            )

        if not self.require_permission(
            "asset_documents.delete"
        ):
            return

    def apply_permissions(self):

        can_create = Permissions.has_permission(
            self.role,
            "asset_documents.create"
        )

        can_edit = Permissions.has_permission(
            self.role,
            "asset_documents.edit"
        )

        can_delete = Permissions.has_permission(
            self.role,
            "asset_documents.delete"
        )

        self.ui.btnAdd.setVisible(can_create)
        self.ui.btnEdit.setVisible(can_edit)
        self.ui.btnDelete.setVisible(can_delete)

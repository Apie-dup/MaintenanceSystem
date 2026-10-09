
from pathlib import Path

from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QDialog,
    QFileDialog,
    QMessageBox,
)

from app.services.asset_service import AssetService
from app.services.asset_document_service import AssetDocumentService
from app.ui.generated.ui_asset_document_dialog import (
    Ui_AssetDocumentDialog,
)
from app.core.permissions import Permissions


class AssetDocumentDialog(QDialog):

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

    def __init__(
            self,
            asset_id,
            document_id=None,
            parent=None,
            user=None,
        ):

        super().__init__(parent)

        self.user = user or {}
        self.role = self.user.get("role")

        self.asset_id = asset_id
        self.document_id = document_id
        self.selected_file = None

        self.ui = Ui_AssetDocumentDialog()
        self.ui.setupUi(self)

        self.setup_asset()
        self.setup_fields()
        self.connect_signals()

        if self.document_id is not None:
            self.load_document()

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
    # Configure fields
    # ---------------------------------------------------------

    def setup_fields(self):
        self.ui.cmbDocumentType.clear()
        self.ui.cmbDocumentType.addItems(
            self.DOCUMENT_TYPES
        )

        self.ui.txtFilePath.setReadOnly(True)

        self.ui.chkExpiryDate.setChecked(False)

        self.ui.dateExpiry.setDate(
            QDate.currentDate()
        )

        self.ui.dateExpiry.setEnabled(False)
        self.ui.dateExpiry.setCalendarPopup(True)

        if self.document_id is None:
            self.setWindowTitle("Add Asset Document")
            self.ui.lblTitle.setText("Add Asset Document")
        else:
            self.setWindowTitle("Edit Asset Document")
            self.ui.lblTitle.setText("Edit Asset Document")

            self.ui.btnBrowse.setEnabled(False)

    # ---------------------------------------------------------
    # Connect signals
    # ---------------------------------------------------------

    def connect_signals(self):
        self.ui.btnBrowse.clicked.connect(
            self.browse_file
        )

        self.ui.btnSave.clicked.connect(
            self.save_document
        )

        self.ui.btnCancel.clicked.connect(
            self.reject
        )

        self.ui.chkExpiryDate.toggled.connect(
            self.ui.dateExpiry.setEnabled
        )

    # ---------------------------------------------------------
    # Browse for document
    # ---------------------------------------------------------

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Asset Document",
            "",
            (
                "Documents (*.pdf *.doc *.docx *.xls *.xlsx "
                "*.jpg *.jpeg *.png *.txt *.csv);;"
                "All Files (*)"
            )
        )

        if not file_path:
            return

        self.selected_file = file_path

        self.ui.txtFilePath.setText(
            str(Path(file_path).name)
        )

        if not self.ui.txtDocumentName.text().strip():
            self.ui.txtDocumentName.setText(
                Path(file_path).stem
            )

    # ---------------------------------------------------------
    # Load existing document
    # ---------------------------------------------------------

    def load_document(self):
        document = AssetDocumentService.get_by_id(
            self.document_id,
            asset_id=self.asset_id,
            user=self.user,
        )

        if document is None:
            raise ValueError("Document not found.")

        if document["asset_id"] != self.asset_id:
            raise ValueError(
                "Document does not belong to this asset."
            )

        self.ui.txtDocumentName.setText(
            document["document_name"]
        )

        self.ui.cmbDocumentType.setCurrentText(
            document["document_type"]
        )

        self.ui.txtFilePath.setText(
            document["file_name"]
        )

        self.ui.txtDescription.setPlainText(
            document["description"] or ""
        )

        expiry_date = document["expiry_date"]

        if expiry_date:
            date = QDate.fromString(
                expiry_date,
                "yyyy-MM-dd"
            )

            if date.isValid():
                self.ui.dateExpiry.setDate(date)
                self.ui.chkExpiryDate.setChecked(True)

    # ---------------------------------------------------------
    # Save document
    # ---------------------------------------------------------

    def save_document(self):

        permission = (
            "asset_documents.create"
            if self.document_id is None
            else "asset_documents.edit"
        )

        if not Permissions.has_permission(
            self.role,
            permission,
        ):
            QMessageBox.warning(
                self,
                "Asset Documentation",
                "You do not have permission to save this document.",
            )
            return

        document_name = (
            self.ui.txtDocumentName.text().strip()
        )

        document_type = (
            self.ui.cmbDocumentType.currentText().strip()
        )

        description = (
            self.ui.txtDescription.toPlainText().strip()
        )

        expiry_date = None

        if self.ui.chkExpiryDate.isChecked():
            expiry_date = (
                self.ui.dateExpiry.date().toString(
                    "yyyy-MM-dd"
                )
            )

        data = {
            "document_name": document_name,
            "document_type": document_type,
            "description": description,
            "expiry_date": expiry_date,
        }

        if not document_name:
            QMessageBox.warning(
                self,
                "Validation",
                "Document Name is required."
            )
            return

        if not document_type:
            QMessageBox.warning(
                self,
                "Validation",
                "Document Type is required."
            )
            return

        if (
            self.document_id is None
            and not self.selected_file
        ):
            QMessageBox.warning(
                self,
                "Validation",
                "Please select a document file."
            )
            return

        try:
            if self.document_id is None:
                AssetDocumentService.add_document(
                    asset_id=self.asset_id,
                    source_file=self.selected_file,
                    data=data,
                    user=self.user,
                )
            else:
                updated = AssetDocumentService.update_document(
                    self.document_id,
                    data,
                    asset_id=self.asset_id,
                    user=self.user,
                )

                if not updated:
                    raise ValueError(
                        "Document could not be updated."
                    )

        except Exception as error:
            QMessageBox.critical(
                self,
                "Asset Documentation",
                str(error)
            )
            return

        self.accept()

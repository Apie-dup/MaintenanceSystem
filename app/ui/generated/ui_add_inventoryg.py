# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_inventory.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class Ui_AddInventoryDialog(object):
    def setupUi(self, AddInventoryDialog):
        if not AddInventoryDialog.objectName():
            AddInventoryDialog.setObjectName(u"AddInventoryDialog")
        AddInventoryDialog.resize(900, 676)
        AddInventoryDialog.setMinimumSize(QSize(900, 0))
        AddInventoryDialog.setMaximumSize(QSize(16777215, 676))
        self.mainLayout = QVBoxLayout(AddInventoryDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.groupPartInformation = QGroupBox(AddInventoryDialog)
        self.groupPartInformation.setObjectName(u"groupPartInformation")
        self.groupPartInformation.setFlat(True)
        self.formPartInfo = QFormLayout(self.groupPartInformation)
        self.formPartInfo.setObjectName(u"formPartInfo")
        self.lblPartNumber = QLabel(self.groupPartInformation)
        self.lblPartNumber.setObjectName(u"lblPartNumber")

        self.formPartInfo.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblPartNumber)

        self.txtPartNumber = QLineEdit(self.groupPartInformation)
        self.txtPartNumber.setObjectName(u"txtPartNumber")
        self.txtPartNumber.setReadOnly(True)

        self.formPartInfo.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtPartNumber)

        self.lblPartName = QLabel(self.groupPartInformation)
        self.lblPartName.setObjectName(u"lblPartName")

        self.formPartInfo.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblPartName)

        self.txtPartName = QLineEdit(self.groupPartInformation)
        self.txtPartName.setObjectName(u"txtPartName")

        self.formPartInfo.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtPartName)

        self.lblDescription = QLabel(self.groupPartInformation)
        self.lblDescription.setObjectName(u"lblDescription")

        self.formPartInfo.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblDescription)

        self.txtDescription = QLineEdit(self.groupPartInformation)
        self.txtDescription.setObjectName(u"txtDescription")

        self.formPartInfo.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtDescription)

        self.lblCategory = QLabel(self.groupPartInformation)
        self.lblCategory.setObjectName(u"lblCategory")

        self.formPartInfo.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblCategory)

        self.cmbCategory = QComboBox(self.groupPartInformation)
        self.cmbCategory.setObjectName(u"cmbCategory")

        self.formPartInfo.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbCategory)

        self.lblSupplier = QLabel(self.groupPartInformation)
        self.lblSupplier.setObjectName(u"lblSupplier")

        self.formPartInfo.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblSupplier)

        self.cmbSupplier = QComboBox(self.groupPartInformation)
        self.cmbSupplier.setObjectName(u"cmbSupplier")

        self.formPartInfo.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbSupplier)

        self.lblUnit = QLabel(self.groupPartInformation)
        self.lblUnit.setObjectName(u"lblUnit")

        self.formPartInfo.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblUnit)

        self.cmbUnit = QComboBox(self.groupPartInformation)
        self.cmbUnit.setObjectName(u"cmbUnit")

        self.formPartInfo.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cmbUnit)


        self.mainLayout.addWidget(self.groupPartInformation)

        self.groupStockInformation = QGroupBox(AddInventoryDialog)
        self.groupStockInformation.setObjectName(u"groupStockInformation")
        self.groupStockInformation.setFlat(True)
        self.formStockInfo = QFormLayout(self.groupStockInformation)
        self.formStockInfo.setObjectName(u"formStockInfo")
        self.lblQuantity = QLabel(self.groupStockInformation)
        self.lblQuantity.setObjectName(u"lblQuantity")

        self.formStockInfo.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblQuantity)

        self.spnQuantity = QSpinBox(self.groupStockInformation)
        self.spnQuantity.setObjectName(u"spnQuantity")
        self.spnQuantity.setMaximum(999999)

        self.formStockInfo.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spnQuantity)

        self.lblMinQty = QLabel(self.groupStockInformation)
        self.lblMinQty.setObjectName(u"lblMinQty")

        self.formStockInfo.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblMinQty)

        self.spnMinimumQuantity = QSpinBox(self.groupStockInformation)
        self.spnMinimumQuantity.setObjectName(u"spnMinimumQuantity")
        self.spnMinimumQuantity.setMaximum(999999)

        self.formStockInfo.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spnMinimumQuantity)

        self.lblReorderQty = QLabel(self.groupStockInformation)
        self.lblReorderQty.setObjectName(u"lblReorderQty")

        self.formStockInfo.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblReorderQty)

        self.spnReorderQuantity = QSpinBox(self.groupStockInformation)
        self.spnReorderQuantity.setObjectName(u"spnReorderQuantity")
        self.spnReorderQuantity.setMaximum(999999)

        self.formStockInfo.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spnReorderQuantity)

        self.lblUnitCost = QLabel(self.groupStockInformation)
        self.lblUnitCost.setObjectName(u"lblUnitCost")

        self.formStockInfo.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblUnitCost)

        self.dsbUnitCost = QDoubleSpinBox(self.groupStockInformation)
        self.dsbUnitCost.setObjectName(u"dsbUnitCost")
        self.dsbUnitCost.setDecimals(2)
        self.dsbUnitCost.setMaximum(999999.989999999990687)

        self.formStockInfo.setWidget(3, QFormLayout.ItemRole.FieldRole, self.dsbUnitCost)

        self.lblLocation = QLabel(self.groupStockInformation)
        self.lblLocation.setObjectName(u"lblLocation")

        self.formStockInfo.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblLocation)

        self.lblBarcode = QLabel(self.groupStockInformation)
        self.lblBarcode.setObjectName(u"lblBarcode")

        self.formStockInfo.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lblBarcode)

        self.txtBarcode = QLineEdit(self.groupStockInformation)
        self.txtBarcode.setObjectName(u"txtBarcode")

        self.formStockInfo.setWidget(6, QFormLayout.ItemRole.FieldRole, self.txtBarcode)

        self.cmbLocation = QComboBox(self.groupStockInformation)
        self.cmbLocation.setObjectName(u"cmbLocation")

        self.formStockInfo.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbLocation)


        self.mainLayout.addWidget(self.groupStockInformation)

        self.groupStatus = QGroupBox(AddInventoryDialog)
        self.groupStatus.setObjectName(u"groupStatus")
        self.groupStatus.setFlat(True)
        self.layoutStatus = QHBoxLayout(self.groupStatus)
        self.layoutStatus.setObjectName(u"layoutStatus")
        self.lblStatus = QLabel(self.groupStatus)
        self.lblStatus.setObjectName(u"lblStatus")

        self.layoutStatus.addWidget(self.lblStatus)

        self.cmbStatus = QComboBox(self.groupStatus)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.layoutStatus.addWidget(self.cmbStatus)


        self.mainLayout.addWidget(self.groupStatus)

        self.groupNotes = QGroupBox(AddInventoryDialog)
        self.groupNotes.setObjectName(u"groupNotes")
        self.groupNotes.setFlat(True)
        self.layoutNotes = QVBoxLayout(self.groupNotes)
        self.layoutNotes.setObjectName(u"layoutNotes")
        self.txtNotes = QTextEdit(self.groupNotes)
        self.txtNotes.setObjectName(u"txtNotes")

        self.layoutNotes.addWidget(self.txtNotes)


        self.mainLayout.addWidget(self.groupNotes)

        self.buttonBox = QDialogButtonBox(AddInventoryDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.mainLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddInventoryDialog)

        QMetaObject.connectSlotsByName(AddInventoryDialog)
    # setupUi

    def retranslateUi(self, AddInventoryDialog):
        AddInventoryDialog.setWindowTitle(QCoreApplication.translate("AddInventoryDialog", u"Add Inventory", None))
        self.groupPartInformation.setTitle(QCoreApplication.translate("AddInventoryDialog", u"Part Information", None))
        self.lblPartNumber.setText(QCoreApplication.translate("AddInventoryDialog", u"Part Number:", None))
        self.lblPartName.setText(QCoreApplication.translate("AddInventoryDialog", u"Part Name:", None))
        self.lblDescription.setText(QCoreApplication.translate("AddInventoryDialog", u"Description:", None))
        self.lblCategory.setText(QCoreApplication.translate("AddInventoryDialog", u"Category:", None))
        self.lblSupplier.setText(QCoreApplication.translate("AddInventoryDialog", u"Supplier:", None))
        self.lblUnit.setText(QCoreApplication.translate("AddInventoryDialog", u"Unit:", None))
        self.groupStockInformation.setTitle(QCoreApplication.translate("AddInventoryDialog", u"Stock Information", None))
        self.lblQuantity.setText(QCoreApplication.translate("AddInventoryDialog", u"Quantity:", None))
        self.lblMinQty.setText(QCoreApplication.translate("AddInventoryDialog", u"Minimum Qty:", None))
        self.lblReorderQty.setText(QCoreApplication.translate("AddInventoryDialog", u"Reorder Qty:", None))
        self.lblUnitCost.setText(QCoreApplication.translate("AddInventoryDialog", u"Unit Cost:", None))
        self.lblLocation.setText(QCoreApplication.translate("AddInventoryDialog", u"Location:", None))
        self.lblBarcode.setText(QCoreApplication.translate("AddInventoryDialog", u"Barcode:", None))
        self.groupStatus.setTitle(QCoreApplication.translate("AddInventoryDialog", u"Status", None))
        self.lblStatus.setText(QCoreApplication.translate("AddInventoryDialog", u"Status:", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("AddInventoryDialog", u"Active", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("AddInventoryDialog", u"Inactive", None))

        self.groupNotes.setTitle(QCoreApplication.translate("AddInventoryDialog", u"Notes", None))
    # retranslateUi


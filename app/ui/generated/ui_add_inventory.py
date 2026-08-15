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
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_AddInventoryItemDialog(object):
    def setupUi(self, AddInventoryItemDialog):
        if not AddInventoryItemDialog.objectName():
            AddInventoryItemDialog.setObjectName(u"AddInventoryItemDialog")
        AddInventoryItemDialog.resize(507, 748)
        self.mainLayout = QVBoxLayout(AddInventoryItemDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.groupPartInfo = QGroupBox(AddInventoryItemDialog)
        self.groupPartInfo.setObjectName(u"groupPartInfo")
        self.formPartInfo = QFormLayout(self.groupPartInfo)
        self.formPartInfo.setObjectName(u"formPartInfo")
        self.lblPartNumber = QLabel(self.groupPartInfo)
        self.lblPartNumber.setObjectName(u"lblPartNumber")

        self.formPartInfo.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblPartNumber)

        self.txtPartNumber = QLineEdit(self.groupPartInfo)
        self.txtPartNumber.setObjectName(u"txtPartNumber")

        self.formPartInfo.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtPartNumber)

        self.lblPartName = QLabel(self.groupPartInfo)
        self.lblPartName.setObjectName(u"lblPartName")

        self.formPartInfo.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblPartName)

        self.txtPartName = QLineEdit(self.groupPartInfo)
        self.txtPartName.setObjectName(u"txtPartName")

        self.formPartInfo.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtPartName)

        self.lblDescription = QLabel(self.groupPartInfo)
        self.lblDescription.setObjectName(u"lblDescription")

        self.formPartInfo.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblDescription)

        self.txtDescription = QLineEdit(self.groupPartInfo)
        self.txtDescription.setObjectName(u"txtDescription")

        self.formPartInfo.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtDescription)

        self.lblCategory = QLabel(self.groupPartInfo)
        self.lblCategory.setObjectName(u"lblCategory")

        self.formPartInfo.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblCategory)

        self.cmbCategory = QComboBox(self.groupPartInfo)
        self.cmbCategory.setObjectName(u"cmbCategory")

        self.formPartInfo.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbCategory)

        self.lblSupplier = QLabel(self.groupPartInfo)
        self.lblSupplier.setObjectName(u"lblSupplier")

        self.formPartInfo.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblSupplier)

        self.cmbSupplier = QComboBox(self.groupPartInfo)
        self.cmbSupplier.setObjectName(u"cmbSupplier")

        self.formPartInfo.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbSupplier)

        self.lblUnit = QLabel(self.groupPartInfo)
        self.lblUnit.setObjectName(u"lblUnit")

        self.formPartInfo.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblUnit)

        self.cmbUnit = QComboBox(self.groupPartInfo)
        self.cmbUnit.setObjectName(u"cmbUnit")

        self.formPartInfo.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cmbUnit)


        self.mainLayout.addWidget(self.groupPartInfo)

        self.groupStockInfo = QGroupBox(AddInventoryItemDialog)
        self.groupStockInfo.setObjectName(u"groupStockInfo")
        self.gridStockInfo = QGridLayout(self.groupStockInfo)
        self.gridStockInfo.setObjectName(u"gridStockInfo")
        self.lblQuantity = QLabel(self.groupStockInfo)
        self.lblQuantity.setObjectName(u"lblQuantity")

        self.gridStockInfo.addWidget(self.lblQuantity, 0, 0, 1, 1)

        self.spnQuantity = QSpinBox(self.groupStockInfo)
        self.spnQuantity.setObjectName(u"spnQuantity")
        self.spnQuantity.setMaximum(999999)

        self.gridStockInfo.addWidget(self.spnQuantity, 0, 1, 1, 1)

        self.lblMinQty = QLabel(self.groupStockInfo)
        self.lblMinQty.setObjectName(u"lblMinQty")

        self.gridStockInfo.addWidget(self.lblMinQty, 0, 2, 1, 1)

        self.spnMinimumQuantity = QSpinBox(self.groupStockInfo)
        self.spnMinimumQuantity.setObjectName(u"spnMinimumQuantity")
        self.spnMinimumQuantity.setMaximum(999999)

        self.gridStockInfo.addWidget(self.spnMinimumQuantity, 0, 3, 1, 1)

        self.lblReorderQty = QLabel(self.groupStockInfo)
        self.lblReorderQty.setObjectName(u"lblReorderQty")

        self.gridStockInfo.addWidget(self.lblReorderQty, 1, 0, 1, 1)

        self.spnReorderQuantity = QSpinBox(self.groupStockInfo)
        self.spnReorderQuantity.setObjectName(u"spnReorderQuantity")
        self.spnReorderQuantity.setMaximum(999999)

        self.gridStockInfo.addWidget(self.spnReorderQuantity, 1, 1, 1, 1)

        self.lblUnitCost = QLabel(self.groupStockInfo)
        self.lblUnitCost.setObjectName(u"lblUnitCost")

        self.gridStockInfo.addWidget(self.lblUnitCost, 1, 2, 1, 1)

        self.dsbUnitCost = QDoubleSpinBox(self.groupStockInfo)
        self.dsbUnitCost.setObjectName(u"dsbUnitCost")
        self.dsbUnitCost.setDecimals(2)
        self.dsbUnitCost.setMaximum(999999.989999999990687)

        self.gridStockInfo.addWidget(self.dsbUnitCost, 1, 3, 1, 1)

        self.lblLocation = QLabel(self.groupStockInfo)
        self.lblLocation.setObjectName(u"lblLocation")

        self.gridStockInfo.addWidget(self.lblLocation, 2, 0, 1, 1)

        self.cmbLocation = QComboBox(self.groupStockInfo)
        self.cmbLocation.setObjectName(u"cmbLocation")

        self.gridStockInfo.addWidget(self.cmbLocation, 2, 1, 1, 1)

        self.lblBarcode = QLabel(self.groupStockInfo)
        self.lblBarcode.setObjectName(u"lblBarcode")

        self.gridStockInfo.addWidget(self.lblBarcode, 2, 2, 1, 1)

        self.txtBarcode = QLineEdit(self.groupStockInfo)
        self.txtBarcode.setObjectName(u"txtBarcode")

        self.gridStockInfo.addWidget(self.txtBarcode, 2, 3, 1, 1)


        self.mainLayout.addWidget(self.groupStockInfo)

        self.groupStatus = QGroupBox(AddInventoryItemDialog)
        self.groupStatus.setObjectName(u"groupStatus")
        self.layoutStatus = QHBoxLayout(self.groupStatus)
        self.layoutStatus.setObjectName(u"layoutStatus")
        self.lblStatus = QLabel(self.groupStatus)
        self.lblStatus.setObjectName(u"lblStatus")

        self.layoutStatus.addWidget(self.lblStatus)

        self.cmbStatus = QComboBox(self.groupStatus)
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.layoutStatus.addWidget(self.cmbStatus)


        self.mainLayout.addWidget(self.groupStatus)

        self.groupNotes = QGroupBox(AddInventoryItemDialog)
        self.groupNotes.setObjectName(u"groupNotes")
        self.layoutNotes = QVBoxLayout(self.groupNotes)
        self.layoutNotes.setObjectName(u"layoutNotes")
        self.teNotes = QPlainTextEdit(self.groupNotes)
        self.teNotes.setObjectName(u"teNotes")

        self.layoutNotes.addWidget(self.teNotes)


        self.mainLayout.addWidget(self.groupNotes)

        self.layoutButtons = QHBoxLayout()
        self.layoutButtons.setObjectName(u"layoutButtons")
        self.spacerButtons = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutButtons.addItem(self.spacerButtons)

        self.buttonBox = QDialogButtonBox(AddInventoryItemDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.layoutButtons.addWidget(self.buttonBox)


        self.mainLayout.addLayout(self.layoutButtons)


        self.retranslateUi(AddInventoryItemDialog)

        QMetaObject.connectSlotsByName(AddInventoryItemDialog)
    # setupUi

    def retranslateUi(self, AddInventoryItemDialog):
        AddInventoryItemDialog.setWindowTitle(QCoreApplication.translate("AddInventoryItemDialog", u"Add Inventory Item", None))
        self.groupPartInfo.setTitle(QCoreApplication.translate("AddInventoryItemDialog", u"Part Information", None))
        self.lblPartNumber.setText(QCoreApplication.translate("AddInventoryItemDialog", u"Part Number:", None))
        self.lblPartName.setText(QCoreApplication.translate("AddInventoryItemDialog", u"Part Name:", None))
        self.lblDescription.setText(QCoreApplication.translate("AddInventoryItemDialog", u"Description:", None))
        self.lblCategory.setText(QCoreApplication.translate("AddInventoryItemDialog", u"Category:", None))
        self.lblSupplier.setText(QCoreApplication.translate("AddInventoryItemDialog", u"Supplier:", None))
        self.lblUnit.setText(QCoreApplication.translate("AddInventoryItemDialog", u"Unit:", None))
        self.groupStockInfo.setTitle(QCoreApplication.translate("AddInventoryItemDialog", u"Stock Information", None))
        self.lblQuantity.setText(QCoreApplication.translate("AddInventoryItemDialog", u"Quantity: On Hand:", None))
        self.lblMinQty.setText(QCoreApplication.translate("AddInventoryItemDialog", u"Minimum Quantity:", None))
        self.lblReorderQty.setText(QCoreApplication.translate("AddInventoryItemDialog", u"Reorder Quantity:", None))
        self.lblUnitCost.setText(QCoreApplication.translate("AddInventoryItemDialog", u"Unit Cost:", None))
        self.lblLocation.setText(QCoreApplication.translate("AddInventoryItemDialog", u"Location:", None))
        self.lblBarcode.setText(QCoreApplication.translate("AddInventoryItemDialog", u"Barcode:", None))
        self.groupStatus.setTitle(QCoreApplication.translate("AddInventoryItemDialog", u"Status", None))
        self.lblStatus.setText(QCoreApplication.translate("AddInventoryItemDialog", u"Status:", None))
        self.groupNotes.setTitle(QCoreApplication.translate("AddInventoryItemDialog", u"Notes", None))
    # retranslateUi


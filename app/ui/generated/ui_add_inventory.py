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
    QDialogButtonBox, QDoubleSpinBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_AddInventoryDialog(object):
    def setupUi(self, AddInventoryDialog):
        if not AddInventoryDialog.objectName():
            AddInventoryDialog.setObjectName(u"AddInventoryDialog")
        AddInventoryDialog.resize(483, 580)
        self.verticalLayout = QVBoxLayout(AddInventoryDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblPartNumber = QLabel(AddInventoryDialog)
        self.lblPartNumber.setObjectName(u"lblPartNumber")

        self.horizontalLayout_2.addWidget(self.lblPartNumber)

        self.txtPartNumber = QLineEdit(AddInventoryDialog)
        self.txtPartNumber.setObjectName(u"txtPartNumber")

        self.horizontalLayout_2.addWidget(self.txtPartNumber)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblPartName = QLabel(AddInventoryDialog)
        self.lblPartName.setObjectName(u"lblPartName")

        self.horizontalLayout_3.addWidget(self.lblPartName)

        self.txtPartName = QLineEdit(AddInventoryDialog)
        self.txtPartName.setObjectName(u"txtPartName")

        self.horizontalLayout_3.addWidget(self.txtPartName)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblCategory = QLabel(AddInventoryDialog)
        self.lblCategory.setObjectName(u"lblCategory")

        self.horizontalLayout_4.addWidget(self.lblCategory)

        self.cmbCategory = QComboBox(AddInventoryDialog)
        self.cmbCategory.setObjectName(u"cmbCategory")

        self.horizontalLayout_4.addWidget(self.cmbCategory)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSupplier_2 = QLabel(AddInventoryDialog)
        self.lblSupplier_2.setObjectName(u"lblSupplier_2")

        self.horizontalLayout.addWidget(self.lblSupplier_2)

        self.cmbSupplier_2 = QComboBox(AddInventoryDialog)
        self.cmbSupplier_2.setObjectName(u"cmbSupplier_2")

        self.horizontalLayout.addWidget(self.cmbSupplier_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblUnit = QLabel(AddInventoryDialog)
        self.lblUnit.setObjectName(u"lblUnit")

        self.horizontalLayout_6.addWidget(self.lblUnit)

        self.cmbUnit = QComboBox(AddInventoryDialog)
        self.cmbUnit.setObjectName(u"cmbUnit")

        self.horizontalLayout_6.addWidget(self.cmbUnit)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lblQuantity = QLabel(AddInventoryDialog)
        self.lblQuantity.setObjectName(u"lblQuantity")

        self.horizontalLayout_9.addWidget(self.lblQuantity)

        self.spnQuantity = QSpinBox(AddInventoryDialog)
        self.spnQuantity.setObjectName(u"spnQuantity")

        self.horizontalLayout_9.addWidget(self.spnQuantity)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lblMinimumQuantity = QLabel(AddInventoryDialog)
        self.lblMinimumQuantity.setObjectName(u"lblMinimumQuantity")

        self.horizontalLayout_10.addWidget(self.lblMinimumQuantity)

        self.spnMinimumQuantity = QSpinBox(AddInventoryDialog)
        self.spnMinimumQuantity.setObjectName(u"spnMinimumQuantity")

        self.horizontalLayout_10.addWidget(self.spnMinimumQuantity)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lblReorderQuantity = QLabel(AddInventoryDialog)
        self.lblReorderQuantity.setObjectName(u"lblReorderQuantity")

        self.horizontalLayout_8.addWidget(self.lblReorderQuantity)

        self.spnReorderQuantity = QSpinBox(AddInventoryDialog)
        self.spnReorderQuantity.setObjectName(u"spnReorderQuantity")

        self.horizontalLayout_8.addWidget(self.spnReorderQuantity)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lblUnitCost = QLabel(AddInventoryDialog)
        self.lblUnitCost.setObjectName(u"lblUnitCost")

        self.horizontalLayout_7.addWidget(self.lblUnitCost)

        self.dsbUnitCost = QDoubleSpinBox(AddInventoryDialog)
        self.dsbUnitCost.setObjectName(u"dsbUnitCost")

        self.horizontalLayout_7.addWidget(self.dsbUnitCost)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblLocation = QLabel(AddInventoryDialog)
        self.lblLocation.setObjectName(u"lblLocation")

        self.horizontalLayout_5.addWidget(self.lblLocation)

        self.cmbLocation = QComboBox(AddInventoryDialog)
        self.cmbLocation.setObjectName(u"cmbLocation")

        self.horizontalLayout_5.addWidget(self.cmbLocation)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lblBarcode = QLabel(AddInventoryDialog)
        self.lblBarcode.setObjectName(u"lblBarcode")

        self.horizontalLayout_11.addWidget(self.lblBarcode)

        self.txtBarcode = QLineEdit(AddInventoryDialog)
        self.txtBarcode.setObjectName(u"txtBarcode")

        self.horizontalLayout_11.addWidget(self.txtBarcode)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lblStatus = QLabel(AddInventoryDialog)
        self.lblStatus.setObjectName(u"lblStatus")

        self.horizontalLayout_12.addWidget(self.lblStatus)

        self.cmbStatus = QComboBox(AddInventoryDialog)
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.horizontalLayout_12.addWidget(self.cmbStatus)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lblNotes = QLabel(AddInventoryDialog)
        self.lblNotes.setObjectName(u"lblNotes")

        self.horizontalLayout_13.addWidget(self.lblNotes)

        self.textEdit = QTextEdit(AddInventoryDialog)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_13.addWidget(self.textEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.buttonBox = QDialogButtonBox(AddInventoryDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddInventoryDialog)
        self.buttonBox.accepted.connect(AddInventoryDialog.accept)
        self.buttonBox.rejected.connect(AddInventoryDialog.reject)

        QMetaObject.connectSlotsByName(AddInventoryDialog)
    # setupUi

    def retranslateUi(self, AddInventoryDialog):
        AddInventoryDialog.setWindowTitle(QCoreApplication.translate("AddInventoryDialog", u"Add Inventory Dialog", None))
        self.lblPartNumber.setText(QCoreApplication.translate("AddInventoryDialog", u"Part Number", None))
        self.lblPartName.setText(QCoreApplication.translate("AddInventoryDialog", u"Part Name", None))
        self.lblCategory.setText(QCoreApplication.translate("AddInventoryDialog", u"Category", None))
        self.lblSupplier_2.setText(QCoreApplication.translate("AddInventoryDialog", u"Supplier", None))
        self.lblUnit.setText(QCoreApplication.translate("AddInventoryDialog", u"Unit", None))
        self.lblQuantity.setText(QCoreApplication.translate("AddInventoryDialog", u"Quantity", None))
        self.lblMinimumQuantity.setText(QCoreApplication.translate("AddInventoryDialog", u"Minimum Quantity", None))
        self.lblReorderQuantity.setText(QCoreApplication.translate("AddInventoryDialog", u"Reorder Quantity", None))
        self.lblUnitCost.setText(QCoreApplication.translate("AddInventoryDialog", u"Unit Cost", None))
        self.lblLocation.setText(QCoreApplication.translate("AddInventoryDialog", u"Location", None))
        self.lblBarcode.setText(QCoreApplication.translate("AddInventoryDialog", u"Barcode", None))
        self.lblStatus.setText(QCoreApplication.translate("AddInventoryDialog", u"Status", None))
        self.lblNotes.setText(QCoreApplication.translate("AddInventoryDialog", u"Notes", None))
    # retranslateUi


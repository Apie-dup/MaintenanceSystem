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
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QLineEdit,
    QSizePolicy, QSpinBox, QTextEdit, QWidget)

class Ui_AddInventoryDialog(object):
    def setupUi(self, AddInventoryDialog):
        if not AddInventoryDialog.objectName():
            AddInventoryDialog.setObjectName(u"AddInventoryDialog")
        AddInventoryDialog.resize(819, 700)
        self.formLayout = QFormLayout(AddInventoryDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.txtPartNumber = QLineEdit(AddInventoryDialog)
        self.txtPartNumber.setObjectName(u"txtPartNumber")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.txtPartNumber)

        self.txtPartName = QLineEdit(AddInventoryDialog)
        self.txtPartName.setObjectName(u"txtPartName")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.txtPartName)

        self.cmdCategory = QComboBox(AddInventoryDialog)
        self.cmdCategory.setObjectName(u"cmdCategory")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.cmdCategory)

        self.cmbSuplier = QComboBox(AddInventoryDialog)
        self.cmbSuplier.setObjectName(u"cmbSuplier")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.cmbSuplier)

        self.cmbUnit = QComboBox(AddInventoryDialog)
        self.cmbUnit.setObjectName(u"cmbUnit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.cmbUnit)

        self.spnQuantity = QSpinBox(AddInventoryDialog)
        self.spnQuantity.setObjectName(u"spnQuantity")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.spnQuantity)

        self.spnMinimum = QSpinBox(AddInventoryDialog)
        self.spnMinimum.setObjectName(u"spnMinimum")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.spnMinimum)

        self.spnReorder = QSpinBox(AddInventoryDialog)
        self.spnReorder.setObjectName(u"spnReorder")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.spnReorder)

        self.dsbUnitCost = QDoubleSpinBox(AddInventoryDialog)
        self.dsbUnitCost.setObjectName(u"dsbUnitCost")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.dsbUnitCost)

        self.txtLocation = QLineEdit(AddInventoryDialog)
        self.txtLocation.setObjectName(u"txtLocation")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.txtLocation)

        self.txtBarcode = QLineEdit(AddInventoryDialog)
        self.txtBarcode.setObjectName(u"txtBarcode")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.txtBarcode)

        self.cmbStaus = QComboBox(AddInventoryDialog)
        self.cmbStaus.setObjectName(u"cmbStaus")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.LabelRole, self.cmbStaus)

        self.teNotes = QTextEdit(AddInventoryDialog)
        self.teNotes.setObjectName(u"teNotes")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.LabelRole, self.teNotes)

        self.buttonBox = QDialogButtonBox(AddInventoryDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.formLayout.setWidget(13, QFormLayout.ItemRole.FieldRole, self.buttonBox)


        self.retranslateUi(AddInventoryDialog)
        self.buttonBox.accepted.connect(AddInventoryDialog.accept)
        self.buttonBox.rejected.connect(AddInventoryDialog.reject)

        QMetaObject.connectSlotsByName(AddInventoryDialog)
    # setupUi

    def retranslateUi(self, AddInventoryDialog):
        AddInventoryDialog.setWindowTitle(QCoreApplication.translate("AddInventoryDialog", u"Add Inventory Dialog", None))
    # retranslateUi


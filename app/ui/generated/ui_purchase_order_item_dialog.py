# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'purchase_order_item_dialog.ui'
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
    QPlainTextEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_PurchaseOrderItemDialog(object):
    def setupUi(self, PurchaseOrderItemDialog):
        if not PurchaseOrderItemDialog.objectName():
            PurchaseOrderItemDialog.setObjectName(u"PurchaseOrderItemDialog")
        PurchaseOrderItemDialog.resize(440, 447)
        self.verticalLayout = QVBoxLayout(PurchaseOrderItemDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(PurchaseOrderItemDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblInventoryItem = QLabel(PurchaseOrderItemDialog)
        self.lblInventoryItem.setObjectName(u"lblInventoryItem")

        self.horizontalLayout.addWidget(self.lblInventoryItem)

        self.cmbInventory = QComboBox(PurchaseOrderItemDialog)
        self.cmbInventory.setObjectName(u"cmbInventory")

        self.horizontalLayout.addWidget(self.cmbInventory)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblQuantityOrdered = QLabel(PurchaseOrderItemDialog)
        self.lblQuantityOrdered.setObjectName(u"lblQuantityOrdered")

        self.horizontalLayout_2.addWidget(self.lblQuantityOrdered)

        self.dsbQuantityOrdered = QDoubleSpinBox(PurchaseOrderItemDialog)
        self.dsbQuantityOrdered.setObjectName(u"dsbQuantityOrdered")
        self.dsbQuantityOrdered.setMinimum(0.010000000000000)

        self.horizontalLayout_2.addWidget(self.dsbQuantityOrdered)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblUnitCost = QLabel(PurchaseOrderItemDialog)
        self.lblUnitCost.setObjectName(u"lblUnitCost")

        self.horizontalLayout_3.addWidget(self.lblUnitCost)

        self.dsbUnitCost = QDoubleSpinBox(PurchaseOrderItemDialog)
        self.dsbUnitCost.setObjectName(u"dsbUnitCost")
        self.dsbUnitCost.setMaximum(999999999.990000009536743)

        self.horizontalLayout_3.addWidget(self.dsbUnitCost)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblNotes = QLabel(PurchaseOrderItemDialog)
        self.lblNotes.setObjectName(u"lblNotes")

        self.horizontalLayout_4.addWidget(self.lblNotes)

        self.txtNotes = QPlainTextEdit(PurchaseOrderItemDialog)
        self.txtNotes.setObjectName(u"txtNotes")

        self.horizontalLayout_4.addWidget(self.txtNotes)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.buttonBox = QDialogButtonBox(PurchaseOrderItemDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(PurchaseOrderItemDialog)

        QMetaObject.connectSlotsByName(PurchaseOrderItemDialog)
    # setupUi

    def retranslateUi(self, PurchaseOrderItemDialog):
        PurchaseOrderItemDialog.setWindowTitle(QCoreApplication.translate("PurchaseOrderItemDialog", u"Purchase Order Item", None))
        self.lblTitle.setText(QCoreApplication.translate("PurchaseOrderItemDialog", u"Purchase Order Item", None))
        self.lblInventoryItem.setText(QCoreApplication.translate("PurchaseOrderItemDialog", u"Inventory Item:", None))
        self.lblQuantityOrdered.setText(QCoreApplication.translate("PurchaseOrderItemDialog", u"Quantity Ordered:", None))
        self.lblUnitCost.setText(QCoreApplication.translate("PurchaseOrderItemDialog", u"Unit Cost:", None))
        self.dsbUnitCost.setPrefix(QCoreApplication.translate("PurchaseOrderItemDialog", u"N$ ", None))
        self.lblNotes.setText(QCoreApplication.translate("PurchaseOrderItemDialog", u"Notes:", None))
    # retranslateUi


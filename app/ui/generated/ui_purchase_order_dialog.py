# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'purchase_order_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QComboBox,
    QDateEdit, QDialog, QDialogButtonBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_PurchaseOrderDialog(object):
    def setupUi(self, PurchaseOrderDialog):
        if not PurchaseOrderDialog.objectName():
            PurchaseOrderDialog.setObjectName(u"PurchaseOrderDialog")
        PurchaseOrderDialog.resize(751, 675)
        self.verticalLayout_4 = QVBoxLayout(PurchaseOrderDialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupPurchaseOrder = QGroupBox(PurchaseOrderDialog)
        self.groupPurchaseOrder.setObjectName(u"groupPurchaseOrder")
        self.verticalLayout = QVBoxLayout(self.groupPurchaseOrder)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblPONumber = QLabel(self.groupPurchaseOrder)
        self.lblPONumber.setObjectName(u"lblPONumber")

        self.horizontalLayout.addWidget(self.lblPONumber)

        self.txtPurchaseOrderNumber = QLineEdit(self.groupPurchaseOrder)
        self.txtPurchaseOrderNumber.setObjectName(u"txtPurchaseOrderNumber")
        self.txtPurchaseOrderNumber.setReadOnly(True)

        self.horizontalLayout.addWidget(self.txtPurchaseOrderNumber)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblSupplier = QLabel(self.groupPurchaseOrder)
        self.lblSupplier.setObjectName(u"lblSupplier")

        self.horizontalLayout_2.addWidget(self.lblSupplier)

        self.cmbSupplier = QComboBox(self.groupPurchaseOrder)
        self.cmbSupplier.setObjectName(u"cmbSupplier")

        self.horizontalLayout_2.addWidget(self.cmbSupplier)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblOrderDate = QLabel(self.groupPurchaseOrder)
        self.lblOrderDate.setObjectName(u"lblOrderDate")

        self.horizontalLayout_3.addWidget(self.lblOrderDate)

        self.dtOrderDate = QDateEdit(self.groupPurchaseOrder)
        self.dtOrderDate.setObjectName(u"dtOrderDate")

        self.horizontalLayout_3.addWidget(self.dtOrderDate)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblExpectedDate = QLabel(self.groupPurchaseOrder)
        self.lblExpectedDate.setObjectName(u"lblExpectedDate")

        self.horizontalLayout_4.addWidget(self.lblExpectedDate)

        self.dtExpectedDate = QDateEdit(self.groupPurchaseOrder)
        self.dtExpectedDate.setObjectName(u"dtExpectedDate")

        self.horizontalLayout_4.addWidget(self.dtExpectedDate)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblStatus = QLabel(self.groupPurchaseOrder)
        self.lblStatus.setObjectName(u"lblStatus")

        self.horizontalLayout_5.addWidget(self.lblStatus)

        self.txtStatus = QLineEdit(self.groupPurchaseOrder)
        self.txtStatus.setObjectName(u"txtStatus")
        self.txtStatus.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.txtStatus)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblReference = QLabel(self.groupPurchaseOrder)
        self.lblReference.setObjectName(u"lblReference")

        self.horizontalLayout_6.addWidget(self.lblReference)

        self.txtReference = QLineEdit(self.groupPurchaseOrder)
        self.txtReference.setObjectName(u"txtReference")

        self.horizontalLayout_6.addWidget(self.txtReference)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addWidget(self.groupPurchaseOrder)

        self.groupBox_2 = QGroupBox(PurchaseOrderDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tblItems = QTableWidget(self.groupBox_2)
        if (self.tblItems.columnCount() < 7):
            self.tblItems.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblItems.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblItems.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblItems.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblItems.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblItems.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblItems.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblItems.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tblItems.setObjectName(u"tblItems")
        self.tblItems.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblItems.setAlternatingRowColors(True)
        self.tblItems.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblItems.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_2.addWidget(self.tblItems)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btnAddItem = QPushButton(self.groupBox_2)
        self.btnAddItem.setObjectName(u"btnAddItem")

        self.horizontalLayout_7.addWidget(self.btnAddItem)

        self.btnEditItem = QPushButton(self.groupBox_2)
        self.btnEditItem.setObjectName(u"btnEditItem")

        self.horizontalLayout_7.addWidget(self.btnEditItem)

        self.btnDeleteItem = QPushButton(self.groupBox_2)
        self.btnDeleteItem.setObjectName(u"btnDeleteItem")

        self.horizontalLayout_7.addWidget(self.btnDeleteItem)

        self.btnReceiveStock = QPushButton(self.groupBox_2)
        self.btnReceiveStock.setObjectName(u"btnReceiveStock")

        self.horizontalLayout_7.addWidget(self.btnReceiveStock)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.lblTotal = QLabel(self.groupBox_2)
        self.lblTotal.setObjectName(u"lblTotal")

        self.verticalLayout_2.addWidget(self.lblTotal)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupNotes = QGroupBox(PurchaseOrderDialog)
        self.groupNotes.setObjectName(u"groupNotes")
        self.verticalLayout_3 = QVBoxLayout(self.groupNotes)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txtNotes = QPlainTextEdit(self.groupNotes)
        self.txtNotes.setObjectName(u"txtNotes")

        self.verticalLayout_3.addWidget(self.txtNotes)


        self.verticalLayout_4.addWidget(self.groupNotes)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.btnMarkOrdered = QPushButton(PurchaseOrderDialog)
        self.btnMarkOrdered.setObjectName(u"btnMarkOrdered")

        self.horizontalLayout_8.addWidget(self.btnMarkOrdered)

        self.btnCancelOrder = QPushButton(PurchaseOrderDialog)
        self.btnCancelOrder.setObjectName(u"btnCancelOrder")

        self.horizontalLayout_8.addWidget(self.btnCancelOrder)

        self.buttonBox = QDialogButtonBox(PurchaseOrderDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.horizontalLayout_8.addWidget(self.buttonBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)


        self.retranslateUi(PurchaseOrderDialog)

        QMetaObject.connectSlotsByName(PurchaseOrderDialog)
    # setupUi

    def retranslateUi(self, PurchaseOrderDialog):
        PurchaseOrderDialog.setWindowTitle(QCoreApplication.translate("PurchaseOrderDialog", u"Purchase Order", None))
        self.groupPurchaseOrder.setTitle(QCoreApplication.translate("PurchaseOrderDialog", u"Purchase Order", None))
        self.lblPONumber.setText(QCoreApplication.translate("PurchaseOrderDialog", u"PO Number:", None))
        self.lblSupplier.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Suplier:", None))
        self.lblOrderDate.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Order Date:", None))
        self.lblExpectedDate.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Expected Date:", None))
        self.lblStatus.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Status:", None))
        self.txtStatus.setPlaceholderText(QCoreApplication.translate("PurchaseOrderDialog", u"Draft", None))
        self.lblReference.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Reference:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PurchaseOrderDialog", u"Items", None))
        ___qtablewidgetitem = self.tblItems.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Part Number", None))
        ___qtablewidgetitem1 = self.tblItems.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Part Name", None))
        ___qtablewidgetitem2 = self.tblItems.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Unit", None))
        ___qtablewidgetitem3 = self.tblItems.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Qty Ordered", None))
        ___qtablewidgetitem4 = self.tblItems.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Qty Received", None))
        ___qtablewidgetitem5 = self.tblItems.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Unit Cost", None))
        ___qtablewidgetitem6 = self.tblItems.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Total", None))
        self.btnAddItem.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Add Item", None))
        self.btnEditItem.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Edit Item", None))
        self.btnDeleteItem.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Delete Item", None))
        self.btnReceiveStock.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Receive Stock", None))
        self.lblTotal.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Total: N$ 0.00", None))
        self.groupNotes.setTitle(QCoreApplication.translate("PurchaseOrderDialog", u"Notes", None))
        self.btnMarkOrdered.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Mark Ordered", None))
        self.btnCancelOrder.setText(QCoreApplication.translate("PurchaseOrderDialog", u"Cancel Order", None))
    # retranslateUi


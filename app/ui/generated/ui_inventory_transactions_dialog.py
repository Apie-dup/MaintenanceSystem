# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inventory_transactions_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QHeaderView, QLabel, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_InventoryTransactionsDialog(object):
    def setupUi(self, InventoryTransactionsDialog):
        if not InventoryTransactionsDialog.objectName():
            InventoryTransactionsDialog.setObjectName(u"InventoryTransactionsDialog")
        InventoryTransactionsDialog.resize(1081, 550)
        self.verticalLayout = QVBoxLayout(InventoryTransactionsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(InventoryTransactionsDialog)
        self.lblTitle.setObjectName(u"lblTitle")

        self.verticalLayout.addWidget(self.lblTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblPartNumber = QLabel(InventoryTransactionsDialog)
        self.lblPartNumber.setObjectName(u"lblPartNumber")

        self.horizontalLayout.addWidget(self.lblPartNumber)

        self.lblPartName = QLabel(InventoryTransactionsDialog)
        self.lblPartName.setObjectName(u"lblPartName")

        self.horizontalLayout.addWidget(self.lblPartName)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblTransactions = QTableWidget(InventoryTransactionsDialog)
        if (self.tblTransactions.columnCount() < 10):
            self.tblTransactions.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblTransactions.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblTransactions.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblTransactions.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblTransactions.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblTransactions.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblTransactions.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblTransactions.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblTransactions.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblTransactions.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblTransactions.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tblTransactions.setObjectName(u"tblTransactions")

        self.verticalLayout.addWidget(self.tblTransactions)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.buttonBox = QDialogButtonBox(InventoryTransactionsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel)

        self.horizontalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(InventoryTransactionsDialog)
        self.buttonBox.accepted.connect(InventoryTransactionsDialog.accept)
        self.buttonBox.rejected.connect(InventoryTransactionsDialog.reject)

        QMetaObject.connectSlotsByName(InventoryTransactionsDialog)
    # setupUi

    def retranslateUi(self, InventoryTransactionsDialog):
        InventoryTransactionsDialog.setWindowTitle(QCoreApplication.translate("InventoryTransactionsDialog", u"Inventory Transactions", None))
        self.lblTitle.setText(QCoreApplication.translate("InventoryTransactionsDialog", u"Inventory Transactions", None))
        self.lblPartNumber.setText(QCoreApplication.translate("InventoryTransactionsDialog", u"TextLabel", None))
        self.lblPartName.setText(QCoreApplication.translate("InventoryTransactionsDialog", u"TextLabel", None))
        ___qtablewidgetitem = self.tblTransactions.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("InventoryTransactionsDialog", u"Date / Time", None))
        ___qtablewidgetitem1 = self.tblTransactions.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("InventoryTransactionsDialog", u"Type", None))
        ___qtablewidgetitem2 = self.tblTransactions.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("InventoryTransactionsDialog", u"Change", None))
        ___qtablewidgetitem3 = self.tblTransactions.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("InventoryTransactionsDialog", u"Previous", None))
        ___qtablewidgetitem4 = self.tblTransactions.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("InventoryTransactionsDialog", u"New", None))
        ___qtablewidgetitem5 = self.tblTransactions.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("InventoryTransactionsDialog", u"Unit Cost", None))
        ___qtablewidgetitem6 = self.tblTransactions.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("InventoryTransactionsDialog", u"Work Order", None))
        ___qtablewidgetitem7 = self.tblTransactions.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("InventoryTransactionsDialog", u"Reference", None))
        ___qtablewidgetitem8 = self.tblTransactions.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("InventoryTransactionsDialog", u"User", None))
        ___qtablewidgetitem9 = self.tblTransactions.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("InventoryTransactionsDialog", u"Notes", None))
    # retranslateUi


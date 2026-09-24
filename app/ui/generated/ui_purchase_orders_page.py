# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'purchase_orders_page.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_PurchaseOrdersPage(object):
    def setupUi(self, PurchaseOrdersPage):
        if not PurchaseOrdersPage.objectName():
            PurchaseOrdersPage.setObjectName(u"PurchaseOrdersPage")
        PurchaseOrdersPage.resize(747, 487)
        self.verticalLayout = QVBoxLayout(PurchaseOrdersPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(PurchaseOrdersPage)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSearch = QLabel(PurchaseOrdersPage)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(PurchaseOrdersPage)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblPurchaseOrders = QTableWidget(PurchaseOrdersPage)
        if (self.tblPurchaseOrders.columnCount() < 7):
            self.tblPurchaseOrders.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblPurchaseOrders.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblPurchaseOrders.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblPurchaseOrders.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblPurchaseOrders.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblPurchaseOrders.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblPurchaseOrders.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblPurchaseOrders.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tblPurchaseOrders.setObjectName(u"tblPurchaseOrders")
        self.tblPurchaseOrders.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblPurchaseOrders.setAlternatingRowColors(True)
        self.tblPurchaseOrders.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblPurchaseOrders.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.tblPurchaseOrders)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(PurchaseOrdersPage)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(PurchaseOrdersPage)
        self.btnEdit.setObjectName(u"btnEdit")

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnRefresh = QPushButton(PurchaseOrdersPage)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.btnDelete = QPushButton(PurchaseOrdersPage)
        self.btnDelete.setObjectName(u"btnDelete")

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(PurchaseOrdersPage)

        QMetaObject.connectSlotsByName(PurchaseOrdersPage)
    # setupUi

    def retranslateUi(self, PurchaseOrdersPage):
        PurchaseOrdersPage.setWindowTitle(QCoreApplication.translate("PurchaseOrdersPage", u"Purchase Orders", None))
        self.lblTitle.setText(QCoreApplication.translate("PurchaseOrdersPage", u"Purchase Orders", None))
        self.lblSearch.setText(QCoreApplication.translate("PurchaseOrdersPage", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("PurchaseOrdersPage", u"Search purchase orders...", None))
        ___qtablewidgetitem = self.tblPurchaseOrders.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PurchaseOrdersPage", u"PO Number", None))
        ___qtablewidgetitem1 = self.tblPurchaseOrders.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PurchaseOrdersPage", u"Supplier", None))
        ___qtablewidgetitem2 = self.tblPurchaseOrders.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PurchaseOrdersPage", u"Order Date", None))
        ___qtablewidgetitem3 = self.tblPurchaseOrders.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PurchaseOrdersPage", u"Expected Date", None))
        ___qtablewidgetitem4 = self.tblPurchaseOrders.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PurchaseOrdersPage", u"Status", None))
        ___qtablewidgetitem5 = self.tblPurchaseOrders.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PurchaseOrdersPage", u"Refresh", None))
        ___qtablewidgetitem6 = self.tblPurchaseOrders.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PurchaseOrdersPage", u"Total", None))
        self.btnAdd.setText(QCoreApplication.translate("PurchaseOrdersPage", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("PurchaseOrdersPage", u"Edit", None))
        self.btnRefresh.setText(QCoreApplication.translate("PurchaseOrdersPage", u"Refresh", None))
        self.btnDelete.setText(QCoreApplication.translate("PurchaseOrdersPage", u"Delete", None))
    # retranslateUi


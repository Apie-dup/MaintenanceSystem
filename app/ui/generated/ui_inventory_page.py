# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inventory_page.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_InventoryWindow(object):
    def setupUi(self, InventoryWindow):
        if not InventoryWindow.objectName():
            InventoryWindow.setObjectName(u"InventoryWindow")
        InventoryWindow.resize(979, 708)
        self.verticalLayout = QVBoxLayout(InventoryWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(InventoryWindow)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSearch = QLabel(InventoryWindow)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(InventoryWindow)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblInventory = QTableWidget(InventoryWindow)
        if (self.tblInventory.columnCount() < 9):
            self.tblInventory.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tblInventory.setObjectName(u"tblInventory")

        self.verticalLayout.addWidget(self.tblInventory)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(InventoryWindow)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(InventoryWindow)
        self.btnEdit.setObjectName(u"btnEdit")

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnRefresh = QPushButton(InventoryWindow)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.btnDelete = QPushButton(InventoryWindow)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnClose = QPushButton(InventoryWindow)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lblStatus = QLabel(InventoryWindow)
        self.lblStatus.setObjectName(u"lblStatus")

        self.verticalLayout.addWidget(self.lblStatus)


        self.retranslateUi(InventoryWindow)

        QMetaObject.connectSlotsByName(InventoryWindow)
    # setupUi

    def retranslateUi(self, InventoryWindow):
        InventoryWindow.setWindowTitle(QCoreApplication.translate("InventoryWindow", u"Inventory Window", None))
        self.lblTitle.setText(QCoreApplication.translate("InventoryWindow", u"Inventory", None))
        self.lblSearch.setText(QCoreApplication.translate("InventoryWindow", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("InventoryWindow", u"Search by Part Number, Name, or Location...", None))
        ___qtablewidgetitem = self.tblInventory.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("InventoryWindow", u"ID", None))
        ___qtablewidgetitem1 = self.tblInventory.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("InventoryWindow", u"Part Number", None))
        ___qtablewidgetitem2 = self.tblInventory.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("InventoryWindow", u"Part Name", None))
        ___qtablewidgetitem3 = self.tblInventory.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("InventoryWindow", u"Category", None))
        ___qtablewidgetitem4 = self.tblInventory.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("InventoryWindow", u"Quantity", None))
        ___qtablewidgetitem5 = self.tblInventory.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("InventoryWindow", u"Minimum", None))
        ___qtablewidgetitem6 = self.tblInventory.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("InventoryWindow", u"Location", None))
        ___qtablewidgetitem7 = self.tblInventory.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("InventoryWindow", u"Status", None))
        ___qtablewidgetitem8 = self.tblInventory.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("InventoryWindow", u"Unit Cost", None))
        self.btnAdd.setText(QCoreApplication.translate("InventoryWindow", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("InventoryWindow", u"Edit", None))
        self.btnRefresh.setText(QCoreApplication.translate("InventoryWindow", u"Refresh", None))
        self.btnDelete.setText(QCoreApplication.translate("InventoryWindow", u"Delete", None))
        self.btnClose.setText(QCoreApplication.translate("InventoryWindow", u"Close", None))
        self.lblStatus.setText(QCoreApplication.translate("InventoryWindow", u"Status", None))
    # retranslateUi


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

class Ui_InventoryPage(object):
    def setupUi(self, InventoryPage):
        if not InventoryPage.objectName():
            InventoryPage.setObjectName(u"InventoryPage")
        InventoryPage.resize(1359, 520)
        self.verticalLayout = QVBoxLayout(InventoryPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(InventoryPage)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSearch = QLabel(InventoryPage)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(InventoryPage)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblInventory = QTableWidget(InventoryPage)
        if (self.tblInventory.columnCount() < 13):
            self.tblInventory.setColumnCount(13)
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
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        self.tblInventory.setObjectName(u"tblInventory")
        self.tblInventory.setAlternatingRowColors(True)
        self.tblInventory.setWordWrap(False)
        self.tblInventory.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.tblInventory)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(InventoryPage)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setMinimumSize(QSize(90, 30))
        self.btnAdd.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(InventoryPage)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnRefresh = QPushButton(InventoryPage)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setMinimumSize(QSize(90, 30))
        self.btnRefresh.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.btnDelete = QPushButton(InventoryPage)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(90, 30))
        self.btnDelete.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lblStatus = QLabel(InventoryPage)
        self.lblStatus.setObjectName(u"lblStatus")

        self.verticalLayout.addWidget(self.lblStatus)


        self.retranslateUi(InventoryPage)

        QMetaObject.connectSlotsByName(InventoryPage)
    # setupUi

    def retranslateUi(self, InventoryPage):
        InventoryPage.setWindowTitle(QCoreApplication.translate("InventoryPage", u"Inventory Page", None))
        self.lblTitle.setText(QCoreApplication.translate("InventoryPage", u"Inventory", None))
        self.lblSearch.setText(QCoreApplication.translate("InventoryPage", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("InventoryPage", u"Search by Part Number, Name, or Location...", None))
        ___qtablewidgetitem = self.tblInventory.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("InventoryPage", u"ID", None))
        ___qtablewidgetitem1 = self.tblInventory.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("InventoryPage", u"Part Number", None))
        ___qtablewidgetitem2 = self.tblInventory.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("InventoryPage", u"Part Name", None))
        ___qtablewidgetitem3 = self.tblInventory.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("InventoryPage", u"Description", None))
        ___qtablewidgetitem4 = self.tblInventory.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("InventoryPage", u"Category", None))
        ___qtablewidgetitem5 = self.tblInventory.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("InventoryPage", u"Supplier ID", None))
        ___qtablewidgetitem6 = self.tblInventory.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("InventoryPage", u"Unit", None))
        ___qtablewidgetitem7 = self.tblInventory.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("InventoryPage", u"Quantity", None))
        ___qtablewidgetitem8 = self.tblInventory.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("InventoryPage", u"Minimum Quantity", None))
        ___qtablewidgetitem9 = self.tblInventory.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("InventoryPage", u"Reorder Quantity", None))
        ___qtablewidgetitem10 = self.tblInventory.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("InventoryPage", u"Unit Cost", None))
        ___qtablewidgetitem11 = self.tblInventory.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("InventoryPage", u"Location", None))
        ___qtablewidgetitem12 = self.tblInventory.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("InventoryPage", u"Notes", None))
        self.btnAdd.setText(QCoreApplication.translate("InventoryPage", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("InventoryPage", u"Edit", None))
        self.btnRefresh.setText(QCoreApplication.translate("InventoryPage", u"Refresh", None))
        self.btnDelete.setText(QCoreApplication.translate("InventoryPage", u"Delete", None))
        self.lblStatus.setText(QCoreApplication.translate("InventoryPage", u"Status", None))
    # retranslateUi


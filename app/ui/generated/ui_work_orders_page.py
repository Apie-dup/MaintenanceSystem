# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'work_orders_page.ui'
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

class Ui_WorkOrdersPage(object):
    def setupUi(self, WorkOrdersPage):
        if not WorkOrdersPage.objectName():
            WorkOrdersPage.setObjectName(u"WorkOrdersPage")
        WorkOrdersPage.resize(921, 709)
        self.verticalLayout = QVBoxLayout(WorkOrdersPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblWorkOrders = QLabel(WorkOrdersPage)
        self.lblWorkOrders.setObjectName(u"lblWorkOrders")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lblWorkOrders.setFont(font)

        self.verticalLayout.addWidget(self.lblWorkOrders)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSearch = QLabel(WorkOrdersPage)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(WorkOrdersPage)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblWorkOrders = QTableWidget(WorkOrdersPage)
        if (self.tblWorkOrders.columnCount() < 9):
            self.tblWorkOrders.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblWorkOrders.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblWorkOrders.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblWorkOrders.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblWorkOrders.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblWorkOrders.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblWorkOrders.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblWorkOrders.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblWorkOrders.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblWorkOrders.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tblWorkOrders.setObjectName(u"tblWorkOrders")
        self.tblWorkOrders.setWordWrap(False)
        self.tblWorkOrders.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tblWorkOrders)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(WorkOrdersPage)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setMinimumSize(QSize(90, 30))
        self.btnAdd.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(WorkOrdersPage)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setMinimumSize(QSize(90, 30))
        self.btnEdit.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnRefresh = QPushButton(WorkOrdersPage)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setMinimumSize(QSize(90, 30))
        self.btnRefresh.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.btnDelete = QPushButton(WorkOrdersPage)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(90, 30))
        self.btnDelete.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.horizontalSpacer = QSpacerItem(852, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lblStatus = QLabel(WorkOrdersPage)
        self.lblStatus.setObjectName(u"lblStatus")

        self.verticalLayout.addWidget(self.lblStatus)


        self.retranslateUi(WorkOrdersPage)

        QMetaObject.connectSlotsByName(WorkOrdersPage)
    # setupUi

    def retranslateUi(self, WorkOrdersPage):
        WorkOrdersPage.setWindowTitle(QCoreApplication.translate("WorkOrdersPage", u"Work Orders Page", None))
        self.lblWorkOrders.setText(QCoreApplication.translate("WorkOrdersPage", u"Work Orders", None))
        self.lblSearch.setText(QCoreApplication.translate("WorkOrdersPage", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("WorkOrdersPage", u"Search work orders....", None))
        ___qtablewidgetitem = self.tblWorkOrders.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WorkOrdersPage", u"ID", None))
        ___qtablewidgetitem1 = self.tblWorkOrders.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WorkOrdersPage", u"WO Number", None))
        ___qtablewidgetitem2 = self.tblWorkOrders.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WorkOrdersPage", u"Asset", None))
        ___qtablewidgetitem3 = self.tblWorkOrders.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WorkOrdersPage", u"Title", None))
        ___qtablewidgetitem4 = self.tblWorkOrders.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WorkOrdersPage", u"Priority", None))
        ___qtablewidgetitem5 = self.tblWorkOrders.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("WorkOrdersPage", u"Status", None))
        ___qtablewidgetitem6 = self.tblWorkOrders.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("WorkOrdersPage", u"Technician", None))
        ___qtablewidgetitem7 = self.tblWorkOrders.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("WorkOrdersPage", u"Due Date", None))
        ___qtablewidgetitem8 = self.tblWorkOrders.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("WorkOrdersPage", u"Notes", None))
        self.btnAdd.setText(QCoreApplication.translate("WorkOrdersPage", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("WorkOrdersPage", u"Edit", None))
        self.btnRefresh.setText(QCoreApplication.translate("WorkOrdersPage", u"Refresh", None))
        self.btnDelete.setText(QCoreApplication.translate("WorkOrdersPage", u"Delete", None))
        self.lblStatus.setText(QCoreApplication.translate("WorkOrdersPage", u"Status", None))
    # retranslateUi


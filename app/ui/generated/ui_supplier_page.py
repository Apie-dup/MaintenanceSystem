# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'supplier_page.ui'
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

class Ui_SuppliersWindow(object):
    def setupUi(self, SuppliersWindow):
        if not SuppliersWindow.objectName():
            SuppliersWindow.setObjectName(u"SuppliersWindow")
        SuppliersWindow.resize(911, 485)
        self.verticalLayout = QVBoxLayout(SuppliersWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblSuppliers = QLabel(SuppliersWindow)
        self.lblSuppliers.setObjectName(u"lblSuppliers")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lblSuppliers.setFont(font)

        self.verticalLayout.addWidget(self.lblSuppliers)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSearch = QLabel(SuppliersWindow)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(SuppliersWindow)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblSuppliers = QTableWidget(SuppliersWindow)
        if (self.tblSuppliers.columnCount() < 9):
            self.tblSuppliers.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblSuppliers.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tblSuppliers.setObjectName(u"tblSuppliers")
        self.tblSuppliers.setAlternatingRowColors(True)
        self.tblSuppliers.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.tblSuppliers)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(SuppliersWindow)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setMinimumSize(QSize(90, 30))
        self.btnAdd.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(SuppliersWindow)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setMinimumSize(QSize(90, 30))
        self.btnEdit.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnRefresh = QPushButton(SuppliersWindow)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setMinimumSize(QSize(90, 30))
        self.btnRefresh.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.btnDelete = QPushButton(SuppliersWindow)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lblStatus = QLabel(SuppliersWindow)
        self.lblStatus.setObjectName(u"lblStatus")

        self.verticalLayout.addWidget(self.lblStatus)


        self.retranslateUi(SuppliersWindow)

        QMetaObject.connectSlotsByName(SuppliersWindow)
    # setupUi

    def retranslateUi(self, SuppliersWindow):
        SuppliersWindow.setWindowTitle(QCoreApplication.translate("SuppliersWindow", u"Suppliers Window", None))
        self.lblSuppliers.setText(QCoreApplication.translate("SuppliersWindow", u"Suppliers", None))
        self.lblSearch.setText(QCoreApplication.translate("SuppliersWindow", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("SuppliersWindow", u"Search by Supplier Code, Supplie Name, Contact Person....", None))
        ___qtablewidgetitem = self.tblSuppliers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SuppliersWindow", u"ID", None))
        ___qtablewidgetitem1 = self.tblSuppliers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SuppliersWindow", u"Supplier Code", None))
        ___qtablewidgetitem2 = self.tblSuppliers.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SuppliersWindow", u"Supplier Name", None))
        ___qtablewidgetitem3 = self.tblSuppliers.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SuppliersWindow", u"Contact Person", None))
        ___qtablewidgetitem4 = self.tblSuppliers.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SuppliersWindow", u"Phone", None))
        ___qtablewidgetitem5 = self.tblSuppliers.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SuppliersWindow", u"Email", None))
        ___qtablewidgetitem6 = self.tblSuppliers.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("SuppliersWindow", u"Address", None))
        ___qtablewidgetitem7 = self.tblSuppliers.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("SuppliersWindow", u"Status", None))
        ___qtablewidgetitem8 = self.tblSuppliers.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("SuppliersWindow", u"Notes", None))
        self.btnAdd.setText(QCoreApplication.translate("SuppliersWindow", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("SuppliersWindow", u"Edit", None))
        self.btnRefresh.setText(QCoreApplication.translate("SuppliersWindow", u"Refresh", None))
        self.btnDelete.setText(QCoreApplication.translate("SuppliersWindow", u"Delete", None))
        self.lblStatus.setText(QCoreApplication.translate("SuppliersWindow", u"Status", None))
    # retranslateUi


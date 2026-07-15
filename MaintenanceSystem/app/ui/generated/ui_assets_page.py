# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assets_page.ui'
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

class Ui_AssetsWindow(object):
    def setupUi(self, AssetsWindow):
        if not AssetsWindow.objectName():
            AssetsWindow.setObjectName(u"AssetsWindow")
        AssetsWindow.resize(1300, 703)
        self.verticalLayout_2 = QVBoxLayout(AssetsWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblTitle = QLabel(AssetsWindow)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout_2.addWidget(self.lblTitle)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSearch = QLabel(AssetsWindow)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(AssetsWindow)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblAssets = QTableWidget(AssetsWindow)
        if (self.tblAssets.columnCount() < 11):
            self.tblAssets.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblAssets.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblAssets.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblAssets.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblAssets.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblAssets.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblAssets.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblAssets.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblAssets.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblAssets.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblAssets.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tblAssets.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tblAssets.setObjectName(u"tblAssets")
        self.tblAssets.setAlternatingRowColors(True)
        self.tblAssets.setSortingEnabled(True)
        self.tblAssets.setColumnCount(11)

        self.verticalLayout.addWidget(self.tblAssets)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(AssetsWindow)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setMinimumSize(QSize(90, 32))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        self.btnAdd.setFont(font1)
        self.btnAdd.setStyleSheet(u"")
        self.btnAdd.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(AssetsWindow)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setMinimumSize(QSize(90, 32))
        self.btnEdit.setStyleSheet(u"")
        self.btnEdit.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(AssetsWindow)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(90, 32))
        self.btnDelete.setStyleSheet(u"")
        self.btnDelete.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.btnRefresh = QPushButton(AssetsWindow)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setMinimumSize(QSize(90, 32))
        self.btnRefresh.setStyleSheet(u"")
        self.btnRefresh.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(AssetsWindow)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(90, 32))
        self.btnClose.setStyleSheet(u"")
        self.btnClose.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.lblStatus = QLabel(AssetsWindow)
        self.lblStatus.setObjectName(u"lblStatus")

        self.verticalLayout_2.addWidget(self.lblStatus)


        self.retranslateUi(AssetsWindow)

        QMetaObject.connectSlotsByName(AssetsWindow)
    # setupUi

    def retranslateUi(self, AssetsWindow):
        AssetsWindow.setWindowTitle(QCoreApplication.translate("AssetsWindow", u"Assets Window", None))
        self.lblTitle.setText(QCoreApplication.translate("AssetsWindow", u"Assets", None))
        self.lblSearch.setText(QCoreApplication.translate("AssetsWindow", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("AssetsWindow", u"Search by asset number, name, category, location....", None))
        ___qtablewidgetitem = self.tblAssets.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AssetsWindow", u"ID", None))
        ___qtablewidgetitem1 = self.tblAssets.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AssetsWindow", u"Asset  Number", None))
        ___qtablewidgetitem2 = self.tblAssets.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AssetsWindow", u"Asset Name", None))
        ___qtablewidgetitem3 = self.tblAssets.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AssetsWindow", u"Description", None))
        ___qtablewidgetitem4 = self.tblAssets.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AssetsWindow", u"Category", None))
        ___qtablewidgetitem5 = self.tblAssets.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AssetsWindow", u"Location", None))
        ___qtablewidgetitem6 = self.tblAssets.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AssetsWindow", u"Manufacturer", None))
        ___qtablewidgetitem7 = self.tblAssets.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AssetsWindow", u"Model", None))
        ___qtablewidgetitem8 = self.tblAssets.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("AssetsWindow", u"Serial No.", None))
        ___qtablewidgetitem9 = self.tblAssets.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("AssetsWindow", u"Status", None))
        ___qtablewidgetitem10 = self.tblAssets.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("AssetsWindow", u"Warranty Expiry", None))
        self.btnAdd.setText(QCoreApplication.translate("AssetsWindow", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("AssetsWindow", u"Edit", None))
        self.btnDelete.setText(QCoreApplication.translate("AssetsWindow", u"Delete", None))
        self.btnRefresh.setText(QCoreApplication.translate("AssetsWindow", u"Refresh", None))
        self.btnClose.setText(QCoreApplication.translate("AssetsWindow", u"Close", None))
        self.lblStatus.setText(QCoreApplication.translate("AssetsWindow", u"Status", None))
    # retranslateUi


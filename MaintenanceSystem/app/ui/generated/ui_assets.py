# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assets.ui'
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
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_AssetsWindow(object):
    def setupUi(self, AssetsWindow):
        if not AssetsWindow.objectName():
            AssetsWindow.setObjectName(u"AssetsWindow")
        AssetsWindow.resize(910, 600)
        self.centralwidget = QWidget(AssetsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(self.centralwidget)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSearch = QLabel(self.centralwidget)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(self.centralwidget)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblAssets = QTableWidget(self.centralwidget)
        if (self.tblAssets.columnCount() < 9):
            self.tblAssets.setColumnCount(9)
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
        self.tblAssets.setObjectName(u"tblAssets")
        self.tblAssets.setColumnCount(9)

        self.verticalLayout.addWidget(self.tblAssets)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(self.centralwidget)
        self.btnEdit.setObjectName(u"btnEdit")

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(self.centralwidget)
        self.btnDelete.setObjectName(u"btnDelete")

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.btnRefresh = QPushButton(self.centralwidget)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.btnClose = QPushButton(self.centralwidget)
        self.btnClose.setObjectName(u"btnClose")

        self.horizontalLayout_2.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lblStatus = QLabel(self.centralwidget)
        self.lblStatus.setObjectName(u"lblStatus")

        self.verticalLayout.addWidget(self.lblStatus)

        AssetsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AssetsWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 910, 33))
        AssetsWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AssetsWindow)
        self.statusbar.setObjectName(u"statusbar")
        AssetsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AssetsWindow)

        QMetaObject.connectSlotsByName(AssetsWindow)
    # setupUi

    def retranslateUi(self, AssetsWindow):
        AssetsWindow.setWindowTitle(QCoreApplication.translate("AssetsWindow", u"Assets", None))
        self.lblTitle.setText(QCoreApplication.translate("AssetsWindow", u"Assets", None))
        self.lblSearch.setText(QCoreApplication.translate("AssetsWindow", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("AssetsWindow", u"Search by asset number, name, category, location....", None))
        ___qtablewidgetitem = self.tblAssets.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AssetsWindow", u"ID", None))
        ___qtablewidgetitem1 = self.tblAssets.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AssetsWindow", u"Asset Name", None))
        ___qtablewidgetitem2 = self.tblAssets.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AssetsWindow", u"Asset No.", None))
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
        ___qtablewidgetitem8.setText(QCoreApplication.translate("AssetsWindow", u"Status", None))
        self.btnAdd.setText(QCoreApplication.translate("AssetsWindow", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("AssetsWindow", u"Edit", None))
        self.btnDelete.setText(QCoreApplication.translate("AssetsWindow", u"Delete", None))
        self.btnRefresh.setText(QCoreApplication.translate("AssetsWindow", u"Refresh", None))
        self.btnClose.setText(QCoreApplication.translate("AssetsWindow", u"Close", None))
        self.lblStatus.setText(QCoreApplication.translate("AssetsWindow", u"Status", None))
    # retranslateUi


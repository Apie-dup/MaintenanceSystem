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
    QWidget)

class Ui_AssetsWindow(object):
    def setupUi(self, AssetsWindow):
        if not AssetsWindow.objectName():
            AssetsWindow.setObjectName(u"AssetsWindow")
        AssetsWindow.resize(1280, 720)
        AssetsWindow.setMinimumSize(QSize(1280, 720))
        self.centralwidget = QWidget(AssetsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblTitle = QLabel(self.centralwidget)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setGeometry(QRect(10, 20, 101, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lblTitle.setFont(font)
        self.tblAssets = QTableWidget(self.centralwidget)
        if (self.tblAssets.columnCount() < 10):
            self.tblAssets.setColumnCount(10)
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
        self.tblAssets.setObjectName(u"tblAssets")
        self.tblAssets.setGeometry(QRect(10, 160, 691, 192))
        self.tblAssets.setColumnCount(10)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 70, 381, 81))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblSearch = QLabel(self.horizontalLayoutWidget)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(self.horizontalLayoutWidget)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)

        self.btnSearch = QPushButton(self.horizontalLayoutWidget)
        self.btnSearch.setObjectName(u"btnSearch")

        self.horizontalLayout.addWidget(self.btnSearch)

        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(20, 380, 81, 26))
        self.btnEdit = QPushButton(self.centralwidget)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setGeometry(QRect(120, 380, 81, 26))
        self.btnDelete = QPushButton(self.centralwidget)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setGeometry(QRect(220, 380, 81, 26))
        self.btnRefresh = QPushButton(self.centralwidget)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setGeometry(QRect(320, 380, 81, 26))
        self.btnClose = QPushButton(self.centralwidget)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(420, 380, 81, 26))
        AssetsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AssetsWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 33))
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
        ___qtablewidgetitem = self.tblAssets.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AssetsWindow", u"New Column", None))
        ___qtablewidgetitem1 = self.tblAssets.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AssetsWindow", u"Asset No", None))
        ___qtablewidgetitem2 = self.tblAssets.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AssetsWindow", u"Description", None))
        ___qtablewidgetitem3 = self.tblAssets.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AssetsWindow", u"Category", None))
        ___qtablewidgetitem4 = self.tblAssets.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AssetsWindow", u"Location", None))
        ___qtablewidgetitem5 = self.tblAssets.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AssetsWindow", u"Manufacturer", None))
        ___qtablewidgetitem6 = self.tblAssets.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AssetsWindow", u"Model", None))
        ___qtablewidgetitem7 = self.tblAssets.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AssetsWindow", u"Serial No", None))
        ___qtablewidgetitem8 = self.tblAssets.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("AssetsWindow", u"Status", None))
        ___qtablewidgetitem9 = self.tblAssets.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("AssetsWindow", u"Edit", None))
        self.lblSearch.setText(QCoreApplication.translate("AssetsWindow", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("AssetsWindow", u"Search assets...", None))
        self.btnSearch.setText(QCoreApplication.translate("AssetsWindow", u"Search", None))
        self.btnAdd.setText(QCoreApplication.translate("AssetsWindow", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("AssetsWindow", u"Edit", None))
        self.btnDelete.setText(QCoreApplication.translate("AssetsWindow", u"Delete", None))
        self.btnRefresh.setText(QCoreApplication.translate("AssetsWindow", u"Refresh", None))
        self.btnClose.setText(QCoreApplication.translate("AssetsWindow", u"Close", None))
    # retranslateUi


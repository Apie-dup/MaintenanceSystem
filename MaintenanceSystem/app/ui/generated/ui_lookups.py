# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lookups.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_LookupWindow(object):
    def setupUi(self, LookupWindow):
        if not LookupWindow.objectName():
            LookupWindow.setObjectName(u"LookupWindow")
        LookupWindow.resize(1307, 682)
        self.centralwidget = QWidget(LookupWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(self.centralwidget)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.lblLookupType = QLabel(self.centralwidget)
        self.lblLookupType.setObjectName(u"lblLookupType")

        self.verticalLayout.addWidget(self.lblLookupType)

        self.cmbLookupType = QComboBox(self.centralwidget)
        self.cmbLookupType.setObjectName(u"cmbLookupType")

        self.verticalLayout.addWidget(self.cmbLookupType)

        self.lblSearch = QLabel(self.centralwidget)
        self.lblSearch.setObjectName(u"lblSearch")

        self.verticalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(self.centralwidget)
        self.txtSearch.setObjectName(u"txtSearch")

        self.verticalLayout.addWidget(self.txtSearch)

        self.tblLookup = QTableWidget(self.centralwidget)
        if (self.tblLookup.columnCount() < 2):
            self.tblLookup.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblLookup.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblLookup.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tblLookup.setObjectName(u"tblLookup")
        self.tblLookup.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblLookup.setAlternatingRowColors(True)
        self.tblLookup.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblLookup.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblLookup.setSortingEnabled(True)
        self.tblLookup.setColumnCount(2)

        self.verticalLayout.addWidget(self.tblLookup)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(self.centralwidget)
        self.btnEdit.setObjectName(u"btnEdit")

        self.horizontalLayout.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(self.centralwidget)
        self.btnDelete.setObjectName(u"btnDelete")

        self.horizontalLayout.addWidget(self.btnDelete)

        self.btnRefresh = QPushButton(self.centralwidget)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.horizontalLayout.addWidget(self.btnRefresh)

        self.horizontalSpacer = QSpacerItem(879, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(self.centralwidget)
        self.btnClose.setObjectName(u"btnClose")

        self.horizontalLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lblStatus = QLabel(self.centralwidget)
        self.lblStatus.setObjectName(u"lblStatus")

        self.verticalLayout.addWidget(self.lblStatus)

        LookupWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LookupWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1307, 33))
        LookupWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LookupWindow)
        self.statusbar.setObjectName(u"statusbar")
        LookupWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LookupWindow)

        QMetaObject.connectSlotsByName(LookupWindow)
    # setupUi

    def retranslateUi(self, LookupWindow):
        LookupWindow.setWindowTitle(QCoreApplication.translate("LookupWindow", u"Lookup Management", None))
        self.lblTitle.setText(QCoreApplication.translate("LookupWindow", u"Lookup Management", None))
        self.lblLookupType.setText(QCoreApplication.translate("LookupWindow", u"Lookup Type", None))
        self.lblSearch.setText(QCoreApplication.translate("LookupWindow", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("LookupWindow", u"Search:", None))
        ___qtablewidgetitem = self.tblLookup.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LookupWindow", u"ID", None))
        ___qtablewidgetitem1 = self.tblLookup.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LookupWindow", u"Name", None))
        self.btnAdd.setText(QCoreApplication.translate("LookupWindow", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("LookupWindow", u"Edit", None))
        self.btnDelete.setText(QCoreApplication.translate("LookupWindow", u"Delete", None))
        self.btnRefresh.setText(QCoreApplication.translate("LookupWindow", u"Refresh", None))
        self.btnClose.setText(QCoreApplication.translate("LookupWindow", u"Close", None))
        self.lblStatus.setText(QCoreApplication.translate("LookupWindow", u"Status", None))
    # retranslateUi


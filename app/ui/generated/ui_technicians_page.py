# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'technicians_page.ui'
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

class Ui_TechniciansWindow(object):
    def setupUi(self, TechniciansWindow):
        if not TechniciansWindow.objectName():
            TechniciansWindow.setObjectName(u"TechniciansWindow")
        TechniciansWindow.resize(1966, 696)
        self.verticalLayout = QVBoxLayout(TechniciansWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTechnicians = QLabel(TechniciansWindow)
        self.lblTechnicians.setObjectName(u"lblTechnicians")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lblTechnicians.setFont(font)

        self.verticalLayout.addWidget(self.lblTechnicians)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSearch = QLabel(TechniciansWindow)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(TechniciansWindow)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblTechnicians = QTableWidget(TechniciansWindow)
        if (self.tblTechnicians.columnCount() < 8):
            self.tblTechnicians.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblTechnicians.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblTechnicians.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblTechnicians.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblTechnicians.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblTechnicians.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblTechnicians.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblTechnicians.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblTechnicians.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tblTechnicians.setObjectName(u"tblTechnicians")
        self.tblTechnicians.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblTechnicians.setAlternatingRowColors(True)
        self.tblTechnicians.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblTechnicians.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tblTechnicians)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(TechniciansWindow)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setMinimumSize(QSize(90, 32))
        self.btnAdd.setStyleSheet(u"")
        self.btnAdd.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(TechniciansWindow)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setMinimumSize(QSize(90, 32))
        self.btnEdit.setStyleSheet(u"")
        self.btnEdit.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnRefresh = QPushButton(TechniciansWindow)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.btnDelete = QPushButton(TechniciansWindow)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(90, 32))
        self.btnDelete.setStyleSheet(u"")
        self.btnDelete.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.horizontalSpacer = QSpacerItem(1299, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(TechniciansWindow)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(90, 32))
        self.btnClose.setStyleSheet(u"")
        self.btnClose.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lblStatus = QLabel(TechniciansWindow)
        self.lblStatus.setObjectName(u"lblStatus")

        self.verticalLayout.addWidget(self.lblStatus)


        self.retranslateUi(TechniciansWindow)

        QMetaObject.connectSlotsByName(TechniciansWindow)
    # setupUi

    def retranslateUi(self, TechniciansWindow):
        TechniciansWindow.setWindowTitle(QCoreApplication.translate("TechniciansWindow", u"Technicians Window", None))
        self.lblTechnicians.setText(QCoreApplication.translate("TechniciansWindow", u"Technicians", None))
        self.lblSearch.setText(QCoreApplication.translate("TechniciansWindow", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("TechniciansWindow", u"Search technicians...", None))
        ___qtablewidgetitem = self.tblTechnicians.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TechniciansWindow", u"ID", None))
        ___qtablewidgetitem1 = self.tblTechnicians.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TechniciansWindow", u"Employee No.", None))
        ___qtablewidgetitem2 = self.tblTechnicians.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TechniciansWindow", u"Emplyee Name", None))
        ___qtablewidgetitem3 = self.tblTechnicians.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TechniciansWindow", u"Last Name", None))
        ___qtablewidgetitem4 = self.tblTechnicians.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TechniciansWindow", u"Trade", None))
        ___qtablewidgetitem5 = self.tblTechnicians.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TechniciansWindow", u"Department", None))
        ___qtablewidgetitem6 = self.tblTechnicians.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TechniciansWindow", u"Phone", None))
        ___qtablewidgetitem7 = self.tblTechnicians.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("TechniciansWindow", u"Status", None))
        self.btnAdd.setText(QCoreApplication.translate("TechniciansWindow", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("TechniciansWindow", u"Edit", None))
        self.btnRefresh.setText(QCoreApplication.translate("TechniciansWindow", u"Refresh", None))
        self.btnDelete.setText(QCoreApplication.translate("TechniciansWindow", u"Delete", None))
        self.btnClose.setText(QCoreApplication.translate("TechniciansWindow", u"Close", None))
        self.lblStatus.setText(QCoreApplication.translate("TechniciansWindow", u"Status", None))
    # retranslateUi


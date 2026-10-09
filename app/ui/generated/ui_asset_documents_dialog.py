# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asset_documents_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_AssetDocumentsDialog(object):
    def setupUi(self, AssetDocumentsDialog):
        if not AssetDocumentsDialog.objectName():
            AssetDocumentsDialog.setObjectName(u"AssetDocumentsDialog")
        AssetDocumentsDialog.resize(950, 550)
        AssetDocumentsDialog.setMinimumSize(QSize(950, 550))
        self.verticalLayout = QVBoxLayout(AssetDocumentsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(AssetDocumentsDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.lblAsset = QLabel(AssetDocumentsDialog)
        self.lblAsset.setObjectName(u"lblAsset")

        self.verticalLayout.addWidget(self.lblAsset)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txtSearch = QLineEdit(AssetDocumentsDialog)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout.addWidget(self.txtSearch)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.cmbDocumentType = QComboBox(AssetDocumentsDialog)
        self.cmbDocumentType.setObjectName(u"cmbDocumentType")

        self.horizontalLayout.addWidget(self.cmbDocumentType)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblDocuments = QTableWidget(AssetDocumentsDialog)
        if (self.tblDocuments.columnCount() < 5):
            self.tblDocuments.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblDocuments.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblDocuments.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblDocuments.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblDocuments.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblDocuments.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblDocuments.setObjectName(u"tblDocuments")

        self.verticalLayout.addWidget(self.tblDocuments)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(AssetDocumentsDialog)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(AssetDocumentsDialog)
        self.btnEdit.setObjectName(u"btnEdit")

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnOpen = QPushButton(AssetDocumentsDialog)
        self.btnOpen.setObjectName(u"btnOpen")

        self.horizontalLayout_2.addWidget(self.btnOpen)

        self.btnDelete = QPushButton(AssetDocumentsDialog)
        self.btnDelete.setObjectName(u"btnDelete")

        self.horizontalLayout_2.addWidget(self.btnDelete)

        self.btnRefresh = QPushButton(AssetDocumentsDialog)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(AssetDocumentsDialog)
        self.btnClose.setObjectName(u"btnClose")

        self.horizontalLayout_2.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(AssetDocumentsDialog)

        QMetaObject.connectSlotsByName(AssetDocumentsDialog)
    # setupUi

    def retranslateUi(self, AssetDocumentsDialog):
        AssetDocumentsDialog.setWindowTitle(QCoreApplication.translate("AssetDocumentsDialog", u"Asset Documentation", None))
        self.lblTitle.setText(QCoreApplication.translate("AssetDocumentsDialog", u"Asset Documentation", None))
        self.lblAsset.setText(QCoreApplication.translate("AssetDocumentsDialog", u"Asset:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("AssetDocumentsDialog", u"Search Documents...", None))
        self.cmbDocumentType.setPlaceholderText(QCoreApplication.translate("AssetDocumentsDialog", u"Document type: All types", None))
        ___qtablewidgetitem = self.tblDocuments.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AssetDocumentsDialog", u"Document Name", None))
        ___qtablewidgetitem1 = self.tblDocuments.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AssetDocumentsDialog", u"Type", None))
        ___qtablewidgetitem2 = self.tblDocuments.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AssetDocumentsDialog", u"Filename", None))
        ___qtablewidgetitem3 = self.tblDocuments.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AssetDocumentsDialog", u"Uploaded", None))
        ___qtablewidgetitem4 = self.tblDocuments.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AssetDocumentsDialog", u"Expiry Date", None))
        self.btnAdd.setText(QCoreApplication.translate("AssetDocumentsDialog", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("AssetDocumentsDialog", u"Edit", None))
        self.btnOpen.setText(QCoreApplication.translate("AssetDocumentsDialog", u"Open", None))
        self.btnDelete.setText(QCoreApplication.translate("AssetDocumentsDialog", u"Delete", None))
        self.btnRefresh.setText(QCoreApplication.translate("AssetDocumentsDialog", u"Refresh", None))
        self.btnClose.setText(QCoreApplication.translate("AssetDocumentsDialog", u"Close", None))
    # retranslateUi

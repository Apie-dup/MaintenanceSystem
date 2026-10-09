# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asset_document_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDialog, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_AssetDocumentDialog(object):
    def setupUi(self, AssetDocumentDialog):
        if not AssetDocumentDialog.objectName():
            AssetDocumentDialog.setObjectName(u"AssetDocumentDialog")
        AssetDocumentDialog.resize(600, 507)
        AssetDocumentDialog.setMinimumSize(QSize(600, 420))
        self.verticalLayout = QVBoxLayout(AssetDocumentDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(AssetDocumentDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.lblAsset = QLabel(AssetDocumentDialog)
        self.lblAsset.setObjectName(u"lblAsset")

        self.verticalLayout.addWidget(self.lblAsset)

        self.lblDocumentName = QLabel(AssetDocumentDialog)
        self.lblDocumentName.setObjectName(u"lblDocumentName")

        self.verticalLayout.addWidget(self.lblDocumentName)

        self.txtDocumentName = QLineEdit(AssetDocumentDialog)
        self.txtDocumentName.setObjectName(u"txtDocumentName")

        self.verticalLayout.addWidget(self.txtDocumentName)

        self.lblDocumentType = QLabel(AssetDocumentDialog)
        self.lblDocumentType.setObjectName(u"lblDocumentType")

        self.verticalLayout.addWidget(self.lblDocumentType)

        self.cmbDocumentType = QComboBox(AssetDocumentDialog)
        self.cmbDocumentType.setObjectName(u"cmbDocumentType")

        self.verticalLayout.addWidget(self.cmbDocumentType)

        self.lblFile = QLabel(AssetDocumentDialog)
        self.lblFile.setObjectName(u"lblFile")

        self.verticalLayout.addWidget(self.lblFile)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txtFilePath = QLineEdit(AssetDocumentDialog)
        self.txtFilePath.setObjectName(u"txtFilePath")
        self.txtFilePath.setReadOnly(True)

        self.horizontalLayout.addWidget(self.txtFilePath)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnBrowse = QPushButton(AssetDocumentDialog)
        self.btnBrowse.setObjectName(u"btnBrowse")
        self.btnBrowse.setFlat(True)

        self.horizontalLayout.addWidget(self.btnBrowse)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lblDescription = QLabel(AssetDocumentDialog)
        self.lblDescription.setObjectName(u"lblDescription")

        self.verticalLayout.addWidget(self.lblDescription)

        self.txtDescription = QPlainTextEdit(AssetDocumentDialog)
        self.txtDescription.setObjectName(u"txtDescription")

        self.verticalLayout.addWidget(self.txtDescription)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dateExpiry = QDateEdit(AssetDocumentDialog)
        self.dateExpiry.setObjectName(u"dateExpiry")
        self.dateExpiry.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.dateExpiry)

        self.chkExpiryDate = QCheckBox(AssetDocumentDialog)
        self.chkExpiryDate.setObjectName(u"chkExpiryDate")

        self.horizontalLayout_3.addWidget(self.chkExpiryDate)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnCancel = QPushButton(AssetDocumentDialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnSave = QPushButton(AssetDocumentDialog)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(AssetDocumentDialog)

        QMetaObject.connectSlotsByName(AssetDocumentDialog)
    # setupUi

    def retranslateUi(self, AssetDocumentDialog):
        AssetDocumentDialog.setWindowTitle(QCoreApplication.translate("AssetDocumentDialog", u"Add Asset Document", None))
        self.lblTitle.setText(QCoreApplication.translate("AssetDocumentDialog", u"Add Asset Document", None))
        self.lblAsset.setText(QCoreApplication.translate("AssetDocumentDialog", u"Asset:", None))
        self.lblDocumentName.setText(QCoreApplication.translate("AssetDocumentDialog", u"Document Name", None))
        self.lblDocumentType.setText(QCoreApplication.translate("AssetDocumentDialog", u"Document Type", None))
        self.lblFile.setText(QCoreApplication.translate("AssetDocumentDialog", u"File", None))
        self.btnBrowse.setText(QCoreApplication.translate("AssetDocumentDialog", u"Browse...", None))
        self.lblDescription.setText(QCoreApplication.translate("AssetDocumentDialog", u"Description", None))
        self.chkExpiryDate.setText(QCoreApplication.translate("AssetDocumentDialog", u"Optional", None))
        self.btnCancel.setText(QCoreApplication.translate("AssetDocumentDialog", u"Cancel", None))
        self.btnSave.setText(QCoreApplication.translate("AssetDocumentDialog", u"Save", None))
    # retranslateUi

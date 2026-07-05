# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_asset.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QFormLayout, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_AddAssetDialog(object):
    def setupUi(self, AddAssetDialog):
        if not AddAssetDialog.objectName():
            AddAssetDialog.setObjectName(u"AddAssetDialog")
        AddAssetDialog.resize(600, 694)
        AddAssetDialog.setMinimumSize(QSize(600, 500))
        self.formLayout = QFormLayout(AddAssetDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.lblAssetNumber = QLabel(AddAssetDialog)
        self.lblAssetNumber.setObjectName(u"lblAssetNumber")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblAssetNumber)

        self.lblAssetName = QLabel(AddAssetDialog)
        self.lblAssetName.setObjectName(u"lblAssetName")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblAssetName)

        self.lblCategory = QLabel(AddAssetDialog)
        self.lblCategory.setObjectName(u"lblCategory")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblCategory)

        self.lblLocation = QLabel(AddAssetDialog)
        self.lblLocation.setObjectName(u"lblLocation")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lblLocation)

        self.lblManufacturer = QLabel(AddAssetDialog)
        self.lblManufacturer.setObjectName(u"lblManufacturer")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.lblManufacturer)

        self.lblModel = QLabel(AddAssetDialog)
        self.lblModel.setObjectName(u"lblModel")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.lblModel)

        self.lblSerialNumber = QLabel(AddAssetDialog)
        self.lblSerialNumber.setObjectName(u"lblSerialNumber")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.LabelRole, self.lblSerialNumber)

        self.lblPurchaseDate = QLabel(AddAssetDialog)
        self.lblPurchaseDate.setObjectName(u"lblPurchaseDate")

        self.formLayout.setWidget(14, QFormLayout.ItemRole.LabelRole, self.lblPurchaseDate)

        self.lblWarrantyExpiry = QLabel(AddAssetDialog)
        self.lblWarrantyExpiry.setObjectName(u"lblWarrantyExpiry")

        self.formLayout.setWidget(16, QFormLayout.ItemRole.LabelRole, self.lblWarrantyExpiry)

        self.lblStatus = QLabel(AddAssetDialog)
        self.lblStatus.setObjectName(u"lblStatus")

        self.formLayout.setWidget(18, QFormLayout.ItemRole.LabelRole, self.lblStatus)

        self.txtAssetNumber = QLineEdit(AddAssetDialog)
        self.txtAssetNumber.setObjectName(u"txtAssetNumber")
        self.txtAssetNumber.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtAssetNumber)

        self.txtAssetName = QLineEdit(AddAssetDialog)
        self.txtAssetName.setObjectName(u"txtAssetName")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtAssetName)

        self.cmbCategory = QComboBox(AddAssetDialog)
        self.cmbCategory.setObjectName(u"cmbCategory")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbCategory)

        self.cmbLocation = QComboBox(AddAssetDialog)
        self.cmbLocation.setObjectName(u"cmbLocation")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.cmbLocation)

        self.txtManufacturer = QLineEdit(AddAssetDialog)
        self.txtManufacturer.setObjectName(u"txtManufacturer")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.txtManufacturer)

        self.txtModel = QLineEdit(AddAssetDialog)
        self.txtModel.setObjectName(u"txtModel")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.txtModel)

        self.txtSerialNumber = QLineEdit(AddAssetDialog)
        self.txtSerialNumber.setObjectName(u"txtSerialNumber")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.FieldRole, self.txtSerialNumber)

        self.dtPurchaseDate = QDateEdit(AddAssetDialog)
        self.dtPurchaseDate.setObjectName(u"dtPurchaseDate")
        self.dtPurchaseDate.setCalendarPopup(True)

        self.formLayout.setWidget(14, QFormLayout.ItemRole.FieldRole, self.dtPurchaseDate)

        self.dtWarrantyExpiry = QDateEdit(AddAssetDialog)
        self.dtWarrantyExpiry.setObjectName(u"dtWarrantyExpiry")
        self.dtWarrantyExpiry.setCalendarPopup(True)

        self.formLayout.setWidget(16, QFormLayout.ItemRole.FieldRole, self.dtWarrantyExpiry)

        self.cmbStatus = QComboBox(AddAssetDialog)
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.formLayout.setWidget(18, QFormLayout.ItemRole.FieldRole, self.cmbStatus)

        self.buttonBox = QDialogButtonBox(AddAssetDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.formLayout.setWidget(19, QFormLayout.ItemRole.FieldRole, self.buttonBox)


        self.retranslateUi(AddAssetDialog)
        self.buttonBox.accepted.connect(AddAssetDialog.accept)
        self.buttonBox.rejected.connect(AddAssetDialog.reject)

        QMetaObject.connectSlotsByName(AddAssetDialog)
    # setupUi

    def retranslateUi(self, AddAssetDialog):
        AddAssetDialog.setWindowTitle(QCoreApplication.translate("AddAssetDialog", u"Add Asset", None))
        self.lblAssetNumber.setText(QCoreApplication.translate("AddAssetDialog", u"Asset Number", None))
        self.lblAssetName.setText(QCoreApplication.translate("AddAssetDialog", u"Asset Name", None))
        self.lblCategory.setText(QCoreApplication.translate("AddAssetDialog", u"Category", None))
        self.lblLocation.setText(QCoreApplication.translate("AddAssetDialog", u"Location", None))
        self.lblManufacturer.setText(QCoreApplication.translate("AddAssetDialog", u"Manufacturer", None))
        self.lblModel.setText(QCoreApplication.translate("AddAssetDialog", u"Model", None))
        self.lblSerialNumber.setText(QCoreApplication.translate("AddAssetDialog", u"Serial Number", None))
        self.lblPurchaseDate.setText(QCoreApplication.translate("AddAssetDialog", u"Purchase Date", None))
        self.lblWarrantyExpiry.setText(QCoreApplication.translate("AddAssetDialog", u"Warranty Expiry", None))
        self.lblStatus.setText(QCoreApplication.translate("AddAssetDialog", u"Status", None))
    # retranslateUi


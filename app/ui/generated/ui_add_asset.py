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
    QDialog, QDialogButtonBox, QDoubleSpinBox, QFormLayout,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_AddAssetDialog(object):
    def setupUi(self, AddAssetDialog):
        if not AddAssetDialog.objectName():
            AddAssetDialog.setObjectName(u"AddAssetDialog")
        AddAssetDialog.resize(649, 848)
        self.mainLayout = QVBoxLayout(AddAssetDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.groupGeneralInfo = QGroupBox(AddAssetDialog)
        self.groupGeneralInfo.setObjectName(u"groupGeneralInfo")
        self.groupGeneralInfo.setFlat(True)
        self.formGeneralInfo = QFormLayout(self.groupGeneralInfo)
        self.formGeneralInfo.setObjectName(u"formGeneralInfo")
        self.lblAssetCode = QLabel(self.groupGeneralInfo)
        self.lblAssetCode.setObjectName(u"lblAssetCode")

        self.formGeneralInfo.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblAssetCode)

        self.txtAssetCode = QLineEdit(self.groupGeneralInfo)
        self.txtAssetCode.setObjectName(u"txtAssetCode")
        self.txtAssetCode.setReadOnly(True)

        self.formGeneralInfo.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtAssetCode)

        self.lblAssetName = QLabel(self.groupGeneralInfo)
        self.lblAssetName.setObjectName(u"lblAssetName")

        self.formGeneralInfo.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblAssetName)

        self.txtAssetName = QLineEdit(self.groupGeneralInfo)
        self.txtAssetName.setObjectName(u"txtAssetName")

        self.formGeneralInfo.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtAssetName)

        self.lblDescription = QLabel(self.groupGeneralInfo)
        self.lblDescription.setObjectName(u"lblDescription")

        self.formGeneralInfo.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblDescription)

        self.txtDescription = QLineEdit(self.groupGeneralInfo)
        self.txtDescription.setObjectName(u"txtDescription")

        self.formGeneralInfo.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtDescription)

        self.lblCategory = QLabel(self.groupGeneralInfo)
        self.lblCategory.setObjectName(u"lblCategory")

        self.formGeneralInfo.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblCategory)

        self.cmbCategory = QComboBox(self.groupGeneralInfo)
        self.cmbCategory.setObjectName(u"cmbCategory")

        self.formGeneralInfo.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbCategory)

        self.lblStatus = QLabel(self.groupGeneralInfo)
        self.lblStatus.setObjectName(u"lblStatus")

        self.formGeneralInfo.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblStatus)

        self.cmbStatus = QComboBox(self.groupGeneralInfo)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.formGeneralInfo.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbStatus)


        self.mainLayout.addWidget(self.groupGeneralInfo)

        self.groupLocation = QGroupBox(AddAssetDialog)
        self.groupLocation.setObjectName(u"groupLocation")
        self.groupLocation.setFlat(True)
        self.formLocation = QFormLayout(self.groupLocation)
        self.formLocation.setObjectName(u"formLocation")
        self.lblLocation = QLabel(self.groupLocation)
        self.lblLocation.setObjectName(u"lblLocation")

        self.formLocation.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblLocation)

        self.cmbLocation = QComboBox(self.groupLocation)
        self.cmbLocation.setObjectName(u"cmbLocation")

        self.formLocation.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbLocation)


        self.mainLayout.addWidget(self.groupLocation)

        self.groupManufacturer = QGroupBox(AddAssetDialog)
        self.groupManufacturer.setObjectName(u"groupManufacturer")
        self.groupManufacturer.setFlat(True)
        self.formManufacturer = QFormLayout(self.groupManufacturer)
        self.formManufacturer.setObjectName(u"formManufacturer")
        self.lblManufacturer = QLabel(self.groupManufacturer)
        self.lblManufacturer.setObjectName(u"lblManufacturer")

        self.formManufacturer.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblManufacturer)

        self.txtManufacturer = QLineEdit(self.groupManufacturer)
        self.txtManufacturer.setObjectName(u"txtManufacturer")

        self.formManufacturer.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtManufacturer)

        self.lblModel = QLabel(self.groupManufacturer)
        self.lblModel.setObjectName(u"lblModel")

        self.formManufacturer.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblModel)

        self.txtModel = QLineEdit(self.groupManufacturer)
        self.txtModel.setObjectName(u"txtModel")

        self.formManufacturer.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtModel)

        self.lblSerialNumber = QLabel(self.groupManufacturer)
        self.lblSerialNumber.setObjectName(u"lblSerialNumber")

        self.formManufacturer.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblSerialNumber)

        self.txtSerialNumber = QLineEdit(self.groupManufacturer)
        self.txtSerialNumber.setObjectName(u"txtSerialNumber")

        self.formManufacturer.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtSerialNumber)


        self.mainLayout.addWidget(self.groupManufacturer)

        self.groupPurchaseInfo = QGroupBox(AddAssetDialog)
        self.groupPurchaseInfo.setObjectName(u"groupPurchaseInfo")
        self.groupPurchaseInfo.setFlat(True)
        self.gridLayout = QGridLayout(self.groupPurchaseInfo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblPurchaseDate = QLabel(self.groupPurchaseInfo)
        self.lblPurchaseDate.setObjectName(u"lblPurchaseDate")

        self.gridLayout.addWidget(self.lblPurchaseDate, 0, 0, 1, 1)

        self.dtPurchaseDate = QDateEdit(self.groupPurchaseInfo)
        self.dtPurchaseDate.setObjectName(u"dtPurchaseDate")
        self.dtPurchaseDate.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dtPurchaseDate, 0, 1, 1, 1)

        self.lblPurchaseCost = QLabel(self.groupPurchaseInfo)
        self.lblPurchaseCost.setObjectName(u"lblPurchaseCost")

        self.gridLayout.addWidget(self.lblPurchaseCost, 0, 2, 1, 1)

        self.dsbPurchaseCost = QDoubleSpinBox(self.groupPurchaseInfo)
        self.dsbPurchaseCost.setObjectName(u"dsbPurchaseCost")
        self.dsbPurchaseCost.setMaximum(999999.989999999990687)
        self.dsbPurchaseCost.setSingleStep(100.000000000000000)

        self.gridLayout.addWidget(self.dsbPurchaseCost, 0, 3, 1, 1)

        self.lblWarrantyExpiry = QLabel(self.groupPurchaseInfo)
        self.lblWarrantyExpiry.setObjectName(u"lblWarrantyExpiry")

        self.gridLayout.addWidget(self.lblWarrantyExpiry, 1, 0, 1, 1)

        self.dtWarrantyExpiry = QDateEdit(self.groupPurchaseInfo)
        self.dtWarrantyExpiry.setObjectName(u"dtWarrantyExpiry")
        self.dtWarrantyExpiry.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dtWarrantyExpiry, 1, 1, 1, 1)


        self.mainLayout.addWidget(self.groupPurchaseInfo)

        self.groupNotes = QGroupBox(AddAssetDialog)
        self.groupNotes.setObjectName(u"groupNotes")
        self.groupNotes.setFlat(True)
        self.layoutNotes = QVBoxLayout(self.groupNotes)
        self.layoutNotes.setObjectName(u"layoutNotes")
        self.txtNotes = QTextEdit(self.groupNotes)
        self.txtNotes.setObjectName(u"txtNotes")

        self.layoutNotes.addWidget(self.txtNotes)


        self.mainLayout.addWidget(self.groupNotes)

        self.buttonBox = QDialogButtonBox(AddAssetDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.mainLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddAssetDialog)

        QMetaObject.connectSlotsByName(AddAssetDialog)
    # setupUi

    def retranslateUi(self, AddAssetDialog):
        AddAssetDialog.setWindowTitle(QCoreApplication.translate("AddAssetDialog", u"Add Asset", None))
        self.groupGeneralInfo.setTitle(QCoreApplication.translate("AddAssetDialog", u"General Information", None))
        self.lblAssetCode.setText(QCoreApplication.translate("AddAssetDialog", u"Asset Code:", None))
        self.lblAssetName.setText(QCoreApplication.translate("AddAssetDialog", u"Asset Name:", None))
        self.lblDescription.setText(QCoreApplication.translate("AddAssetDialog", u"Description:", None))
        self.lblCategory.setText(QCoreApplication.translate("AddAssetDialog", u"Category:", None))
        self.lblStatus.setText(QCoreApplication.translate("AddAssetDialog", u"Status:", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("AddAssetDialog", u"Active", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("AddAssetDialog", u"Inactive", None))

        self.groupLocation.setTitle(QCoreApplication.translate("AddAssetDialog", u"Location", None))
        self.lblLocation.setText(QCoreApplication.translate("AddAssetDialog", u"Location:", None))
        self.groupManufacturer.setTitle(QCoreApplication.translate("AddAssetDialog", u"Manufacturer", None))
        self.lblManufacturer.setText(QCoreApplication.translate("AddAssetDialog", u"Manufacturer:", None))
        self.lblModel.setText(QCoreApplication.translate("AddAssetDialog", u"Model:", None))
        self.lblSerialNumber.setText(QCoreApplication.translate("AddAssetDialog", u"Serial Number:", None))
        self.groupPurchaseInfo.setTitle(QCoreApplication.translate("AddAssetDialog", u"Purchase Information", None))
        self.lblPurchaseDate.setText(QCoreApplication.translate("AddAssetDialog", u"Purchase Date:", None))
        self.lblPurchaseCost.setText(QCoreApplication.translate("AddAssetDialog", u"Purchase Cost:", None))
        self.dsbPurchaseCost.setPrefix(QCoreApplication.translate("AddAssetDialog", u"N$ ", None))
        self.lblWarrantyExpiry.setText(QCoreApplication.translate("AddAssetDialog", u"Warranty Expiry:", None))
        self.groupNotes.setTitle(QCoreApplication.translate("AddAssetDialog", u"Notes", None))
    # retranslateUi


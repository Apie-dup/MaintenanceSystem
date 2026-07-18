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
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_AddAssetDialog(object):
    def setupUi(self, AddAssetDialog):
        if not AddAssetDialog.objectName():
            AddAssetDialog.setObjectName(u"AddAssetDialog")
        AddAssetDialog.resize(600, 694)
        AddAssetDialog.setMinimumSize(QSize(600, 500))
        self.verticalLayout = QVBoxLayout(AddAssetDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblAssetNumber = QLabel(AddAssetDialog)
        self.lblAssetNumber.setObjectName(u"lblAssetNumber")

        self.horizontalLayout.addWidget(self.lblAssetNumber)

        self.txtAssetNumber = QLineEdit(AddAssetDialog)
        self.txtAssetNumber.setObjectName(u"txtAssetNumber")
        self.txtAssetNumber.setReadOnly(True)

        self.horizontalLayout.addWidget(self.txtAssetNumber)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblAssetName = QLabel(AddAssetDialog)
        self.lblAssetName.setObjectName(u"lblAssetName")

        self.horizontalLayout_2.addWidget(self.lblAssetName)

        self.txtAssetName = QLineEdit(AddAssetDialog)
        self.txtAssetName.setObjectName(u"txtAssetName")

        self.horizontalLayout_2.addWidget(self.txtAssetName)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblDescription = QLabel(AddAssetDialog)
        self.lblDescription.setObjectName(u"lblDescription")

        self.horizontalLayout_3.addWidget(self.lblDescription)

        self.teDescription = QTextEdit(AddAssetDialog)
        self.teDescription.setObjectName(u"teDescription")

        self.horizontalLayout_3.addWidget(self.teDescription)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblCategory = QLabel(AddAssetDialog)
        self.lblCategory.setObjectName(u"lblCategory")

        self.horizontalLayout_4.addWidget(self.lblCategory)

        self.cmbCategory = QComboBox(AddAssetDialog)
        self.cmbCategory.setObjectName(u"cmbCategory")

        self.horizontalLayout_4.addWidget(self.cmbCategory)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblLocation = QLabel(AddAssetDialog)
        self.lblLocation.setObjectName(u"lblLocation")

        self.horizontalLayout_5.addWidget(self.lblLocation)

        self.cmbLocation = QComboBox(AddAssetDialog)
        self.cmbLocation.setObjectName(u"cmbLocation")

        self.horizontalLayout_5.addWidget(self.cmbLocation)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblManufacturer = QLabel(AddAssetDialog)
        self.lblManufacturer.setObjectName(u"lblManufacturer")

        self.horizontalLayout_6.addWidget(self.lblManufacturer)

        self.txtManufacturer = QLineEdit(AddAssetDialog)
        self.txtManufacturer.setObjectName(u"txtManufacturer")

        self.horizontalLayout_6.addWidget(self.txtManufacturer)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lblModel = QLabel(AddAssetDialog)
        self.lblModel.setObjectName(u"lblModel")

        self.horizontalLayout_7.addWidget(self.lblModel)

        self.txtModel = QLineEdit(AddAssetDialog)
        self.txtModel.setObjectName(u"txtModel")

        self.horizontalLayout_7.addWidget(self.txtModel)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lblSerialNumber = QLabel(AddAssetDialog)
        self.lblSerialNumber.setObjectName(u"lblSerialNumber")

        self.horizontalLayout_8.addWidget(self.lblSerialNumber)

        self.txtSerialNumber = QLineEdit(AddAssetDialog)
        self.txtSerialNumber.setObjectName(u"txtSerialNumber")

        self.horizontalLayout_8.addWidget(self.txtSerialNumber)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lblPurchaseDate = QLabel(AddAssetDialog)
        self.lblPurchaseDate.setObjectName(u"lblPurchaseDate")

        self.horizontalLayout_9.addWidget(self.lblPurchaseDate)

        self.dtPurchaseDate = QDateEdit(AddAssetDialog)
        self.dtPurchaseDate.setObjectName(u"dtPurchaseDate")
        self.dtPurchaseDate.setCalendarPopup(True)

        self.horizontalLayout_9.addWidget(self.dtPurchaseDate)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lblWarrantyExpiry = QLabel(AddAssetDialog)
        self.lblWarrantyExpiry.setObjectName(u"lblWarrantyExpiry")

        self.horizontalLayout_10.addWidget(self.lblWarrantyExpiry)

        self.dtWarrantyExpiry = QDateEdit(AddAssetDialog)
        self.dtWarrantyExpiry.setObjectName(u"dtWarrantyExpiry")
        self.dtWarrantyExpiry.setCalendarPopup(True)

        self.horizontalLayout_10.addWidget(self.dtWarrantyExpiry)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lblStatus = QLabel(AddAssetDialog)
        self.lblStatus.setObjectName(u"lblStatus")

        self.horizontalLayout_11.addWidget(self.lblStatus)

        self.cmbStatus = QComboBox(AddAssetDialog)
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.horizontalLayout_11.addWidget(self.cmbStatus)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.buttonBox = QDialogButtonBox(AddAssetDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddAssetDialog)
        self.buttonBox.accepted.connect(AddAssetDialog.accept)
        self.buttonBox.rejected.connect(AddAssetDialog.reject)

        QMetaObject.connectSlotsByName(AddAssetDialog)
    # setupUi

    def retranslateUi(self, AddAssetDialog):
        AddAssetDialog.setWindowTitle(QCoreApplication.translate("AddAssetDialog", u"Add Asset", None))
        self.lblAssetNumber.setText(QCoreApplication.translate("AddAssetDialog", u"Asset Number", None))
        self.lblAssetName.setText(QCoreApplication.translate("AddAssetDialog", u"Asset Name", None))
        self.lblDescription.setText(QCoreApplication.translate("AddAssetDialog", u"Description", None))
        self.lblCategory.setText(QCoreApplication.translate("AddAssetDialog", u"Category", None))
        self.lblLocation.setText(QCoreApplication.translate("AddAssetDialog", u"Location", None))
        self.lblManufacturer.setText(QCoreApplication.translate("AddAssetDialog", u"Manufacturer", None))
        self.lblModel.setText(QCoreApplication.translate("AddAssetDialog", u"Model", None))
        self.lblSerialNumber.setText(QCoreApplication.translate("AddAssetDialog", u"Serial Number", None))
        self.lblPurchaseDate.setText(QCoreApplication.translate("AddAssetDialog", u"Purchase Date", None))
        self.lblWarrantyExpiry.setText(QCoreApplication.translate("AddAssetDialog", u"Warranty Expiry", None))
        self.lblStatus.setText(QCoreApplication.translate("AddAssetDialog", u"Status", None))
    # retranslateUi


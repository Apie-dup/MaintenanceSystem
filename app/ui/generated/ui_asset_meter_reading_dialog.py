# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asset_meter_reading_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QDoubleSpinBox, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_AssetMeterReadingDialog(object):
    def setupUi(self, AssetMeterReadingDialog):
        if not AssetMeterReadingDialog.objectName():
            AssetMeterReadingDialog.setObjectName(u"AssetMeterReadingDialog")
        AssetMeterReadingDialog.resize(442, 492)
        self.verticalLayout_2 = QVBoxLayout(AssetMeterReadingDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblTitle = QLabel(AssetMeterReadingDialog)
        self.lblTitle.setObjectName(u"lblTitle")

        self.verticalLayout_2.addWidget(self.lblTitle)

        self.lblAsset = QLabel(AssetMeterReadingDialog)
        self.lblAsset.setObjectName(u"lblAsset")

        self.verticalLayout_2.addWidget(self.lblAsset)

        self.groupBox = QGroupBox(AssetMeterReadingDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tblHistory = QTableWidget(self.groupBox)
        if (self.tblHistory.columnCount() < 4):
            self.tblHistory.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblHistory.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblHistory.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblHistory.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblHistory.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tblHistory.setObjectName(u"tblHistory")

        self.verticalLayout.addWidget(self.tblHistory)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupNewReading = QGroupBox(AssetMeterReadingDialog)
        self.groupNewReading.setObjectName(u"groupNewReading")
        self.verticalLayout_3 = QVBoxLayout(self.groupNewReading)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblMeterType = QLabel(self.groupNewReading)
        self.lblMeterType.setObjectName(u"lblMeterType")

        self.horizontalLayout_2.addWidget(self.lblMeterType)

        self.cmbMeterType = QComboBox(self.groupNewReading)
        self.cmbMeterType.addItem("")
        self.cmbMeterType.addItem("")
        self.cmbMeterType.addItem("")
        self.cmbMeterType.setObjectName(u"cmbMeterType")

        self.horizontalLayout_2.addWidget(self.cmbMeterType)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblReading = QLabel(self.groupNewReading)
        self.lblReading.setObjectName(u"lblReading")

        self.horizontalLayout_3.addWidget(self.lblReading)

        self.dsbReading = QDoubleSpinBox(self.groupNewReading)
        self.dsbReading.setObjectName(u"dsbReading")
        self.dsbReading.setMaximum(999999999.000000000000000)

        self.horizontalLayout_3.addWidget(self.dsbReading)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblReadingDate = QLabel(self.groupNewReading)
        self.lblReadingDate.setObjectName(u"lblReadingDate")

        self.horizontalLayout_4.addWidget(self.lblReadingDate)

        self.dtReadingDate = QDateEdit(self.groupNewReading)
        self.dtReadingDate.setObjectName(u"dtReadingDate")
        self.dtReadingDate.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dtReadingDate)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblNotes = QLabel(self.groupNewReading)
        self.lblNotes.setObjectName(u"lblNotes")

        self.horizontalLayout_5.addWidget(self.lblNotes)

        self.teNotes = QPlainTextEdit(self.groupNewReading)
        self.teNotes.setObjectName(u"teNotes")
        self.teNotes.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_5.addWidget(self.teNotes)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.groupNewReading)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnRecordReading = QPushButton(AssetMeterReadingDialog)
        self.btnRecordReading.setObjectName(u"btnRecordReading")

        self.horizontalLayout.addWidget(self.btnRecordReading)

        self.btnClose = QPushButton(AssetMeterReadingDialog)
        self.btnClose.setObjectName(u"btnClose")

        self.horizontalLayout.addWidget(self.btnClose)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(AssetMeterReadingDialog)

        QMetaObject.connectSlotsByName(AssetMeterReadingDialog)
    # setupUi

    def retranslateUi(self, AssetMeterReadingDialog):
        AssetMeterReadingDialog.setWindowTitle(QCoreApplication.translate("AssetMeterReadingDialog", u"Asset Meter Reading Dialog", None))
        self.lblTitle.setText(QCoreApplication.translate("AssetMeterReadingDialog", u"Asset Meter Readings", None))
        self.lblAsset.setText(QCoreApplication.translate("AssetMeterReadingDialog", u"Asset:", None))
        self.groupBox.setTitle(QCoreApplication.translate("AssetMeterReadingDialog", u"Meter Reading History", None))
        ___qtablewidgetitem = self.tblHistory.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AssetMeterReadingDialog", u"Reading Date", None))
        ___qtablewidgetitem1 = self.tblHistory.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AssetMeterReadingDialog", u"Meter Type", None))
        ___qtablewidgetitem2 = self.tblHistory.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AssetMeterReadingDialog", u"Reading", None))
        ___qtablewidgetitem3 = self.tblHistory.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AssetMeterReadingDialog", u"Notes", None))
        self.groupNewReading.setTitle(QCoreApplication.translate("AssetMeterReadingDialog", u"New Meter Reading", None))
        self.lblMeterType.setText(QCoreApplication.translate("AssetMeterReadingDialog", u"Meter Type:", None))
        self.cmbMeterType.setItemText(0, QCoreApplication.translate("AssetMeterReadingDialog", u"Running Hours", None))
        self.cmbMeterType.setItemText(1, QCoreApplication.translate("AssetMeterReadingDialog", u"Kilometers", None))
        self.cmbMeterType.setItemText(2, QCoreApplication.translate("AssetMeterReadingDialog", u"Cycles", None))

        self.lblReading.setText(QCoreApplication.translate("AssetMeterReadingDialog", u"Reading:", None))
        self.lblReadingDate.setText(QCoreApplication.translate("AssetMeterReadingDialog", u"Reading Date:", None))
        self.lblNotes.setText(QCoreApplication.translate("AssetMeterReadingDialog", u"Notes:", None))
        self.btnRecordReading.setText(QCoreApplication.translate("AssetMeterReadingDialog", u"Record Reading", None))
        self.btnClose.setText(QCoreApplication.translate("AssetMeterReadingDialog", u"Close", None))
    # retranslateUi


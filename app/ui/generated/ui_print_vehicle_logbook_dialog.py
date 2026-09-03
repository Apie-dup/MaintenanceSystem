# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'print_vehicle_logbook_dialog.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_PrintVehicleLogbookDialog(object):
    def setupUi(self, PrintVehicleLogbookDialog):
        if not PrintVehicleLogbookDialog.objectName():
            PrintVehicleLogbookDialog.setObjectName(u"PrintVehicleLogbookDialog")
        PrintVehicleLogbookDialog.resize(500, 270)
        self.verticalLayout = QVBoxLayout(PrintVehicleLogbookDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(PrintVehicleLogbookDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.verticalSpacer = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblVehicle = QLabel(PrintVehicleLogbookDialog)
        self.lblVehicle.setObjectName(u"lblVehicle")

        self.horizontalLayout.addWidget(self.lblVehicle)

        self.cmbVehicle = QComboBox(PrintVehicleLogbookDialog)
        self.cmbVehicle.setObjectName(u"cmbVehicle")

        self.horizontalLayout.addWidget(self.cmbVehicle)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 19, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblFromDate = QLabel(PrintVehicleLogbookDialog)
        self.lblFromDate.setObjectName(u"lblFromDate")

        self.horizontalLayout_2.addWidget(self.lblFromDate)

        self.dtFromDate = QDateEdit(PrintVehicleLogbookDialog)
        self.dtFromDate.setObjectName(u"dtFromDate")
        self.dtFromDate.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.dtFromDate)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblToDate = QLabel(PrintVehicleLogbookDialog)
        self.lblToDate.setObjectName(u"lblToDate")

        self.horizontalLayout_3.addWidget(self.lblToDate)

        self.dtToDate = QDateEdit(PrintVehicleLogbookDialog)
        self.dtToDate.setObjectName(u"dtToDate")
        self.dtToDate.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.dtToDate)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btnCancel = QPushButton(PrintVehicleLogbookDialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout_4.addWidget(self.btnCancel)

        self.btnCreatePdf = QPushButton(PrintVehicleLogbookDialog)
        self.btnCreatePdf.setObjectName(u"btnCreatePdf")

        self.horizontalLayout_4.addWidget(self.btnCreatePdf)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(PrintVehicleLogbookDialog)

        QMetaObject.connectSlotsByName(PrintVehicleLogbookDialog)
    # setupUi

    def retranslateUi(self, PrintVehicleLogbookDialog):
        PrintVehicleLogbookDialog.setWindowTitle(QCoreApplication.translate("PrintVehicleLogbookDialog", u"Print Vehicle Logbook Dialog", None))
        self.lblTitle.setText(QCoreApplication.translate("PrintVehicleLogbookDialog", u"Print Vehicle Logbook ", None))
        self.lblVehicle.setText(QCoreApplication.translate("PrintVehicleLogbookDialog", u"Vehicle:", None))
        self.lblFromDate.setText(QCoreApplication.translate("PrintVehicleLogbookDialog", u"From Date:", None))
        self.lblToDate.setText(QCoreApplication.translate("PrintVehicleLogbookDialog", u"To Date:", None))
        self.btnCancel.setText(QCoreApplication.translate("PrintVehicleLogbookDialog", u"Cancel", None))
        self.btnCreatePdf.setText(QCoreApplication.translate("PrintVehicleLogbookDialog", u"Create Pdf", None))
    # retranslateUi


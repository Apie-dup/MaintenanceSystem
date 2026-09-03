# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_vehicle_log.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_VehicleLogbookDialog(object):
    def setupUi(self, VehicleLogbookDialog):
        if not VehicleLogbookDialog.objectName():
            VehicleLogbookDialog.setObjectName(u"VehicleLogbookDialog")
        VehicleLogbookDialog.resize(518, 698)
        self.verticalLayout = QVBoxLayout(VehicleLogbookDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblVehicle = QLabel(VehicleLogbookDialog)
        self.lblVehicle.setObjectName(u"lblVehicle")

        self.horizontalLayout.addWidget(self.lblVehicle)

        self.txtVehicle = QLineEdit(VehicleLogbookDialog)
        self.txtVehicle.setObjectName(u"txtVehicle")

        self.horizontalLayout.addWidget(self.txtVehicle)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblDate = QLabel(VehicleLogbookDialog)
        self.lblDate.setObjectName(u"lblDate")

        self.horizontalLayout_2.addWidget(self.lblDate)

        self.dtLogDate = QDateEdit(VehicleLogbookDialog)
        self.dtLogDate.setObjectName(u"dtLogDate")
        self.dtLogDate.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.dtLogDate)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblDriver = QLabel(VehicleLogbookDialog)
        self.lblDriver.setObjectName(u"lblDriver")

        self.horizontalLayout_3.addWidget(self.lblDriver)

        self.txtDriver = QLineEdit(VehicleLogbookDialog)
        self.txtDriver.setObjectName(u"txtDriver")

        self.horizontalLayout_3.addWidget(self.txtDriver)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(VehicleLogbookDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.txtFrom = QLineEdit(VehicleLogbookDialog)
        self.txtFrom.setObjectName(u"txtFrom")

        self.horizontalLayout_4.addWidget(self.txtFrom)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblTo = QLabel(VehicleLogbookDialog)
        self.lblTo.setObjectName(u"lblTo")

        self.horizontalLayout_5.addWidget(self.lblTo)

        self.txtTo = QLineEdit(VehicleLogbookDialog)
        self.txtTo.setObjectName(u"txtTo")

        self.horizontalLayout_5.addWidget(self.txtTo)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblPurpose = QLabel(VehicleLogbookDialog)
        self.lblPurpose.setObjectName(u"lblPurpose")

        self.horizontalLayout_6.addWidget(self.lblPurpose)

        self.txtPurpose = QLineEdit(VehicleLogbookDialog)
        self.txtPurpose.setObjectName(u"txtPurpose")

        self.horizontalLayout_6.addWidget(self.txtPurpose)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lblStartMeter = QLabel(VehicleLogbookDialog)
        self.lblStartMeter.setObjectName(u"lblStartMeter")

        self.horizontalLayout_7.addWidget(self.lblStartMeter)

        self.dsbStartMeter = QDoubleSpinBox(VehicleLogbookDialog)
        self.dsbStartMeter.setObjectName(u"dsbStartMeter")
        self.dsbStartMeter.setDecimals(1)
        self.dsbStartMeter.setMaximum(9999999.000000000000000)

        self.horizontalLayout_7.addWidget(self.dsbStartMeter)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lblEndMeter = QLabel(VehicleLogbookDialog)
        self.lblEndMeter.setObjectName(u"lblEndMeter")

        self.horizontalLayout_8.addWidget(self.lblEndMeter)

        self.dsbEndMeter = QDoubleSpinBox(VehicleLogbookDialog)
        self.dsbEndMeter.setObjectName(u"dsbEndMeter")
        self.dsbEndMeter.setDecimals(1)
        self.dsbEndMeter.setMaximum(9999999.000000000000000)

        self.horizontalLayout_8.addWidget(self.dsbEndMeter)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lblDistance = QLabel(VehicleLogbookDialog)
        self.lblDistance.setObjectName(u"lblDistance")

        self.horizontalLayout_9.addWidget(self.lblDistance)

        self.dsbDistance = QDoubleSpinBox(VehicleLogbookDialog)
        self.dsbDistance.setObjectName(u"dsbDistance")
        self.dsbDistance.setReadOnly(True)
        self.dsbDistance.setDecimals(1)
        self.dsbDistance.setMaximum(9999999.000000000000000)

        self.horizontalLayout_9.addWidget(self.dsbDistance)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_5 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lblFeuleQuantity = QLabel(VehicleLogbookDialog)
        self.lblFeuleQuantity.setObjectName(u"lblFeuleQuantity")

        self.horizontalLayout_10.addWidget(self.lblFeuleQuantity)

        self.dsbFuelQuantity = QDoubleSpinBox(VehicleLogbookDialog)
        self.dsbFuelQuantity.setObjectName(u"dsbFuelQuantity")
        self.dsbFuelQuantity.setMaximum(9999999.000000000000000)

        self.horizontalLayout_10.addWidget(self.dsbFuelQuantity)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lblFuelCost = QLabel(VehicleLogbookDialog)
        self.lblFuelCost.setObjectName(u"lblFuelCost")

        self.horizontalLayout_11.addWidget(self.lblFuelCost)

        self.dsbFuelCost = QDoubleSpinBox(VehicleLogbookDialog)
        self.dsbFuelCost.setObjectName(u"dsbFuelCost")

        self.horizontalLayout_11.addWidget(self.dsbFuelCost)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_6 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lblNotes = QLabel(VehicleLogbookDialog)
        self.lblNotes.setObjectName(u"lblNotes")

        self.horizontalLayout_12.addWidget(self.lblNotes)

        self.plainTextEdit = QPlainTextEdit(VehicleLogbookDialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout_12.addWidget(self.plainTextEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.buttonBox = QDialogButtonBox(VehicleLogbookDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(VehicleLogbookDialog)
        self.buttonBox.accepted.connect(VehicleLogbookDialog.accept)
        self.buttonBox.rejected.connect(VehicleLogbookDialog.reject)

        QMetaObject.connectSlotsByName(VehicleLogbookDialog)
    # setupUi

    def retranslateUi(self, VehicleLogbookDialog):
        VehicleLogbookDialog.setWindowTitle(QCoreApplication.translate("VehicleLogbookDialog", u"Vehicle Logbook", None))
        self.lblVehicle.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Vehicle:", None))
        self.lblDate.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Date:", None))
        self.lblDriver.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Driver:", None))
        self.label.setText(QCoreApplication.translate("VehicleLogbookDialog", u"From:", None))
        self.lblTo.setText(QCoreApplication.translate("VehicleLogbookDialog", u"To:", None))
        self.lblPurpose.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Purpose:", None))
        self.lblStartMeter.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Start km:", None))
        self.lblEndMeter.setText(QCoreApplication.translate("VehicleLogbookDialog", u"End kim:", None))
        self.lblDistance.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Distance:", None))
        self.lblFeuleQuantity.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Fuel Qty:", None))
        self.lblFuelCost.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Fuel Cost:", None))
        self.lblNotes.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Notes:", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehicle_logbook_dialog.ui'
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
    QDialog, QDialogButtonBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_VehicleLogbookDialog(object):
    def setupUi(self, VehicleLogbookDialog):
        if not VehicleLogbookDialog.objectName():
            VehicleLogbookDialog.setObjectName(u"VehicleLogbookDialog")
        VehicleLogbookDialog.resize(518, 684)
        self.verticalLayout = QVBoxLayout(VehicleLogbookDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblVehicle = QLabel(VehicleLogbookDialog)
        self.lblVehicle.setObjectName(u"lblVehicle")

        self.horizontalLayout.addWidget(self.lblVehicle)

        self.cmbAsset = QComboBox(VehicleLogbookDialog)
        self.cmbAsset.setObjectName(u"cmbAsset")

        self.horizontalLayout.addWidget(self.cmbAsset)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblPurpose = QLabel(VehicleLogbookDialog)
        self.lblPurpose.setObjectName(u"lblPurpose")

        self.horizontalLayout_6.addWidget(self.lblPurpose)

        self.txtPurpose = QLineEdit(VehicleLogbookDialog)
        self.txtPurpose.setObjectName(u"txtPurpose")

        self.horizontalLayout_6.addWidget(self.txtPurpose)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lblDefectFaultRepoted = QLabel(VehicleLogbookDialog)
        self.lblDefectFaultRepoted.setObjectName(u"lblDefectFaultRepoted")

        self.horizontalLayout_13.addWidget(self.lblDefectFaultRepoted)

        self.teDefectReported = QPlainTextEdit(VehicleLogbookDialog)
        self.teDefectReported.setObjectName(u"teDefectReported")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teDefectReported.sizePolicy().hasHeightForWidth())
        self.teDefectReported.setSizePolicy(sizePolicy)
        self.teDefectReported.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_13.addWidget(self.teDefectReported)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.groupReadings = QGroupBox(VehicleLogbookDialog)
        self.groupReadings.setObjectName(u"groupReadings")
        self.gridLayout = QGridLayout(self.groupReadings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lblStartMeter = QLabel(self.groupReadings)
        self.lblStartMeter.setObjectName(u"lblStartMeter")

        self.horizontalLayout_7.addWidget(self.lblStartMeter)

        self.dsbStartMeter = QDoubleSpinBox(self.groupReadings)
        self.dsbStartMeter.setObjectName(u"dsbStartMeter")
        self.dsbStartMeter.setDecimals(1)
        self.dsbStartMeter.setMaximum(9999999.000000000000000)

        self.horizontalLayout_7.addWidget(self.dsbStartMeter)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lblStartHours = QLabel(self.groupReadings)
        self.lblStartHours.setObjectName(u"lblStartHours")

        self.horizontalLayout_14.addWidget(self.lblStartHours)

        self.dsbStartHours = QDoubleSpinBox(self.groupReadings)
        self.dsbStartHours.setObjectName(u"dsbStartHours")
        self.dsbStartHours.setMaximum(999999999.990000009536743)

        self.horizontalLayout_14.addWidget(self.dsbStartHours)


        self.gridLayout.addLayout(self.horizontalLayout_14, 0, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lblEndMeter = QLabel(self.groupReadings)
        self.lblEndMeter.setObjectName(u"lblEndMeter")

        self.horizontalLayout_8.addWidget(self.lblEndMeter)

        self.dsbEndMeter = QDoubleSpinBox(self.groupReadings)
        self.dsbEndMeter.setObjectName(u"dsbEndMeter")
        self.dsbEndMeter.setDecimals(1)
        self.dsbEndMeter.setMaximum(9999999.000000000000000)

        self.horizontalLayout_8.addWidget(self.dsbEndMeter)


        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lblEndHours = QLabel(self.groupReadings)
        self.lblEndHours.setObjectName(u"lblEndHours")

        self.horizontalLayout_15.addWidget(self.lblEndHours)

        self.dsbEndHours = QDoubleSpinBox(self.groupReadings)
        self.dsbEndHours.setObjectName(u"dsbEndHours")
        self.dsbEndHours.setMaximum(999999999.990000009536743)

        self.horizontalLayout_15.addWidget(self.dsbEndHours)


        self.gridLayout.addLayout(self.horizontalLayout_15, 1, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lblDistance = QLabel(self.groupReadings)
        self.lblDistance.setObjectName(u"lblDistance")

        self.horizontalLayout_9.addWidget(self.lblDistance)

        self.dsbDistance = QDoubleSpinBox(self.groupReadings)
        self.dsbDistance.setObjectName(u"dsbDistance")
        self.dsbDistance.setReadOnly(True)
        self.dsbDistance.setDecimals(1)
        self.dsbDistance.setMaximum(9999999.000000000000000)

        self.horizontalLayout_9.addWidget(self.dsbDistance)


        self.gridLayout.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lblHoursUsed = QLabel(self.groupReadings)
        self.lblHoursUsed.setObjectName(u"lblHoursUsed")

        self.horizontalLayout_16.addWidget(self.lblHoursUsed)

        self.dsbHoursUsed = QDoubleSpinBox(self.groupReadings)
        self.dsbHoursUsed.setObjectName(u"dsbHoursUsed")
        self.dsbHoursUsed.setReadOnly(True)
        self.dsbHoursUsed.setMaximum(999999999.990000009536743)

        self.horizontalLayout_16.addWidget(self.dsbHoursUsed)


        self.gridLayout.addLayout(self.horizontalLayout_16, 2, 1, 2, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lblFuelQuantity = QLabel(self.groupReadings)
        self.lblFuelQuantity.setObjectName(u"lblFuelQuantity")

        self.horizontalLayout_10.addWidget(self.lblFuelQuantity)

        self.dsbFuelQuantity = QDoubleSpinBox(self.groupReadings)
        self.dsbFuelQuantity.setObjectName(u"dsbFuelQuantity")
        self.dsbFuelQuantity.setMaximum(9999999.000000000000000)

        self.horizontalLayout_10.addWidget(self.dsbFuelQuantity)


        self.gridLayout.addLayout(self.horizontalLayout_10, 3, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lblFuelCost = QLabel(self.groupReadings)
        self.lblFuelCost.setObjectName(u"lblFuelCost")

        self.horizontalLayout_11.addWidget(self.lblFuelCost)

        self.dsbFuelCost = QDoubleSpinBox(self.groupReadings)
        self.dsbFuelCost.setObjectName(u"dsbFuelCost")
        self.dsbFuelCost.setMaximum(9999999.000000000000000)

        self.horizontalLayout_11.addWidget(self.dsbFuelCost)


        self.gridLayout.addLayout(self.horizontalLayout_11, 4, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupReadings)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lblNotes = QLabel(VehicleLogbookDialog)
        self.lblNotes.setObjectName(u"lblNotes")

        self.horizontalLayout_12.addWidget(self.lblNotes)

        self.txtNotes = QPlainTextEdit(VehicleLogbookDialog)
        self.txtNotes.setObjectName(u"txtNotes")
        sizePolicy.setHeightForWidth(self.txtNotes.sizePolicy().hasHeightForWidth())
        self.txtNotes.setSizePolicy(sizePolicy)
        self.txtNotes.setMinimumSize(QSize(0, 80))

        self.horizontalLayout_12.addWidget(self.txtNotes)


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
        self.lblDefectFaultRepoted.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Defect / Fault Reported:", None))
        self.groupReadings.setTitle(QCoreApplication.translate("VehicleLogbookDialog", u"Readings", None))
        self.lblStartMeter.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Start km:", None))
        self.lblStartHours.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Start Hours:", None))
        self.lblEndMeter.setText(QCoreApplication.translate("VehicleLogbookDialog", u"End km:", None))
        self.lblEndHours.setText(QCoreApplication.translate("VehicleLogbookDialog", u"End Hours:", None))
        self.lblDistance.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Distance:", None))
        self.lblHoursUsed.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Hours Used:", None))
        self.lblFuelQuantity.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Fuel Qty:", None))
        self.lblFuelCost.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Fuel Cost:", None))
        self.lblNotes.setText(QCoreApplication.translate("VehicleLogbookDialog", u"Notes:", None))
    # retranslateUi


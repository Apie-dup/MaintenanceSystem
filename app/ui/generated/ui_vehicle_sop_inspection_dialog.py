# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehicle_sop_inspection_dialog.ui'
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
    QDialog, QDialogButtonBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_VehicleSopInspectionDialog(object):
    def setupUi(self, VehicleSopInspectionDialog):
        if not VehicleSopInspectionDialog.objectName():
            VehicleSopInspectionDialog.setObjectName(u"VehicleSopInspectionDialog")
        VehicleSopInspectionDialog.resize(545, 740)
        self.verticalLayout_3 = QVBoxLayout(VehicleSopInspectionDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupInspectionDetails = QGroupBox(VehicleSopInspectionDialog)
        self.groupInspectionDetails.setObjectName(u"groupInspectionDetails")
        self.gridLayout = QGridLayout(self.groupInspectionDetails)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblInspectionNumber = QLabel(self.groupInspectionDetails)
        self.lblInspectionNumber.setObjectName(u"lblInspectionNumber")

        self.horizontalLayout.addWidget(self.lblInspectionNumber)

        self.txtInspectionNumber = QLineEdit(self.groupInspectionDetails)
        self.txtInspectionNumber.setObjectName(u"txtInspectionNumber")
        self.txtInspectionNumber.setReadOnly(True)

        self.horizontalLayout.addWidget(self.txtInspectionNumber)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblSOP = QLabel(self.groupInspectionDetails)
        self.lblSOP.setObjectName(u"lblSOP")

        self.horizontalLayout_2.addWidget(self.lblSOP)

        self.cmbSop = QComboBox(self.groupInspectionDetails)
        self.cmbSop.setObjectName(u"cmbSop")

        self.horizontalLayout_2.addWidget(self.cmbSop)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblAsset = QLabel(self.groupInspectionDetails)
        self.lblAsset.setObjectName(u"lblAsset")

        self.horizontalLayout_3.addWidget(self.lblAsset)

        self.txtAsset = QLineEdit(self.groupInspectionDetails)
        self.txtAsset.setObjectName(u"txtAsset")
        self.txtAsset.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.txtAsset)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblFrequency = QLabel(self.groupInspectionDetails)
        self.lblFrequency.setObjectName(u"lblFrequency")

        self.horizontalLayout_4.addWidget(self.lblFrequency)

        self.txtFrequency = QLineEdit(self.groupInspectionDetails)
        self.txtFrequency.setObjectName(u"txtFrequency")
        self.txtFrequency.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.txtFrequency)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblDate = QLabel(self.groupInspectionDetails)
        self.lblDate.setObjectName(u"lblDate")

        self.horizontalLayout_5.addWidget(self.lblDate)

        self.dtInspectionDate = QDateEdit(self.groupInspectionDetails)
        self.dtInspectionDate.setObjectName(u"dtInspectionDate")
        self.dtInspectionDate.setCalendarPopup(True)

        self.horizontalLayout_5.addWidget(self.dtInspectionDate)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblOperator = QLabel(self.groupInspectionDetails)
        self.lblOperator.setObjectName(u"lblOperator")

        self.horizontalLayout_6.addWidget(self.lblOperator)

        self.txtOperator = QLineEdit(self.groupInspectionDetails)
        self.txtOperator.setObjectName(u"txtOperator")

        self.horizontalLayout_6.addWidget(self.txtOperator)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lblMeterType = QLabel(self.groupInspectionDetails)
        self.lblMeterType.setObjectName(u"lblMeterType")

        self.horizontalLayout_7.addWidget(self.lblMeterType)

        self.cmbMeterType = QComboBox(self.groupInspectionDetails)
        self.cmbMeterType.setObjectName(u"cmbMeterType")

        self.horizontalLayout_7.addWidget(self.cmbMeterType)


        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lblMeterReading = QLabel(self.groupInspectionDetails)
        self.lblMeterReading.setObjectName(u"lblMeterReading")

        self.horizontalLayout_8.addWidget(self.lblMeterReading)

        self.spnMeterReading = QSpinBox(self.groupInspectionDetails)
        self.spnMeterReading.setObjectName(u"spnMeterReading")
        self.spnMeterReading.setMaximum(999999999)

        self.horizontalLayout_8.addWidget(self.spnMeterReading)


        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupInspectionDetails)

        self.groupCheclist = QGroupBox(VehicleSopInspectionDialog)
        self.groupCheclist.setObjectName(u"groupCheclist")
        self.verticalLayout_2 = QVBoxLayout(self.groupCheclist)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tblChecklist = QTableWidget(self.groupCheclist)
        if (self.tblChecklist.columnCount() < 4):
            self.tblChecklist.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblChecklist.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblChecklist.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblChecklist.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblChecklist.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tblChecklist.setObjectName(u"tblChecklist")

        self.verticalLayout_2.addWidget(self.tblChecklist)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btnSetResult = QPushButton(self.groupCheclist)
        self.btnSetResult.setObjectName(u"btnSetResult")

        self.horizontalLayout_9.addWidget(self.btnSetResult)

        self.btnCreateWorkOrder = QPushButton(self.groupCheclist)
        self.btnCreateWorkOrder.setObjectName(u"btnCreateWorkOrder")

        self.horizontalLayout_9.addWidget(self.btnCreateWorkOrder)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.verticalLayout_3.addWidget(self.groupCheclist)

        self.groupBox = QGroupBox(VehicleSopInspectionDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txtComments = QPlainTextEdit(self.groupBox)
        self.txtComments.setObjectName(u"txtComments")
        self.txtComments.setMinimumSize(QSize(0, 90))

        self.verticalLayout.addWidget(self.txtComments)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btnComplete = QPushButton(VehicleSopInspectionDialog)
        self.btnComplete.setObjectName(u"btnComplete")

        self.horizontalLayout_10.addWidget(self.btnComplete)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.buttonBox = QDialogButtonBox(VehicleSopInspectionDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.horizontalLayout_10.addWidget(self.buttonBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)


        self.retranslateUi(VehicleSopInspectionDialog)
        self.buttonBox.accepted.connect(VehicleSopInspectionDialog.accept)
        self.buttonBox.rejected.connect(VehicleSopInspectionDialog.reject)

        QMetaObject.connectSlotsByName(VehicleSopInspectionDialog)
    # setupUi

    def retranslateUi(self, VehicleSopInspectionDialog):
        VehicleSopInspectionDialog.setWindowTitle(QCoreApplication.translate("VehicleSopInspectionDialog", u"Vehicle Sop Inspection Dialog", None))
        self.groupInspectionDetails.setTitle(QCoreApplication.translate("VehicleSopInspectionDialog", u"Inspection Details ", None))
        self.lblInspectionNumber.setText(QCoreApplication.translate("VehicleSopInspectionDialog", u"Inspection Number:", None))
        self.lblSOP.setText(QCoreApplication.translate("VehicleSopInspectionDialog", u"SOP:", None))
        self.lblAsset.setText(QCoreApplication.translate("VehicleSopInspectionDialog", u"Asset:", None))
        self.lblFrequency.setText(QCoreApplication.translate("VehicleSopInspectionDialog", u"Frequency:", None))
        self.lblDate.setText(QCoreApplication.translate("VehicleSopInspectionDialog", u"Inspection Date:", None))
        self.dtInspectionDate.setDisplayFormat(QCoreApplication.translate("VehicleSopInspectionDialog", u"yyyy-MM-dd", None))
        self.lblOperator.setText(QCoreApplication.translate("VehicleSopInspectionDialog", u"Operator:", None))
        self.lblMeterType.setText(QCoreApplication.translate("VehicleSopInspectionDialog", u"Meter Type:", None))
        self.lblMeterReading.setText(QCoreApplication.translate("VehicleSopInspectionDialog", u"Meter Reading:", None))
        self.groupCheclist.setTitle(QCoreApplication.translate("VehicleSopInspectionDialog", u"Checklist", None))
        ___qtablewidgetitem = self.tblChecklist.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VehicleSopInspectionDialog", u"Seq.", None))
        ___qtablewidgetitem1 = self.tblChecklist.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VehicleSopInspectionDialog", u"Check Description", None))
        ___qtablewidgetitem2 = self.tblChecklist.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VehicleSopInspectionDialog", u"Required", None))
        ___qtablewidgetitem3 = self.tblChecklist.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VehicleSopInspectionDialog", u"Result", None))
        self.btnSetResult.setText(QCoreApplication.translate("VehicleSopInspectionDialog", u"Set Result", None))
        self.btnCreateWorkOrder.setText(QCoreApplication.translate("VehicleSopInspectionDialog", u"Create Work Order", None))
        self.groupBox.setTitle(QCoreApplication.translate("VehicleSopInspectionDialog", u"Coments", None))
        self.btnComplete.setText(QCoreApplication.translate("VehicleSopInspectionDialog", u"Complete Inspection", None))
    # retranslateUi


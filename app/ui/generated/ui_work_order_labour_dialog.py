# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'work_order_labour_dialog.ui'
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
    QDialog, QDialogButtonBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_WorkOrderLabourDialog(object):
    def setupUi(self, WorkOrderLabourDialog):
        if not WorkOrderLabourDialog.objectName():
            WorkOrderLabourDialog.setObjectName(u"WorkOrderLabourDialog")
        WorkOrderLabourDialog.resize(639, 649)
        self.verticalLayout = QVBoxLayout(WorkOrderLabourDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(WorkOrderLabourDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblTechnician = QLabel(WorkOrderLabourDialog)
        self.lblTechnician.setObjectName(u"lblTechnician")

        self.horizontalLayout.addWidget(self.lblTechnician)

        self.cmbTechnician = QComboBox(WorkOrderLabourDialog)
        self.cmbTechnician.setObjectName(u"cmbTechnician")

        self.horizontalLayout.addWidget(self.cmbTechnician)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblWorkDate = QLabel(WorkOrderLabourDialog)
        self.lblWorkDate.setObjectName(u"lblWorkDate")

        self.horizontalLayout_2.addWidget(self.lblWorkDate)

        self.dtWorkDate = QDateEdit(WorkOrderLabourDialog)
        self.dtWorkDate.setObjectName(u"dtWorkDate")
        self.dtWorkDate.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.dtWorkDate)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblHours = QLabel(WorkOrderLabourDialog)
        self.lblHours.setObjectName(u"lblHours")

        self.horizontalLayout_3.addWidget(self.lblHours)

        self.dsbHours = QDoubleSpinBox(WorkOrderLabourDialog)
        self.dsbHours.setObjectName(u"dsbHours")
        self.dsbHours.setMaximum(9999.000000000000000)
        self.dsbHours.setSingleStep(0.250000000000000)

        self.horizontalLayout_3.addWidget(self.dsbHours)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblHourluRate = QLabel(WorkOrderLabourDialog)
        self.lblHourluRate.setObjectName(u"lblHourluRate")

        self.horizontalLayout_4.addWidget(self.lblHourluRate)

        self.dsbHourlyRate = QDoubleSpinBox(WorkOrderLabourDialog)
        self.dsbHourlyRate.setObjectName(u"dsbHourlyRate")
        self.dsbHourlyRate.setMaximum(999999.989999999990687)

        self.horizontalLayout_4.addWidget(self.dsbHourlyRate)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblLabourCost = QLabel(WorkOrderLabourDialog)
        self.lblLabourCost.setObjectName(u"lblLabourCost")

        self.horizontalLayout_5.addWidget(self.lblLabourCost)

        self.txtLabourCost = QLineEdit(WorkOrderLabourDialog)
        self.txtLabourCost.setObjectName(u"txtLabourCost")
        self.txtLabourCost.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.txtLabourCost)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblDescription = QLabel(WorkOrderLabourDialog)
        self.lblDescription.setObjectName(u"lblDescription")

        self.horizontalLayout_6.addWidget(self.lblDescription)

        self.txtDescription = QLineEdit(WorkOrderLabourDialog)
        self.txtDescription.setObjectName(u"txtDescription")

        self.horizontalLayout_6.addWidget(self.txtDescription)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lblNotes = QLabel(WorkOrderLabourDialog)
        self.lblNotes.setObjectName(u"lblNotes")

        self.horizontalLayout_7.addWidget(self.lblNotes)

        self.txtNotes = QPlainTextEdit(WorkOrderLabourDialog)
        self.txtNotes.setObjectName(u"txtNotes")

        self.horizontalLayout_7.addWidget(self.txtNotes)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.buttonBox = QDialogButtonBox(WorkOrderLabourDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(WorkOrderLabourDialog)
        self.buttonBox.accepted.connect(WorkOrderLabourDialog.accept)
        self.buttonBox.rejected.connect(WorkOrderLabourDialog.reject)

        QMetaObject.connectSlotsByName(WorkOrderLabourDialog)
    # setupUi

    def retranslateUi(self, WorkOrderLabourDialog):
        WorkOrderLabourDialog.setWindowTitle(QCoreApplication.translate("WorkOrderLabourDialog", u" Add Labour", None))
        self.lblTitle.setText(QCoreApplication.translate("WorkOrderLabourDialog", u" Add Labour", None))
        self.lblTechnician.setText(QCoreApplication.translate("WorkOrderLabourDialog", u"Technician:", None))
        self.lblWorkDate.setText(QCoreApplication.translate("WorkOrderLabourDialog", u"Work Date:", None))
        self.lblHours.setText(QCoreApplication.translate("WorkOrderLabourDialog", u"Hours:", None))
        self.lblHourluRate.setText(QCoreApplication.translate("WorkOrderLabourDialog", u"Hourly Rate:", None))
        self.lblLabourCost.setText(QCoreApplication.translate("WorkOrderLabourDialog", u"Labour Cost:", None))
        self.lblDescription.setText(QCoreApplication.translate("WorkOrderLabourDialog", u"Description:", None))
        self.lblNotes.setText(QCoreApplication.translate("WorkOrderLabourDialog", u"Notes:", None))
    # retranslateUi


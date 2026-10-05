# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehicle_sop_inspection_result_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QPlainTextEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_VehicleSopInspectionResultDialog(object):
    def setupUi(self, VehicleSopInspectionResultDialog):
        if not VehicleSopInspectionResultDialog.objectName():
            VehicleSopInspectionResultDialog.setObjectName(u"VehicleSopInspectionResultDialog")
        VehicleSopInspectionResultDialog.resize(400, 354)
        self.verticalLayout = QVBoxLayout(VehicleSopInspectionResultDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(VehicleSopInspectionResultDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.lblCheck = QLabel(VehicleSopInspectionResultDialog)
        self.lblCheck.setObjectName(u"lblCheck")

        self.verticalLayout.addWidget(self.lblCheck)

        self.lblCheckDescription = QLabel(VehicleSopInspectionResultDialog)
        self.lblCheckDescription.setObjectName(u"lblCheckDescription")

        self.verticalLayout.addWidget(self.lblCheckDescription)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblResult = QLabel(VehicleSopInspectionResultDialog)
        self.lblResult.setObjectName(u"lblResult")

        self.horizontalLayout.addWidget(self.lblResult)

        self.cmbResult = QComboBox(VehicleSopInspectionResultDialog)
        self.cmbResult.setObjectName(u"cmbResult")

        self.horizontalLayout.addWidget(self.cmbResult)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lblComments = QLabel(VehicleSopInspectionResultDialog)
        self.lblComments.setObjectName(u"lblComments")

        self.verticalLayout.addWidget(self.lblComments)

        self.txtComments = QPlainTextEdit(VehicleSopInspectionResultDialog)
        self.txtComments.setObjectName(u"txtComments")

        self.verticalLayout.addWidget(self.txtComments)

        self.buttonBox = QDialogButtonBox(VehicleSopInspectionResultDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(VehicleSopInspectionResultDialog)
        self.buttonBox.accepted.connect(VehicleSopInspectionResultDialog.accept)
        self.buttonBox.rejected.connect(VehicleSopInspectionResultDialog.reject)

        QMetaObject.connectSlotsByName(VehicleSopInspectionResultDialog)
    # setupUi

    def retranslateUi(self, VehicleSopInspectionResultDialog):
        VehicleSopInspectionResultDialog.setWindowTitle(QCoreApplication.translate("VehicleSopInspectionResultDialog", u"Vehicle Sop Inspection Result", None))
        self.lblTitle.setText(QCoreApplication.translate("VehicleSopInspectionResultDialog", u"Checklist Result   ", None))
        self.lblCheck.setText(QCoreApplication.translate("VehicleSopInspectionResultDialog", u"Check:", None))
        self.lblCheckDescription.setText("")
        self.lblResult.setText(QCoreApplication.translate("VehicleSopInspectionResultDialog", u"Result:", None))
        self.lblComments.setText(QCoreApplication.translate("VehicleSopInspectionResultDialog", u"Comments:", None))
    # retranslateUi


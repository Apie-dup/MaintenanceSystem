# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehicle_sop_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_VehicleSopDialog(object):
    def setupUi(self, VehicleSopDialog):
        if not VehicleSopDialog.objectName():
            VehicleSopDialog.setObjectName(u"VehicleSopDialog")
        VehicleSopDialog.resize(435, 494)
        self.verticalLayout = QVBoxLayout(VehicleSopDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(VehicleSopDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSOPNumber = QLabel(VehicleSopDialog)
        self.lblSOPNumber.setObjectName(u"lblSOPNumber")

        self.horizontalLayout.addWidget(self.lblSOPNumber)

        self.txtSopNumber = QLineEdit(VehicleSopDialog)
        self.txtSopNumber.setObjectName(u"txtSopNumber")
        self.txtSopNumber.setReadOnly(True)

        self.horizontalLayout.addWidget(self.txtSopNumber)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblVehicleAsset = QLabel(VehicleSopDialog)
        self.lblVehicleAsset.setObjectName(u"lblVehicleAsset")

        self.horizontalLayout_2.addWidget(self.lblVehicleAsset)

        self.cmbAsset = QComboBox(VehicleSopDialog)
        self.cmbAsset.setObjectName(u"cmbAsset")

        self.horizontalLayout_2.addWidget(self.cmbAsset)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblSOPName = QLabel(VehicleSopDialog)
        self.lblSOPName.setObjectName(u"lblSOPName")

        self.horizontalLayout_3.addWidget(self.lblSOPName)

        self.txtSopName = QLineEdit(VehicleSopDialog)
        self.txtSopName.setObjectName(u"txtSopName")

        self.horizontalLayout_3.addWidget(self.txtSopName)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblFrequency = QLabel(VehicleSopDialog)
        self.lblFrequency.setObjectName(u"lblFrequency")

        self.horizontalLayout_4.addWidget(self.lblFrequency)

        self.cmbFrequency = QComboBox(VehicleSopDialog)
        self.cmbFrequency.setObjectName(u"cmbFrequency")

        self.horizontalLayout_4.addWidget(self.cmbFrequency)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblActive = QLabel(VehicleSopDialog)
        self.lblActive.setObjectName(u"lblActive")

        self.horizontalLayout_5.addWidget(self.lblActive)

        self.chkActive = QCheckBox(VehicleSopDialog)
        self.chkActive.setObjectName(u"chkActive")

        self.horizontalLayout_5.addWidget(self.chkActive)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.lblDescription = QLabel(VehicleSopDialog)
        self.lblDescription.setObjectName(u"lblDescription")

        self.verticalLayout.addWidget(self.lblDescription)

        self.txtDescription = QPlainTextEdit(VehicleSopDialog)
        self.txtDescription.setObjectName(u"txtDescription")

        self.verticalLayout.addWidget(self.txtDescription)

        self.lblNotes = QLabel(VehicleSopDialog)
        self.lblNotes.setObjectName(u"lblNotes")

        self.verticalLayout.addWidget(self.lblNotes)

        self.txtNotes = QPlainTextEdit(VehicleSopDialog)
        self.txtNotes.setObjectName(u"txtNotes")

        self.verticalLayout.addWidget(self.txtNotes)

        self.buttonBox = QDialogButtonBox(VehicleSopDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(VehicleSopDialog)
        self.buttonBox.accepted.connect(VehicleSopDialog.accept)
        self.buttonBox.rejected.connect(VehicleSopDialog.reject)

        QMetaObject.connectSlotsByName(VehicleSopDialog)
    # setupUi

    def retranslateUi(self, VehicleSopDialog):
        VehicleSopDialog.setWindowTitle(QCoreApplication.translate("VehicleSopDialog", u"Vehicle SOP", None))
        self.lblTitle.setText(QCoreApplication.translate("VehicleSopDialog", u"Vehicle SOP", None))
        self.lblSOPNumber.setText(QCoreApplication.translate("VehicleSopDialog", u"SOP Number:", None))
        self.lblVehicleAsset.setText(QCoreApplication.translate("VehicleSopDialog", u"Vehicle / Asset:", None))
        self.lblSOPName.setText(QCoreApplication.translate("VehicleSopDialog", u"SOP Name:", None))
        self.lblFrequency.setText(QCoreApplication.translate("VehicleSopDialog", u"Frequency:", None))
        self.lblActive.setText(QCoreApplication.translate("VehicleSopDialog", u"Active:", None))
        self.chkActive.setText("")
        self.lblDescription.setText(QCoreApplication.translate("VehicleSopDialog", u"Description:", None))
        self.lblNotes.setText(QCoreApplication.translate("VehicleSopDialog", u"Notes:", None))
    # retranslateUi


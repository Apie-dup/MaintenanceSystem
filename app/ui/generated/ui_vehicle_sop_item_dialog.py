# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehicle_sop_item_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QPlainTextEdit,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_VehicleSopItemDialog(object):
    def setupUi(self, VehicleSopItemDialog):
        if not VehicleSopItemDialog.objectName():
            VehicleSopItemDialog.setObjectName(u"VehicleSopItemDialog")
        VehicleSopItemDialog.resize(400, 396)
        self.verticalLayout = QVBoxLayout(VehicleSopItemDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(VehicleSopItemDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSequence = QLabel(VehicleSopItemDialog)
        self.lblSequence.setObjectName(u"lblSequence")

        self.horizontalLayout.addWidget(self.lblSequence)

        self.spnSequence = QSpinBox(VehicleSopItemDialog)
        self.spnSequence.setObjectName(u"spnSequence")
        self.spnSequence.setMaximum(999)
        self.spnSequence.setValue(1)

        self.horizontalLayout.addWidget(self.spnSequence)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lblCheckDescription = QLabel(VehicleSopItemDialog)
        self.lblCheckDescription.setObjectName(u"lblCheckDescription")

        self.verticalLayout.addWidget(self.lblCheckDescription)

        self.txtCheckDescription = QPlainTextEdit(VehicleSopItemDialog)
        self.txtCheckDescription.setObjectName(u"txtCheckDescription")

        self.verticalLayout.addWidget(self.txtCheckDescription)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblRequired = QLabel(VehicleSopItemDialog)
        self.lblRequired.setObjectName(u"lblRequired")

        self.horizontalLayout_2.addWidget(self.lblRequired)

        self.chkRequired = QCheckBox(VehicleSopItemDialog)
        self.chkRequired.setObjectName(u"chkRequired")

        self.horizontalLayout_2.addWidget(self.chkRequired)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.buttonBox = QDialogButtonBox(VehicleSopItemDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(VehicleSopItemDialog)
        self.buttonBox.accepted.connect(VehicleSopItemDialog.accept)
        self.buttonBox.rejected.connect(VehicleSopItemDialog.reject)

        QMetaObject.connectSlotsByName(VehicleSopItemDialog)
    # setupUi

    def retranslateUi(self, VehicleSopItemDialog):
        VehicleSopItemDialog.setWindowTitle(QCoreApplication.translate("VehicleSopItemDialog", u"SOP Checklist Item\\n", None))
        self.lblTitle.setText(QCoreApplication.translate("VehicleSopItemDialog", u"SOP Checklist Item\n"
"", None))
        self.lblSequence.setText(QCoreApplication.translate("VehicleSopItemDialog", u"Sequence:", None))
        self.lblCheckDescription.setText(QCoreApplication.translate("VehicleSopItemDialog", u"Check Description:", None))
        self.lblRequired.setText(QCoreApplication.translate("VehicleSopItemDialog", u"Required:", None))
        self.chkRequired.setText("")
    # retranslateUi


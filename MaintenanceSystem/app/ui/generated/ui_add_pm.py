# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_pm.ui'
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
    QDateEdit, QDialog, QDialogButtonBox, QDoubleSpinBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class Ui_AddPMDialog(object):
    def setupUi(self, AddPMDialog):
        if not AddPMDialog.objectName():
            AddPMDialog.setObjectName(u"AddPMDialog")
        AddPMDialog.resize(884, 729)
        self.verticalLayout = QVBoxLayout(AddPMDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblPMNumber = QLabel(AddPMDialog)
        self.lblPMNumber.setObjectName(u"lblPMNumber")

        self.horizontalLayout.addWidget(self.lblPMNumber)

        self.txtPMNumber = QLineEdit(AddPMDialog)
        self.txtPMNumber.setObjectName(u"txtPMNumber")
        self.txtPMNumber.setReadOnly(True)

        self.horizontalLayout.addWidget(self.txtPMNumber)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblAsset = QLabel(AddPMDialog)
        self.lblAsset.setObjectName(u"lblAsset")

        self.horizontalLayout_2.addWidget(self.lblAsset)

        self.cmbAsset = QComboBox(AddPMDialog)
        self.cmbAsset.setObjectName(u"cmbAsset")

        self.horizontalLayout_2.addWidget(self.cmbAsset)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblTask = QLabel(AddPMDialog)
        self.lblTask.setObjectName(u"lblTask")

        self.horizontalLayout_3.addWidget(self.lblTask)

        self.txtTask = QLineEdit(AddPMDialog)
        self.txtTask.setObjectName(u"txtTask")

        self.horizontalLayout_3.addWidget(self.txtTask)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblDescription = QLabel(AddPMDialog)
        self.lblDescription.setObjectName(u"lblDescription")

        self.horizontalLayout_4.addWidget(self.lblDescription)

        self.teDescription = QTextEdit(AddPMDialog)
        self.teDescription.setObjectName(u"teDescription")

        self.horizontalLayout_4.addWidget(self.teDescription)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblFrequency = QLabel(AddPMDialog)
        self.lblFrequency.setObjectName(u"lblFrequency")

        self.horizontalLayout_5.addWidget(self.lblFrequency)

        self.cmbFrequency = QComboBox(AddPMDialog)
        self.cmbFrequency.setObjectName(u"cmbFrequency")

        self.horizontalLayout_5.addWidget(self.cmbFrequency)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblFrequencyValue = QLabel(AddPMDialog)
        self.lblFrequencyValue.setObjectName(u"lblFrequencyValue")

        self.horizontalLayout_6.addWidget(self.lblFrequencyValue)

        self.spnFrequencyValue = QSpinBox(AddPMDialog)
        self.spnFrequencyValue.setObjectName(u"spnFrequencyValue")

        self.horizontalLayout_6.addWidget(self.spnFrequencyValue)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lblLastService = QLabel(AddPMDialog)
        self.lblLastService.setObjectName(u"lblLastService")

        self.horizontalLayout_7.addWidget(self.lblLastService)

        self.dtLastService = QDateEdit(AddPMDialog)
        self.dtLastService.setObjectName(u"dtLastService")

        self.horizontalLayout_7.addWidget(self.dtLastService)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lblNextDue = QLabel(AddPMDialog)
        self.lblNextDue.setObjectName(u"lblNextDue")

        self.horizontalLayout_8.addWidget(self.lblNextDue)

        self.dtNextDue = QDateEdit(AddPMDialog)
        self.dtNextDue.setObjectName(u"dtNextDue")

        self.horizontalLayout_8.addWidget(self.dtNextDue)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lblPriority = QLabel(AddPMDialog)
        self.lblPriority.setObjectName(u"lblPriority")

        self.horizontalLayout_9.addWidget(self.lblPriority)

        self.cmbPriority = QComboBox(AddPMDialog)
        self.cmbPriority.setObjectName(u"cmbPriority")

        self.horizontalLayout_9.addWidget(self.cmbPriority)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lblEstimatedHours = QLabel(AddPMDialog)
        self.lblEstimatedHours.setObjectName(u"lblEstimatedHours")

        self.horizontalLayout_10.addWidget(self.lblEstimatedHours)

        self.dsbEstimatedHours = QDoubleSpinBox(AddPMDialog)
        self.dsbEstimatedHours.setObjectName(u"dsbEstimatedHours")

        self.horizontalLayout_10.addWidget(self.dsbEstimatedHours)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.ldlEstimatedCost = QLabel(AddPMDialog)
        self.ldlEstimatedCost.setObjectName(u"ldlEstimatedCost")

        self.horizontalLayout_11.addWidget(self.ldlEstimatedCost)

        self.dsbEstimatedCost = QDoubleSpinBox(AddPMDialog)
        self.dsbEstimatedCost.setObjectName(u"dsbEstimatedCost")

        self.horizontalLayout_11.addWidget(self.dsbEstimatedCost)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.labStautus = QLabel(AddPMDialog)
        self.labStautus.setObjectName(u"labStautus")

        self.horizontalLayout_12.addWidget(self.labStautus)

        self.chkActive = QCheckBox(AddPMDialog)
        self.chkActive.setObjectName(u"chkActive")

        self.horizontalLayout_12.addWidget(self.chkActive)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lblNotes = QLabel(AddPMDialog)
        self.lblNotes.setObjectName(u"lblNotes")

        self.horizontalLayout_13.addWidget(self.lblNotes)

        self.teNotes = QTextEdit(AddPMDialog)
        self.teNotes.setObjectName(u"teNotes")

        self.horizontalLayout_13.addWidget(self.teNotes)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.buttonBox = QDialogButtonBox(AddPMDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddPMDialog)
        self.buttonBox.accepted.connect(AddPMDialog.accept)
        self.buttonBox.rejected.connect(AddPMDialog.reject)

        QMetaObject.connectSlotsByName(AddPMDialog)
    # setupUi

    def retranslateUi(self, AddPMDialog):
        AddPMDialog.setWindowTitle(QCoreApplication.translate("AddPMDialog", u"Preventive Maintenance", None))
        self.lblPMNumber.setText(QCoreApplication.translate("AddPMDialog", u"PM Number", None))
        self.lblAsset.setText(QCoreApplication.translate("AddPMDialog", u"Asset", None))
        self.lblTask.setText(QCoreApplication.translate("AddPMDialog", u"Task", None))
        self.lblDescription.setText(QCoreApplication.translate("AddPMDialog", u"Description", None))
        self.lblFrequency.setText(QCoreApplication.translate("AddPMDialog", u"Frequency", None))
        self.lblFrequencyValue.setText(QCoreApplication.translate("AddPMDialog", u"Frequency Value", None))
        self.lblLastService.setText(QCoreApplication.translate("AddPMDialog", u"Last Service", None))
        self.lblNextDue.setText(QCoreApplication.translate("AddPMDialog", u"Next Due", None))
        self.lblPriority.setText(QCoreApplication.translate("AddPMDialog", u"Priority", None))
        self.lblEstimatedHours.setText(QCoreApplication.translate("AddPMDialog", u"Estimated Hours", None))
        self.ldlEstimatedCost.setText(QCoreApplication.translate("AddPMDialog", u"Estimated Cost", None))
        self.labStautus.setText(QCoreApplication.translate("AddPMDialog", u"Status", None))
        self.chkActive.setText("")
        self.lblNotes.setText(QCoreApplication.translate("AddPMDialog", u"Notes", None))
    # retranslateUi


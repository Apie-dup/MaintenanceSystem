# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'receive_stock_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ReceiveStockDialog(object):
    def setupUi(self, ReceiveStockDialog):
        if not ReceiveStockDialog.objectName():
            ReceiveStockDialog.setObjectName(u"ReceiveStockDialog")
        ReceiveStockDialog.resize(341, 537)
        self.verticalLayout = QVBoxLayout(ReceiveStockDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(ReceiveStockDialog)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.lblPart = QLabel(ReceiveStockDialog)
        self.lblPart.setObjectName(u"lblPart")

        self.verticalLayout.addWidget(self.lblPart)

        self.lblPartValue = QLabel(ReceiveStockDialog)
        self.lblPartValue.setObjectName(u"lblPartValue")

        self.verticalLayout.addWidget(self.lblPartValue)

        self.lblCurrentQuantity = QLabel(ReceiveStockDialog)
        self.lblCurrentQuantity.setObjectName(u"lblCurrentQuantity")

        self.verticalLayout.addWidget(self.lblCurrentQuantity)

        self.lblCurrentQuantityValue = QLabel(ReceiveStockDialog)
        self.lblCurrentQuantityValue.setObjectName(u"lblCurrentQuantityValue")

        self.verticalLayout.addWidget(self.lblCurrentQuantityValue)

        self.lblQuantityReceived = QLabel(ReceiveStockDialog)
        self.lblQuantityReceived.setObjectName(u"lblQuantityReceived")

        self.verticalLayout.addWidget(self.lblQuantityReceived)

        self.dsbQuantity = QDoubleSpinBox(ReceiveStockDialog)
        self.dsbQuantity.setObjectName(u"dsbQuantity")
        self.dsbQuantity.setMaximum(99999999.000000000000000)

        self.verticalLayout.addWidget(self.dsbQuantity)

        self.lblUnitCost = QLabel(ReceiveStockDialog)
        self.lblUnitCost.setObjectName(u"lblUnitCost")

        self.verticalLayout.addWidget(self.lblUnitCost)

        self.dsbUnitCost = QDoubleSpinBox(ReceiveStockDialog)
        self.dsbUnitCost.setObjectName(u"dsbUnitCost")
        self.dsbUnitCost.setMaximum(999999999.000000000000000)

        self.verticalLayout.addWidget(self.dsbUnitCost)

        self.lblReference = QLabel(ReceiveStockDialog)
        self.lblReference.setObjectName(u"lblReference")

        self.verticalLayout.addWidget(self.lblReference)

        self.txtReference = QLineEdit(ReceiveStockDialog)
        self.txtReference.setObjectName(u"txtReference")

        self.verticalLayout.addWidget(self.txtReference)

        self.lblNotes = QLabel(ReceiveStockDialog)
        self.lblNotes.setObjectName(u"lblNotes")

        self.verticalLayout.addWidget(self.lblNotes)

        self.txtNotes = QPlainTextEdit(ReceiveStockDialog)
        self.txtNotes.setObjectName(u"txtNotes")

        self.verticalLayout.addWidget(self.txtNotes)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonBox = QDialogButtonBox(ReceiveStockDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ReceiveStockDialog)

        QMetaObject.connectSlotsByName(ReceiveStockDialog)
    # setupUi

    def retranslateUi(self, ReceiveStockDialog):
        ReceiveStockDialog.setWindowTitle(QCoreApplication.translate("ReceiveStockDialog", u"Receive Stock", None))
        self.lblTitle.setText(QCoreApplication.translate("ReceiveStockDialog", u"Receive Stock", None))
        self.lblPart.setText(QCoreApplication.translate("ReceiveStockDialog", u"Part:", None))
        self.lblPartValue.setText("")
        self.lblCurrentQuantity.setText(QCoreApplication.translate("ReceiveStockDialog", u"Current Quantity:", None))
        self.lblCurrentQuantityValue.setText("")
        self.lblQuantityReceived.setText(QCoreApplication.translate("ReceiveStockDialog", u"Quantity Received:", None))
        self.lblUnitCost.setText(QCoreApplication.translate("ReceiveStockDialog", u"Unit Cost:", None))
        self.lblReference.setText(QCoreApplication.translate("ReceiveStockDialog", u"Reference:", None))
        self.lblNotes.setText(QCoreApplication.translate("ReceiveStockDialog", u"Notes:", None))
    # retranslateUi


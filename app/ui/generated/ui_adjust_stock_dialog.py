# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adjust_stock_dialog.ui'
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
    QDialogButtonBox, QDoubleSpinBox, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_AdjustStockDialog(object):
    def setupUi(self, AdjustStockDialog):
        if not AdjustStockDialog.objectName():
            AdjustStockDialog.setObjectName(u"AdjustStockDialog")
        AdjustStockDialog.resize(400, 616)
        self.verticalLayout = QVBoxLayout(AdjustStockDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(AdjustStockDialog)
        self.lblTitle.setObjectName(u"lblTitle")

        self.verticalLayout.addWidget(self.lblTitle)

        self.lblPart = QLabel(AdjustStockDialog)
        self.lblPart.setObjectName(u"lblPart")

        self.verticalLayout.addWidget(self.lblPart)

        self.lblPartValue = QLabel(AdjustStockDialog)
        self.lblPartValue.setObjectName(u"lblPartValue")

        self.verticalLayout.addWidget(self.lblPartValue)

        self.lblCurrentQuantity = QLabel(AdjustStockDialog)
        self.lblCurrentQuantity.setObjectName(u"lblCurrentQuantity")

        self.verticalLayout.addWidget(self.lblCurrentQuantity)

        self.lblCurrentQuantityValue = QLabel(AdjustStockDialog)
        self.lblCurrentQuantityValue.setObjectName(u"lblCurrentQuantityValue")

        self.verticalLayout.addWidget(self.lblCurrentQuantityValue)

        self.lblAdjustmentType = QLabel(AdjustStockDialog)
        self.lblAdjustmentType.setObjectName(u"lblAdjustmentType")

        self.verticalLayout.addWidget(self.lblAdjustmentType)

        self.cmbAdjustmentType = QComboBox(AdjustStockDialog)
        self.cmbAdjustmentType.addItem("")
        self.cmbAdjustmentType.addItem("")
        self.cmbAdjustmentType.setObjectName(u"cmbAdjustmentType")

        self.verticalLayout.addWidget(self.cmbAdjustmentType)

        self.lblQuantity = QLabel(AdjustStockDialog)
        self.lblQuantity.setObjectName(u"lblQuantity")

        self.verticalLayout.addWidget(self.lblQuantity)

        self.dsbQuantity = QDoubleSpinBox(AdjustStockDialog)
        self.dsbQuantity.setObjectName(u"dsbQuantity")
        self.dsbQuantity.setMinimum(0.010000000000000)
        self.dsbQuantity.setMaximum(999999999.000000000000000)

        self.verticalLayout.addWidget(self.dsbQuantity)

        self.lblNewQuantity = QLabel(AdjustStockDialog)
        self.lblNewQuantity.setObjectName(u"lblNewQuantity")

        self.verticalLayout.addWidget(self.lblNewQuantity)

        self.lblNewQuantityValue = QLabel(AdjustStockDialog)
        self.lblNewQuantityValue.setObjectName(u"lblNewQuantityValue")

        self.verticalLayout.addWidget(self.lblNewQuantityValue)

        self.lblReference = QLabel(AdjustStockDialog)
        self.lblReference.setObjectName(u"lblReference")

        self.verticalLayout.addWidget(self.lblReference)

        self.txtReference = QLineEdit(AdjustStockDialog)
        self.txtReference.setObjectName(u"txtReference")

        self.verticalLayout.addWidget(self.txtReference)

        self.lblNotes = QLabel(AdjustStockDialog)
        self.lblNotes.setObjectName(u"lblNotes")

        self.verticalLayout.addWidget(self.lblNotes)

        self.txtNotes = QPlainTextEdit(AdjustStockDialog)
        self.txtNotes.setObjectName(u"txtNotes")

        self.verticalLayout.addWidget(self.txtNotes)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonBox = QDialogButtonBox(AdjustStockDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AdjustStockDialog)

        self.cmbAdjustmentType.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AdjustStockDialog)
    # setupUi

    def retranslateUi(self, AdjustStockDialog):
        AdjustStockDialog.setWindowTitle(QCoreApplication.translate("AdjustStockDialog", u"Stock Adjustment", None))
        self.lblTitle.setText(QCoreApplication.translate("AdjustStockDialog", u"Stock Adjustment", None))
        self.lblPart.setText(QCoreApplication.translate("AdjustStockDialog", u"Part:", None))
        self.lblPartValue.setText("")
        self.lblCurrentQuantity.setText(QCoreApplication.translate("AdjustStockDialog", u"Current Quantity:", None))
        self.lblCurrentQuantityValue.setText("")
        self.lblAdjustmentType.setText(QCoreApplication.translate("AdjustStockDialog", u"Adjustment Type:", None))
        self.cmbAdjustmentType.setItemText(0, QCoreApplication.translate("AdjustStockDialog", u"Increase", None))
        self.cmbAdjustmentType.setItemText(1, QCoreApplication.translate("AdjustStockDialog", u"Decrease", None))

        self.cmbAdjustmentType.setCurrentText(QCoreApplication.translate("AdjustStockDialog", u"Increase", None))
        self.lblQuantity.setText(QCoreApplication.translate("AdjustStockDialog", u"Quantity:", None))
        self.lblNewQuantity.setText(QCoreApplication.translate("AdjustStockDialog", u"New Quantity:", None))
        self.lblNewQuantityValue.setText("")
        self.lblReference.setText(QCoreApplication.translate("AdjustStockDialog", u"Reference:", None))
        self.lblNotes.setText(QCoreApplication.translate("AdjustStockDialog", u"Notes:", None))
    # retranslateUi


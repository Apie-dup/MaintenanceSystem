# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_page.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_SettingsPage(object):
    def setupUi(self, SettingsPage):
        if not SettingsPage.objectName():
            SettingsPage.setObjectName(u"SettingsPage")
        SettingsPage.resize(719, 534)
        self.verticalLayout = QVBoxLayout(SettingsPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(SettingsPage)
        self.lblTitle.setObjectName(u"lblTitle")

        self.verticalLayout.addWidget(self.lblTitle)

        self.groupGeneralSettings = QGroupBox(SettingsPage)
        self.groupGeneralSettings.setObjectName(u"groupGeneralSettings")
        self.formLayout = QFormLayout(self.groupGeneralSettings)
        self.formLayout.setObjectName(u"formLayout")
        self.lblOrganizationName = QLabel(self.groupGeneralSettings)
        self.lblOrganizationName.setObjectName(u"lblOrganizationName")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblOrganizationName)

        self.txtOrganizationName = QLineEdit(self.groupGeneralSettings)
        self.txtOrganizationName.setObjectName(u"txtOrganizationName")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtOrganizationName)

        self.lblSystemName = QLabel(self.groupGeneralSettings)
        self.lblSystemName.setObjectName(u"lblSystemName")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblSystemName)

        self.txtSystemName = QLineEdit(self.groupGeneralSettings)
        self.txtSystemName.setObjectName(u"txtSystemName")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtSystemName)


        self.verticalLayout.addWidget(self.groupGeneralSettings)

        self.groupRegionalSetting = QGroupBox(SettingsPage)
        self.groupRegionalSetting.setObjectName(u"groupRegionalSetting")
        self.formLayout_2 = QFormLayout(self.groupRegionalSetting)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lblCurrencySymbol = QLabel(self.groupRegionalSetting)
        self.lblCurrencySymbol.setObjectName(u"lblCurrencySymbol")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblCurrencySymbol)

        self.txtCurrencySymbol = QLineEdit(self.groupRegionalSetting)
        self.txtCurrencySymbol.setObjectName(u"txtCurrencySymbol")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtCurrencySymbol)

        self.labelCurrencyCode = QLabel(self.groupRegionalSetting)
        self.labelCurrencyCode.setObjectName(u"labelCurrencyCode")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelCurrencyCode)

        self.txtCurrencyCode = QLineEdit(self.groupRegionalSetting)
        self.txtCurrencyCode.setObjectName(u"txtCurrencyCode")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtCurrencyCode)

        self.lblDateFormat = QLabel(self.groupRegionalSetting)
        self.lblDateFormat.setObjectName(u"lblDateFormat")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblDateFormat)

        self.cmbDateFormat = QComboBox(self.groupRegionalSetting)
        self.cmbDateFormat.setObjectName(u"cmbDateFormat")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbDateFormat)


        self.verticalLayout.addWidget(self.groupRegionalSetting)

        self.groupAppearance = QGroupBox(SettingsPage)
        self.groupAppearance.setObjectName(u"groupAppearance")
        self.formLayout_3 = QFormLayout(self.groupAppearance)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lblTheme = QLabel(self.groupAppearance)
        self.lblTheme.setObjectName(u"lblTheme")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblTheme)

        self.cmbTheme = QComboBox(self.groupAppearance)
        self.cmbTheme.setObjectName(u"cmbTheme")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbTheme)


        self.verticalLayout.addWidget(self.groupAppearance)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnReload = QPushButton(SettingsPage)
        self.btnReload.setObjectName(u"btnReload")

        self.horizontalLayout.addWidget(self.btnReload)

        self.btnSave = QPushButton(SettingsPage)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lblStatus = QLabel(SettingsPage)
        self.lblStatus.setObjectName(u"lblStatus")

        self.verticalLayout.addWidget(self.lblStatus)


        self.retranslateUi(SettingsPage)

        QMetaObject.connectSlotsByName(SettingsPage)
    # setupUi

    def retranslateUi(self, SettingsPage):
        SettingsPage.setWindowTitle(QCoreApplication.translate("SettingsPage", u"Settings Page", None))
        self.lblTitle.setText(QCoreApplication.translate("SettingsPage", u"Settings", None))
        self.groupGeneralSettings.setTitle(QCoreApplication.translate("SettingsPage", u"General Settings", None))
        self.lblOrganizationName.setText(QCoreApplication.translate("SettingsPage", u"Organization Name:", None))
        self.lblSystemName.setText(QCoreApplication.translate("SettingsPage", u"System Name:", None))
        self.groupRegionalSetting.setTitle(QCoreApplication.translate("SettingsPage", u"Regional Settings", None))
        self.lblCurrencySymbol.setText(QCoreApplication.translate("SettingsPage", u"Currency Symbol:", None))
        self.labelCurrencyCode.setText(QCoreApplication.translate("SettingsPage", u"Currency Code:", None))
        self.lblDateFormat.setText(QCoreApplication.translate("SettingsPage", u"Date Format:", None))
        self.groupAppearance.setTitle(QCoreApplication.translate("SettingsPage", u"Appearance", None))
        self.lblTheme.setText(QCoreApplication.translate("SettingsPage", u"Theme:", None))
        self.btnReload.setText(QCoreApplication.translate("SettingsPage", u"Reload", None))
        self.btnSave.setText(QCoreApplication.translate("SettingsPage", u"Save Settings", None))
        self.lblStatus.setText(QCoreApplication.translate("SettingsPage", u"Status:", None))
    # retranslateUi


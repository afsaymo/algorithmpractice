# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'algMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QPushButton,
    QSizePolicy, QWidget)

class Ui_algMenu(object):
    def setupUi(self, algMenu):
        if not algMenu.objectName():
            algMenu.setObjectName(u"algMenu")
        algMenu.resize(229, 181)
        self.gridLayout = QGridLayout(algMenu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cb_alg_select = QComboBox(algMenu)
        self.cb_alg_select.addItem("")
        self.cb_alg_select.addItem("")
        self.cb_alg_select.addItem("")
        self.cb_alg_select.setObjectName(u"cb_alg_select")

        self.gridLayout.addWidget(self.cb_alg_select, 0, 0, 1, 2)

        self.cb_start = QComboBox(algMenu)
        self.cb_start.addItem("")
        self.cb_start.addItem("")
        self.cb_start.addItem("")
        self.cb_start.addItem("")
        self.cb_start.addItem("")
        self.cb_start.setObjectName(u"cb_start")

        self.gridLayout.addWidget(self.cb_start, 1, 0, 1, 1)

        self.cb_end = QComboBox(algMenu)
        self.cb_end.addItem("")
        self.cb_end.addItem("")
        self.cb_end.addItem("")
        self.cb_end.addItem("")
        self.cb_end.addItem("")
        self.cb_end.setObjectName(u"cb_end")

        self.gridLayout.addWidget(self.cb_end, 1, 1, 1, 1)

        self.bttn_begin = QPushButton(algMenu)
        self.bttn_begin.setObjectName(u"bttn_begin")

        self.gridLayout.addWidget(self.bttn_begin, 2, 0, 1, 1)


        self.retranslateUi(algMenu)

        QMetaObject.connectSlotsByName(algMenu)
    # setupUi

    def retranslateUi(self, algMenu):
        algMenu.setWindowTitle(QCoreApplication.translate("algMenu", u"Form", None))
        self.cb_alg_select.setItemText(0, QCoreApplication.translate("algMenu", u"Select Search Algorithm", None))
        self.cb_alg_select.setItemText(1, QCoreApplication.translate("algMenu", u"Depth First Search", None))
        self.cb_alg_select.setItemText(2, QCoreApplication.translate("algMenu", u"Breadth First Search", None))

        self.cb_start.setItemText(0, QCoreApplication.translate("algMenu", u"Select Start", None))
        self.cb_start.setItemText(1, QCoreApplication.translate("algMenu", u"A", None))
        self.cb_start.setItemText(2, QCoreApplication.translate("algMenu", u"B", None))
        self.cb_start.setItemText(3, QCoreApplication.translate("algMenu", u"C", None))
        self.cb_start.setItemText(4, QCoreApplication.translate("algMenu", u"D", None))

        self.cb_end.setItemText(0, QCoreApplication.translate("algMenu", u"Select End", None))
        self.cb_end.setItemText(1, QCoreApplication.translate("algMenu", u"A", None))
        self.cb_end.setItemText(2, QCoreApplication.translate("algMenu", u"B", None))
        self.cb_end.setItemText(3, QCoreApplication.translate("algMenu", u"C", None))
        self.cb_end.setItemText(4, QCoreApplication.translate("algMenu", u"D", None))

        self.bttn_begin.setText(QCoreApplication.translate("algMenu", u"Begin Search", None))
    # retranslateUi


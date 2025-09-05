# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'oversaetterlayout.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

import roeversprog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(568, 389)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 20, 481, 261))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName(u"widget")
        self.tittle = QLabel(self.widget)
        self.tittle.setObjectName(u"tittle")
        self.tittle.setGeometry(QRect(110, 0, 281, 41))
        self.tittle.setAutoFillBackground(False)
        self.tittle.setStyleSheet(u" font: 18pt \"Segoe UI\";")
        self.insertlabel = QLabel(self.widget)
        self.insertlabel.setObjectName(u"insertlabel")
        self.insertlabel.setGeometry(QRect(20, 60, 181, 21))
        self.insertlabel.setAutoFillBackground(False)
        self.insertlabel.setStyleSheet(u"background-color: white; font: 10pt \"Segoe UI\";")
        self.insertlabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.insertlabel.setFrameShadow(QFrame.Shadow.Raised)
        self.roversprog = QLabel(self.widget)
        self.roversprog.setObjectName(u"roversprog")
        self.roversprog.setGeometry(QRect(290, 60, 171, 21))
        self.roversprog.setStyleSheet(u"background-color: white; font: 10pt \"Segoe UI\";")
        self.roversprog.setFrameShape(QFrame.Shape.StyledPanel)
        self.roversprog.setFrameShadow(QFrame.Shadow.Raised)
        self.change_button = QPushButton(self.widget)
        self.change_button.setObjectName(u"change_button")
        self.change_button.setGeometry(QRect(210, 120, 75, 24))
        self.change_button2 = QPushButton(self.widget)
        self.change_button2.setObjectName(u"change_button2")
        self.change_button2.setGeometry(QRect(210, 160, 75, 24))
        self.inputframe = QFrame(self.widget)
        self.inputframe.setObjectName(u"inputframe")
        self.inputframe.setGeometry(QRect(20, 80, 181, 171))
        self.inputframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.inputframe.setFrameShadow(QFrame.Shadow.Raised)
        self.inputfelt = QPlainTextEdit(self.inputframe)
        self.inputfelt.setObjectName(u"inputfelt")
        self.inputfelt.setGeometry(QRect(0, 0, 181, 171))
        self.inputfelt.setStyleSheet(u"background-color: lavenderblush;")
        self.inputfelt.setReadOnly(False)
        self.inputfelt.setOverwriteMode(True)
        self.inputfelt.setBackgroundVisible(False)
        self.outputframe = QFrame(self.widget)
        self.outputframe.setObjectName(u"outputframe")
        self.outputframe.setGeometry(QRect(290, 80, 171, 171))
        self.outputframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.outputframe.setFrameShadow(QFrame.Shadow.Raised)
        self.outputfelt = QPlainTextEdit(self.outputframe)
        self.outputfelt.setObjectName(u"outputfelt")
        self.outputfelt.setGeometry(QRect(0, 0, 171, 171))
        self.outputfelt.setStyleSheet(u"background-color: lavenderblush;")
        self.outputfelt.setReadOnly(True)
        self.outputfelt.setOverwriteMode(False)
        self.outputframe.raise_()
        self.inputframe.raise_()
        self.tittle.raise_()
        self.insertlabel.raise_()
        self.roversprog.raise_()
        self.change_button.raise_()
        self.change_button2.raise_()
        self.change_button.clicked.connect(self.changed_button)
        self.change_button2.clicked.connect(self.changed_button)

        self.verticalLayout.addWidget(self.widget)

        self.background = QWidget(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(-10, 0, 581, 351))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet(u"background-color: lightpink; font-size: 16px;")
        self.translatebutton = QPushButton(self.background)
        self.translatebutton.setObjectName(u"translatebutton")
        self.translatebutton.setGeometry(QRect(250, 280, 121, 41))
        self.translatebutton.setAutoFillBackground(False)
        self.translatebutton.setStyleSheet(u"background-color: white; font-size: 16px;")
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.background.raise_()
        self.verticalLayoutWidget.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 568, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tittle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; text-decoration: underline; color:#fdfdfd;\">R\u00f8versprog translator</span></p></body></html>", None))
        self.insertlabel.setText(QCoreApplication.translate("MainWindow", u"Insert any language here:", None))
        self.roversprog.setText(QCoreApplication.translate("MainWindow", u"R\u00f8versprog:", None))
        self.change_button.setText(QCoreApplication.translate("MainWindow", u"--->", None))
        self.change_button2.setText(QCoreApplication.translate("MainWindow", u"<---", None))
        self.inputfelt.setPlainText(QCoreApplication.translate("MainWindow", u"inds\u00e6t dit tekst her..", None))
        self.translatebutton.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        
    # retranslateUi
    def changed_button(self):

        current_insertlabel_text = self.insertlabel.text()
        current_røversprog_text = self.roversprog.text()

        if current_insertlabel_text == "Insert any language here:" and current_røversprog_text == "Røversprog:":
            self.insertlabel.setText("Indsæt dit røversprog")
            self.roversprog.setText("Almindeligt sprog")
            
        elif current_insertlabel_text == "Indsæt dit røversprog" and current_røversprog_text == "Almindeligt sprog":
            self.insertlabel.setText("Insert any language here:")
            self.roversprog.setText("Røversprog:")

    
    # change

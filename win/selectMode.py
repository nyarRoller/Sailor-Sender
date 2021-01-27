# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectMode.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap

class Ui_selectMode(object):
    def setupUi(self, selectMode):
        selectMode.setObjectName("selectMode")
        selectMode.resize(972, 770)
        selectMode.setMinimumSize(QtCore.QSize(972, 770))
        selectMode.setMaximumSize(QtCore.QSize(972, 770))
        self.centralwidget = QtWidgets.QWidget(selectMode)
        self.centralwidget.setObjectName("centralwidget")
        self.log = QtWidgets.QWidget(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(10, 10, 941, 51))
        self.log.setStyleSheet("background-color: white;\n"
" border-radius:10px;")
        self.log.setObjectName("log")
        self.LogOut = QtWidgets.QPushButton(self.log)
        self.LogOut.setGeometry(QtCore.QRect(840, 10, 91, 31))
        self.LogOut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LogOut.setStyleSheet("QPushButton {\n"
"background-color: #333333;\n"
"border-radius: 10px;\n"
"\n"
"font-family: Poppins-Medium;\n"
"font-size: 15px;\n"
"color: #fff;\n"
"line-height: 1.2;\n"
"}\n"
"QPushButton::before {\n"
"  content: \"\";\n"
"  display: block;\n"
"  position: absolute;\n"
"  z-index: -1;\n"
"  width: 100%;\n"
"  height: 100%;\n"
"  border-radius: 10px;\n"
"  top: 0;\n"
"  left: 0;\n"
"  background: #a64bf4;\n"
"  background: -webkit-linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  background: -o-linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  background: -moz-linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  background: linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  opacity: 0;\n"
"  -webkit-transition: all 0.4s;\n"
"  -o-transition: all 0.4s;\n"
"  -moz-transition: all 0.4s;\n"
"  transition: all 0.4s;\n"
"}\n"
"\n"
"QPushButton:hover:before{\n"
"    opacity: 1;\n"
"}"
"QPushButton:hover {\n"
"  background-color: #545454;\n"
"}\n")
        self.LogOut.setObjectName("LogOut")
        self.email = QtWidgets.QLabel(self.log)
        self.email.setGeometry(QtCore.QRect(500, 14, 121, 16))
        self.email.setStyleSheet("font-family: Poppins-Regular;\n"
"font-size: 20px;")
        self.email.setObjectName("email")
        self.back = QtWidgets.QPushButton(self.log)
        self.back.setGeometry(QtCore.QRect(20, 10, 181, 31))
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setStyleSheet("QPushButton {\n"
"background-color: #333333;\n"
"border-radius: 10px;\n"
"\n"
"font-family: Poppins-Medium;\n"
"font-size: 15px;\n"
"color: #fff;\n"
"line-height: 1.2;\n"
"}\n"
"QPushButton::before {\n"
"  content: \"\";\n"
"  display: block;\n"
"  position: absolute;\n"
"  z-index: -1;\n"
"  width: 100%;\n"
"  height: 100%;\n"
"  border-radius: 10px;\n"
"  top: 0;\n"
"  left: 0;\n"
"  background: #a64bf4;\n"
"  background: -webkit-linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  background: -o-linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  background: -moz-linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  background: linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  opacity: 0;\n"
"  -webkit-transition: all 0.4s;\n"
"  -o-transition: all 0.4s;\n"
"  -moz-transition: all 0.4s;\n"
"  transition: all 0.4s;\n"
"}\n"
"\n"
"QPushButton:hover:before{\n"
"    opacity: 1;\n"
"}"
"QPushButton:hover {\n"
"  background-color: #545454;\n"
"}\n")
        self.back.setObjectName("back")
        self.bg = QtWidgets.QFrame(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(-10, -20, 1001, 811))
        self.bg.setObjectName("bg")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(140, 210, 721, 461))
        self.widget.setStyleSheet("background-color:white;\n"
"border-radius:15px;")
        self.widget.setObjectName("widget")
        self.ApGenerator = QtWidgets.QPushButton(self.widget)
        self.ApGenerator.setGeometry(QtCore.QRect(60, 210, 251, 81))
        self.ApGenerator.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ApGenerator.setStyleSheet("QPushButton {\n"
"background-color: #333333;\n"
"border-radius: 10px;\n"
"\n"
"font-family: Poppins-Medium;\n"
"font-size: 25px;\n"
"color: #fff;\n"
"line-height: 1.2;\n"
"}\n"
"QPushButton::before {\n"
"  content: \"\";\n"
"  display: block;\n"
"  position: absolute;\n"
"  z-index: -1;\n"
"  width: 100%;\n"
"  height: 100%;\n"
"  border-radius: 10px;\n"
"  top: 0;\n"
"  left: 0;\n"
"  background: #a64bf4;\n"
"  background: -webkit-linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  background: -o-linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  background: -moz-linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  background: linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  opacity: 0;\n"
"  -webkit-transition: all 0.4s;\n"
"  -o-transition: all 0.4s;\n"
"  -moz-transition: all 0.4s;\n"
"  transition: all 0.4s;\n"
"}\n"
"\n"
"QPushButton:hover:before{\n"
"    opacity: 1;\n"
"}"
"QPushButton:hover {\n"
"  background-color: #545454;\n"
"}\n")
        self.ApGenerator.setObjectName("ApGenerator")
        self.ManualMode = QtWidgets.QPushButton(self.widget)
        self.ManualMode.setGeometry(QtCore.QRect(400, 210, 251, 81))
        self.ManualMode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ManualMode.setStyleSheet("QPushButton {\n"
"background-color: #333333;\n"
"border-radius: 10px;\n"
"\n"
"font-family: Poppins-Medium;\n"
"font-size: 25px;\n"
"color: #fff;\n"
"line-height: 1.2;\n"
"}\n"
"QPushButton::before {\n"
"  content: \"\";\n"
"  display: block;\n"
"  position: absolute;\n"
"  z-index: -1;\n"
"  width: 100%;\n"
"  height: 100%;\n"
"  border-radius: 10px;\n"
"  top: 0;\n"
"  left: 0;\n"
"  background: #a64bf4;\n"
"  background: -webkit-linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  background: -o-linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  background: -moz-linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  background: linear-gradient(45deg, #00dbde, #fc00ff);\n"
"  opacity: 0;\n"
"  -webkit-transition: all 0.4s;\n"
"  -o-transition: all 0.4s;\n"
"  -moz-transition: all 0.4s;\n"
"  transition: all 0.4s;\n"
"}\n"
"\n"
"QPushButton:hover:before{\n"
"    opacity: 1;\n"
"}"
"QPushButton:hover {\n"
"  background-color: #545454;\n"
"}\n")
        self.ManualMode.setObjectName("ManualMode")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(70, 80, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Poppins-Regular")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font-family: Poppins-Regular;\n"
"font-size: 40px;")
        self.label.setObjectName("label")
        self.bg.setStyleSheet("background-image: url(bg-01.jpg)")
        self.bg.raise_()

        self.bg.adjustSize()
        self.log.raise_()
        self.widget.raise_()
        selectMode.setCentralWidget(self.centralwidget)

        self.retranslateUi(selectMode)
        QtCore.QMetaObject.connectSlotsByName(selectMode)

    def retranslateUi(self, selectMode):
        _translate = QtCore.QCoreApplication.translate
        selectMode.setWindowTitle(_translate("selectMode", "Sailor Sender"))
        self.LogOut.setText(_translate("selectMode", "Вийти"))
        self.email.setText(_translate("selectMode", "Електронна пошта"))
        self.back.setText(_translate("selectMode", "Назад"))
        self.ApGenerator.setText(_translate("selectMode", "Application Generator"))
        self.ManualMode.setText(_translate("selectMode", "Manual mode"))
        self.label.setText(_translate("selectMode", "Оберіть режим"))

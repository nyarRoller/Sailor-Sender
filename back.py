# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'back.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BackTo(object):
    def setupUi(self, BackTo):
        BackTo.setObjectName("BackTo")
        BackTo.resize(972, 770)
        BackTo.setMinimumSize(QtCore.QSize(972, 770))
        BackTo.setMaximumSize(QtCore.QSize(972, 770))

        self.gridLayout = QtWidgets.QGridLayout(BackTo)
        self.gridLayout.setObjectName("gridLayout")
        self.cs = QtWidgets.QWidget(BackTo)
        self.cs.setObjectName("cs")
        self.widget_2 = QtWidgets.QWidget(self.cs)
        self.widget_2.setGeometry(QtCore.QRect(290, 170, 421, 421))
        self.widget_2.setStyleSheet("background-color:white;\n"
"border-radius:10px;")
        self.widget_2.setObjectName("widget_2")
        self.Back = QtWidgets.QPushButton(self.widget_2)
        self.Back.setGeometry(QtCore.QRect(80, 320, 251, 31))
        self.Back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back.setStyleSheet("QPushButton {\n"
"background-color: #333333;\n"
"border-radius: 10px;\n"
"\n"
"font-family: Poppins-Medium;\n"
"font-size: 16px;\n"
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
"}")
        self.Back.setObjectName("Back")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(20, 30, 430, 90))
        self.label.setStyleSheet("font-family: Poppins-Regular;\n"
"font-size: 25px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(55, 170, 421, 91))
        self.label_2.setStyleSheet("font-family: Poppins-Regular;\n"
"font-size: 20px;\n"
"text-align: center;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(50, 240, 421, 20))
        self.label_3.setStyleSheet("font-family: Poppins-Regular;\n"
"font-size: 20px;\n"
"text-align: center;")
        self.label_3.setObjectName("label_3")
        self.BgBackTo = QtWidgets.QWidget(self.cs)
        self.BgBackTo.setGeometry(QtCore.QRect(-1, -1, 973, 773))
        self.BgBackTo.setObjectName("BgBackTo")
        self.BgBackTo.raise_()
        self.BgBackTo.setStyleSheet("background-image: url(bg-01.jpg);")
        self.widget_2.raise_()
        self.gridLayout.addWidget(self.cs, 0, 0, 1, 1)

        self.retranslateUi(BackTo)
        QtCore.QMetaObject.connectSlotsByName(BackTo)

    def retranslateUi(self, BackTo):
        _translate = QtCore.QCoreApplication.translate
        BackTo.setWindowTitle(_translate("BackTo", "Sailor Sender"))
        self.Back.setText(_translate("BackTo", "Выйти"))
        self.label.setText(_translate("BackTo", "Рассылка успешно выполнена"))
        self.label_2.setText(_translate("BackTo", "Чтобы выйти из программы"))
        self.label_3.setText(_translate("BackTo", "Нажмите на кнопку ниже"))

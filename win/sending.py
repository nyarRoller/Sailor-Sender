# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sending.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(972, 770)
        MainForm.setMinimumSize(QtCore.QSize(972, 770))
        MainForm.setMaximumSize(QtCore.QSize(972, 770))
        self.bg = QtWidgets.QWidget(MainForm)
        self.bg.setGeometry(QtCore.QRect(40, 30, 891, 711))
        self.bg.setStyleSheet("background-color: white;\n"
"border-radius:10px;")
        self.bg.setObjectName("bg")
        self.body = QtWidgets.QTextEdit(self.bg)
        self.body.setGeometry(QtCore.QRect(40, 140, 801, 431))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.body.setFont(font)
        self.body.setStyleSheet(" background-color: #f7f7f7;\n"
" border: 1px solid #e6e6e6;\n"
" border-radius: 10px;\n"
"font: 57 16pt \"Poppins Medium\";")
        self.body.setObjectName("body")
        self.subjEdit = QtWidgets.QLineEdit(self.bg)
        self.subjEdit.setGeometry(QtCore.QRect(40, 40, 801, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.subjEdit.setFont(font)
        self.subjEdit.setStyleSheet(" background-color: #f7f7f7;\n"
" border: 1px solid #e6e6e6;\n"
" border-radius: 10px;\n"
" font: 57 16pt \"Poppins\";")
        self.subjEdit.setText("")
        self.subjEdit.setObjectName("subjEdit")
        self.sendFile = QtWidgets.QPushButton(self.bg)
        self.sendFile.setGeometry(QtCore.QRect(720, 620, 131, 24))
        self.sendFile.setStyleSheet("QPushButton {\n"
"background-color: #333333;\n"
"border-radius: 10px;\n"
"\n"
"font-family: Poppins-Medium;\n"
"font-size: 16px;\n"
"color: #fff;\n"
"line-height: 1.2;\n"
"}")
        self.sendFile.setObjectName("sendFile")
        self.fileChose = QtWidgets.QLineEdit(self.bg)
        self.fileChose.setGeometry(QtCore.QRect(40, 622, 671, 21))
        self.fileChose.setStyleSheet(" background-color: #f7f7f7;\n"
" border: 1px solid #e6e6e6;\n"
" border-radius: 10px;\n"
" font: 57 16pt \"Poppins\";")
        self.fileChose.setObjectName("fileChose")
        self.sendForm = QtWidgets.QPushButton(self.bg)
        self.sendForm.setGeometry(QtCore.QRect(340, 660, 211, 41))
        self.sendForm.setStyleSheet("QPushButton {\n"
"background-color: #333333;\n"
"border-radius: 10px;\n"
"\n"
"font-family: Poppins-Medium;\n"
"font-size: 25px;\n"
"color: #fff;\n"
"line-height: 1.2;\n"
"}")
        self.sendForm.setObjectName("sendForm")
        self.theme = QtWidgets.QLabel(self.bg)
        self.theme.setGeometry(QtCore.QRect(50, 20, 111, 16))
        self.theme.setStyleSheet("font-family: Poppins-Regular;\n"
"color: #333333;\n"
"line-height: 1.2;\n"
"font-size: 18px;")
        self.theme.setObjectName("theme")
        self.text = QtWidgets.QLabel(self.bg)
        self.text.setGeometry(QtCore.QRect(50, 120, 121, 16))
        self.text.setStyleSheet("font-family: Poppins-Regular;\n"
"color: #333333;\n"
"line-height: 1.2;\n"
"font-size: 18px;")
        self.text.setObjectName("text")
        self.fileAp = QtWidgets.QLabel(self.bg)
        self.fileAp.setGeometry(QtCore.QRect(60, 600, 91, 16))
        self.fileAp.setStyleSheet("font-family: Poppins-Regular;\n"
"color: #333333;\n"
"line-height: 1.2;\n"
"font-size: 18px;")
        self.fileAp.setObjectName("fileAp")
        self.log = QtWidgets.QWidget(MainForm)
        self.log.setGeometry(QtCore.QRect(40, 0, 891, 51))
        self.log.setStyleSheet("background-color: white;\n"
" border-radius:10px;")
        self.log.setObjectName("log")
        self.LogOut = QtWidgets.QPushButton(self.log)
        self.LogOut.setGeometry(QtCore.QRect(770, 10, 91, 31))
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
"}")
        self.LogOut.setObjectName("LogOut")
        self.email = QtWidgets.QLabel(self.log)
        self.email.setGeometry(QtCore.QRect(410, 5, 121, 16))
        self.email.setStyleSheet("font-family: Poppins-Regular;\n"
"font-size: 20px;")
        self.email.setObjectName("email")
        self.back = QtWidgets.QPushButton(self.log)
        self.back.setGeometry(QtCore.QRect(10, 10, 181, 31))
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
"}")
        self.back.setObjectName("back")
        self.b_g = QtWidgets.QWidget(MainForm)
        self.b_g.setGeometry(QtCore.QRect(-20, -10, 1001, 791))
        self.b_g.setObjectName("b_g")
        self.b_g.raise_()
        self.bg.raise_()
        self.log.raise_()

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Sailor Sender"))
        self.body.setHtml(_translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Poppins Medium\'; font-size:16pt; font-weight:56; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>"))
        self.sendFile.setText(_translate("MainForm", "Выбрать файл"))
        self.sendForm.setText(_translate("MainForm", "Отправить"))
        self.theme.setText(_translate("MainForm", "Тема письма"))
        self.text.setText(_translate("MainForm", "Текст письма"))
        self.fileAp.setText(_translate("MainForm", "Апликашка"))
        self.LogOut.setText(_translate("MainForm", "Log out"))
        self.email.setText(_translate("MainForm", "Email Adress"))
        self.back.setText(_translate("MainForm", "Back"))

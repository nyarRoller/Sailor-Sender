# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(972, 770)
        Dialog.setMinimumSize(QtCore.QSize(927, 770))
        Dialog.setMaximumSize(QtCore.QSize(972, 770))
        self.bg = QtWidgets.QWidget(Dialog)
        self.bg.setGeometry(QtCore.QRect(40, 35, 891, 711))
        self.bg.setStyleSheet("background-color: white;\n"
"border-radius:10px;")
        self.bg.setObjectName("bg")
        self.body_2 = QtWidgets.QTextEdit(self.bg)
        self.body_2.setGeometry(QtCore.QRect(40, 140, 801, 431))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.body_2.setFont(font)
        self.body_2.setStyleSheet(" background-color: #f7f7f7;\n"
" border: 1px solid #e6e6e6;\n"
" border-radius: 10px;\n"
"font: 57 16pt \"Poppins Medium\";")
        self.body_2.setObjectName("body_2")
        self.subjEdit_2 = QtWidgets.QLineEdit(self.bg)
        self.subjEdit_2.setGeometry(QtCore.QRect(40, 40, 801, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.subjEdit_2.setFont(font)
        self.subjEdit_2.setStyleSheet(" background-color: #f7f7f7;\n"
" border: 1px solid #e6e6e6;\n"
" border-radius: 10px;\n"
" font: 57 16pt \"Poppins\";")
        self.subjEdit_2.setText("")
        self.subjEdit_2.setObjectName("subjEdit_2")
        self.sendFile_2 = QtWidgets.QPushButton(self.bg)
        self.sendFile_2.setGeometry(QtCore.QRect(720, 620, 131, 24))
        self.sendFile_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendFile_2.setStyleSheet("QPushButton {\n"
"background-color: #333333;\n"
"border-radius: 10px;\n"
"\n"
"font-family: Poppins-Medium;\n"
"font-size: 16px;\n"
"color: #fff;\n"
"line-height: 1.2;\n"
"}"
"QPushButton:hover {\n"
"  background-color: #545454;\n"
"}\n")
        self.sendFile_2.setObjectName("sendFile_2")
        self.fileChose_2 = QtWidgets.QLineEdit(self.bg)
        self.fileChose_2.setGeometry(QtCore.QRect(40, 622, 671, 21))
        self.fileChose_2.setStyleSheet(" background-color: #f7f7f7;\n"
" border: 1px solid #e6e6e6;\n"
" border-radius: 10px;\n"
" font: 57 16pt \"Poppins\";")
        self.fileChose_2.setObjectName("fileChose_2")
        self.sendForm_2 = QtWidgets.QPushButton(self.bg)
        self.sendForm_2.setGeometry(QtCore.QRect(340, 660, 211, 41))
        self.sendForm_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendForm_2.setStyleSheet("QPushButton {\n"
"background-color: #333333;\n"
"border-radius: 10px;\n"
"\n"
"font-family: Poppins-Medium;\n"
"font-size: 25px;\n"
"color: #fff;\n"
"line-height: 1.2;\n"
"}"
"QPushButton:hover {\n"
"  background-color: #545454;\n"
"}\n")
        self.sendForm_2.setObjectName("sendForm_2")
        self.theme_2 = QtWidgets.QLabel(self.bg)
        self.theme_2.setGeometry(QtCore.QRect(50, 20, 111, 16))
        self.theme_2.setStyleSheet("font-family: Poppins-Regular;\n"
"color: #333333;\n"
"line-height: 1.2;\n"
"font-size: 18px;")
        self.theme_2.setObjectName("theme_2")
        self.text_2 = QtWidgets.QLabel(self.bg)
        self.text_2.setGeometry(QtCore.QRect(50, 120, 121, 16))
        self.text_2.setStyleSheet("font-family: Poppins-Regular;\n"
"color: #333333;\n"
"line-height: 1.2;\n"
"font-size: 18px;")
        self.text_2.setObjectName("text_2")
        self.fileAp_2 = QtWidgets.QLabel(self.bg)
        self.fileAp_2.setGeometry(QtCore.QRect(60, 600, 91, 16))
        self.fileAp_2.setStyleSheet("font-family: Poppins-Regular;\n"
"color: #333333;\n"
"line-height: 1.2;\n"
"font-size: 18px;")
        self.fileAp_2.setObjectName("fileAp_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 971, 771))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(80, 790, 811, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color:white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: lightblue;\n"
"    width: 10px;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.widget.raise_()
        self.widget.setStyleSheet("background-image: url(bg-01.jpg);")
        self.bg.raise_()
        self.log = QtWidgets.QWidget(Dialog)
        self.log.setGeometry(QtCore.QRect(40, 5, 891, 51))
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
"}"
"QPushButton:hover {\n"
"  background-color: #545454;\n"
"}\n")
        self.LogOut.setObjectName("LogOut")
        self.email = QtWidgets.QLabel(self.log)
        self.email.setGeometry(QtCore.QRect(450, 14, 121, 16))
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
"}"
"QPushButton:hover {\n"
"  background-color: #545454;\n"
"}\n")
        self.back.setObjectName("back")
        self.log.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sailor Sender"))
        self.body_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Poppins Medium\'; font-size:16pt; font-weight:56; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>"))
        self.sendFile_2.setText(_translate("Dialog", "Выбрать файл"))
        self.sendForm_2.setText(_translate("Dialog", "Отправить"))
        self.theme_2.setText(_translate("Dialog", "Тема письма"))
        self.text_2.setText(_translate("Dialog", "Текст письма"))
        self.fileAp_2.setText(_translate("Dialog", "Апликашка"))
        self.LogOut.setText(_translate("Dialog", "Log out"))
        self.email.setText(_translate("Dialog", "Email Adress"))
        self.back.setText(_translate("Dialog", "Back"))

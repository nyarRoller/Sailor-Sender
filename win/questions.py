# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'questions.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QST(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 770)
        MainWindow.setMinimumSize(QtCore.QSize(972, 770))
        MainWindow.setMaximumSize(QtCore.QSize(972, 770))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.areaQuestion = QtWidgets.QWidget(self.centralwidget)
        self.areaQuestion.setGeometry(QtCore.QRect(140, 200, 701, 361))
        self.areaQuestion.setStyleSheet("background-color:white;\n"
"border-radius:10px;")
        self.areaQuestion.setObjectName("areaQuestion")
        self.question = QtWidgets.QLabel(self.areaQuestion)
        self.question.setGeometry(QtCore.QRect(30, 60, 651, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins-Regular")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.question.setFont(font)
        self.question.setStyleSheet("font-family: Poppins-Regular;\n"
"font-size: 20px;")
        self.question.setObjectName("question")
        self.questionAnswer = QtWidgets.QLineEdit(self.areaQuestion)
        self.questionAnswer.setGeometry(QtCore.QRect(20, 220, 651, 31))
        self.questionAnswer.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.questionAnswer.setStyleSheet(" background-color: #d4d4d4;\n"
" border: 1px solid #e6e6e6;\n"
" border-radius: 10px;")
        self.questionAnswer.setObjectName("questionAnswer")
        self.Enter = QtWidgets.QPushButton(self.areaQuestion)
        self.Enter.setGeometry(QtCore.QRect(370, 300, 250, 41))
        self.Enter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Enter.setStyleSheet("QPushButton {\n"
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
"QPushButton:hover{\n"
"    background-color: #545454;\n"
"}")
        self.Enter.setObjectName("Enter")
        self.bk = QtWidgets.QPushButton(self.areaQuestion)
        self.bk.setGeometry(QtCore.QRect(80, 300, 250, 41))
        self.bk.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bk.setStyleSheet("QPushButton {\n"
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
"QPushButton:hover{\n"
"    background-color: #545454;"
"}")
        self.bk.setObjectName("bk")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 971, 771))
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.widget.setStyleSheet("background-image: url(bg-01.jpg);")
        self.areaQuestion.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.log = QtWidgets.QWidget(MainWindow)
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
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sailor Sender"))
        self.question.setText(_translate("MainWindow", "Вопрос"))
        self.Enter.setText(_translate("MainWindow", "Next"))
        self.bk.setText(_translate("MainWindow", "Back"))
        self.LogOut.setText(_translate("selectMode", "Log out"))
        self.email.setText(_translate("selectMode", "Email Adress"))
        self.back.setText(_translate("selectMode", "Back"))
        


#Login window
from PyQt5 import QtCore, QtGui, QtWidgets
import json
import sys
import os

sys.path.append(os.getcwd())
from data.language import languages
with open("data\data.json", "r") as read_file:
        data = json.load(read_file)
lang = data["language"]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 770)
        MainWindow.setMinimumSize(QtCore.QSize(972, 770))
        MainWindow.setMaximumSize(QtCore.QSize(972, 770))
        MainWindow.setStyleSheet("background-color: ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 973, 773))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("background-image: url(bg-01.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(270, 200, 421, 421))
        self.widget.setStyleSheet("background-color:white;\n"
"border-radius:10px;")
        self.widget.setObjectName("widget")
        self.Enter = QtWidgets.QPushButton(self.widget)
        self.Enter.setGeometry(QtCore.QRect(80, 320, 251, 31))
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
"QPushButton:hover {\n"
"  background-color: #545454;\n"
"}\n"
)
        self.Enter.setObjectName("Enter")
        self.status = QtWidgets.QLabel(self.widget)
        self.status.setGeometry(QtCore.QRect(160, 30, 290, 61))
        self.status.move(95,36)
        self.status.setStyleSheet("font-family: Poppins-Regular;\n"
"font-size: 20px;\n"
)
        self.status.setObjectName("status")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(80, 50, 71, 21))
        self.label.move(20,55)
        font = QtGui.QFont()
        font.setFamily("Poppins-Regular")
        font.setPointSize(0)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font-family: Poppins-Regular;\n"
"font-size: 20px;")
        self.label.setObjectName("label")
        self.Pasword = QtWidgets.QLineEdit(self.widget)
        self.Pasword.setGeometry(QtCore.QRect(80, 250, 251, 31))
        self.Pasword.setStyleSheet(" background-color: #f7f7f7;\n"
" border: 1px solid #e6e6e6;\n"
" border-radius: 10px;\n"
" font: 57 16pt \"Poppins\";")
        self.Pasword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Pasword.setReadOnly(False)
        self.Pasword.setObjectName("Pasword")
        self.Email = QtWidgets.QLineEdit(self.widget)
        self.Email.setGeometry(QtCore.QRect(80, 170, 251, 31))
        self.Email.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Email.setStyleSheet(" background-color: #f7f7f7;\n"
" border: 1px solid #e6e6e6;\n"
" border-radius: 10px;\n"
" font: 57 16pt \"Poppins\";")

        self.Email.setObjectName("Email")
        self.labeEmail = QtWidgets.QLabel(self.widget)
        self.labeEmail.setGeometry(QtCore.QRect(80, 140, 70, 20))
        self.labeEmail.setMinimumSize(QtCore.QSize(0, 13))
        self.labeEmail.setStyleSheet("font-family: Poppins-Regular;\n"
"color: #333333;\n"
"line-height: 1.2;\n"
"font-size: 18px;")
        self.labeEmail.setObjectName("labeEmail")
        self.labelPasword = QtWidgets.QLabel(self.widget)
        self.labelPasword.setGeometry(QtCore.QRect(80, 220, 81, 16))
        self.labelPasword.setStyleSheet("font-family: Poppins-Regular;\n"
"color: #333333;\n"
"line-height: 1.2;\n"
"font-size: 18px;")
        self.labelPasword.setObjectName("labelPasword")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sailor Sender"))
        self.Enter.setText(_translate("MainWindow", languages[lang]["mainWindow"]["login"]))
        self.status.setText(_translate("MainWindow", languages[lang]["mainWindow"]["statusInfo"][0]))
        self.label.setText(_translate("MainWindow", languages[lang]["mainWindow"]["status"]))
        self.labeEmail.setText(_translate("MainWindow", languages[lang]["mainWindow"]["email"]))
        self.labelPasword.setText(_translate("MainWindow", languages[lang]["mainWindow"]["password"]))

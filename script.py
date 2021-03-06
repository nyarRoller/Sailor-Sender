import yagmail
import sys

import base64
import smtplib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from win.GUI import *
import os
from PyQt5.QtWidgets import QMessageBox
from data.database import QuestList

import time
import codecs
from win.back import *
from win.fileDialog import *
from enum import Enum, auto

from win.dialog import *
import time
from win.SelectObj import *

from win.questions import *

from win.selectMode import *
from docxtpl import DocxTemplate
import json
import temp.yagmail.__init__ 
from sys import argv, executable
from data.language import languages

errorLogin = True
global infoText
infoText = "None"

def getId(dct,i):
    localI = 0
    for key in dct:
        if localI == i:
            return key 
        else:
            localI += 1
form = False
class selectMode(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self,parent)
        self.SM = Ui_selectMode()
        self.SM.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))
        
        self.SM.ManualMode.clicked.connect(self.ManualModeFunk)
        self.SM.ApGenerator.clicked.connect(self.ApMode)

        with open("data\data.json", "r") as f:
            data = json.load(f) 

        self.SM.email.setText(data['account']['login'])
        self.SM.email.adjustSize()
        self.SM.LogOut.clicked.connect(self.logOut)
        self.SM.back.clicked.connect(self.back)

    def back(self):
        self.close()
        win = SelectObj(self)   
        win.show()
    def logOut(self):
        with open("data\data.json", "r") as f:
            data = json.load(f) 
        
        data["account"]["login"] = None
        data["account"]["pasword"] = None
        data["enterInAccount"] = False
        with open("data\data.json", "w") as write_file:
            json.dump(data, write_file, indent = 4)
        
        

        self.win = MyWin(self)
        self.close()
        self.win.show()

        
    def ManualModeFunk(self):
        try:
            self.close()
            nextWindow = MyForm(self) #Переход к конечной вкладке
            nextWindow.show()
        except Exception as e:
            print(e)
            self.close()
            nextWin = selectMode(self)
            nextWin.show()



    def ApMode(self):
        try:
            self.close()
            nextWindow = quest(self) #Переход к конечной вкладке
            nextWindow.show()
        except:
            self.close()
            nextWin = selectMode(self)
            nextWin.show()

class quest(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        
        self.questNum = 0
        QtWidgets.QWidget.__init__(self, parent)

        self.qst = Ui_QST()
        self.qst.setupUi(self)

        
        self.setWindowIcon(QIcon('icon.png'))

        self.qst.Enter.clicked.connect(self.next)
        
        self.qst.question.setText(QuestList[0])   
        self.procent = 100 / (len(QuestList) - 1) #Расчёт прогрес бара
        self.step = 0 #Начальное значение
        
        self.qst.email.setText(data['account']['login'])
        self.qst.email.adjustSize()
        self.qst.LogOut.clicked.connect(self.logOut)
        self.qst.back.clicked.connect(self.back)

    def back(self):
        self.close()
        win = selectMode(self)
        win.show()
    def logOut(self):
        with open("data\data.json", "r") as f:
            data = json.load(f) 
        
        data["account"]["login"] = None
        data["account"]["pasword"] = None
        data["enterInAccount"] = False
        with open("data\data.json", "w") as w:
            json.dump(data, w, indent = 4)
        
        self.close()
        win = MyWin(self)
        win.show() 
        
  
    def next(self):
        with open("data\quest.json", "r") as r:
            questData = json.load(r)

        try:
            questData["answers"][getId(questData["answers"],self.questNum)] = self.qst.questionAnswer.text()
            questData["questCount"] = self.questNum
            self.qst.questionAnswer.setText("")
            self.questNum += 1
            self.qst.question.setText(QuestList[self.questNum])
            
            with open("data\quest.json", "w") as w:
                json.dump(questData, w, indent = 4)

                   

        except IndexError:
            self.qst.question.setText("Формування резюме, зачекайте")
            
            context = {}
            with open("data/quest.json","r") as read_file:
                questData = json.load(read_file)
            doc = DocxTemplate("Novikontas application.docx")
            for key in questData["answers"]:
                context[key] = questData["answers"][key]
            
            doc.render(context)
            doc.save("newDoc.docx")
            global form
            form = True
            print("Suc form")
            win = MyForm(self)
            self.close()
            win.show()


class Error(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle("Пропущено путь")
        self.setWindowIcon(QIcon('icon.png'))        
        self.setObjectName("MainWindow")
        self.sizeX, self.sizeY = 400, 200
        self.resize(self.sizeX, self.sizeY)
        self.setMinimumSize(QtCore.QSize(self.sizeX, self.sizeY))
        self.setMaximumSize(QtCore.QSize(self.sizeX, self.sizeY))
        self.setStyleSheet("background-color: ")   
        global infoText 
        self.label = QtWidgets.QLabel(infoText,self)
        self.label.setGeometry(QtCore.QRect(self.sizeX//2 - 25 ,self.sizeY//2-40 ,110, 30))
        font = QtGui.QFont()
        font.setFamily("Poppins-Regular")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(35)
        self.label.setFont(font)
        self.label.setStyleSheet("font-family: Poppins-Regular;\n"
"font-size: 20px;")
        self.btn = QtWidgets.QPushButton('Ok', self)
        self.btn.setGeometry(QtCore.QRect(self.sizeX//2 - 50, self.sizeY - 20 - 31, 100, 31))        
        self.btn.setStyleSheet("QPushButton {\n"
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
        self.btn.clicked.connect(self.leave)

    def leave(self):
        self.close() 
        self.win = MyWin()
        self.win.show()

class BkTo(QtWidgets.QDialog): #Форма для выхода из программы
    
    def __init__(self, parent = None): 
        super(BkTo, self).__init__(parent)
        self.bk = Ui_BackTo()
        self.bk.setupUi(self)
        self.bk.Back.clicked.connect(self.back) #Кнопка выхода
        self.setWindowIcon(QIcon('icon.png'))

    def back(self):
        sys.exit()

class MyForm(QtWidgets.QDialog): #Окно отправки сообщения
    def __init__(self, parent = None):
        super(MyForm, self).__init__(parent)
        self.form = Ui_Dialog() 
        self.form.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))
        self.progressBar = QtWidgets.QProgressBar(self) #Создание прогресбара
        self.progressBar.setGeometry(QtCore.QRect(80, 740, 811, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color:black;\n"
"    font-family: arial black;\n"
"}\n"
"\n"
"QProgr essBar::chunk {\n"
"    background-color: lightblue;\n"
"    width: 10px;\n"
"}")

        self.progressBar.setProperty("value", 0) #Значение прогресабара по умолчанию
        self.progressBar.setObjectName("progressBar")
        if form:
         self.form.fileChose_2.setText(str(os.path.abspath("newDoc.docx")))
         self.form.sendFile_2.setEnabled(False)
         self.form.fileChose_2.setEnabled(False)

        self.form.sendFile_2.clicked.connect(self.showDialog) #Кнопка прикрепить файл

        self.form.sendForm_2.clicked.connect(self.sendForm) #Кнопка "Отправить"

        self.form.email.setText(data['account']['login'])
        self.form.email.adjustSize()
        self.form.LogOut.clicked.connect(self.logOut)
        self.form.back.clicked.connect(self.back)

    def back(self):
        self.close()
        win = selectMode(self)
        win.show()
    def logOut(self):
        with open("data/data.json", "r") as read_file:
            data = json.load(read_file)
        
        data["account"]["login"] = None
        data["account"]["pasword"] = None
        data["enterInAccount"] = False
        with open("data\data.json", "w") as f:
            json.dump(data, f, indent = 4)
        
        self.close()

        self.win = MyWin(self)
        # selfwin.show()        
    def showDialog(self):
 
        # fname = Dialog(self) #Получение имени файла через проводник
        # fname.filters = ["Doc files (*.doc *.docx *.pdf)"]
        # fname.default_filter_index = 0
        # # fname.getOpenFileName(self, 'Open file')
        # fname.exec()
        # print('{0}/{1}'.format(fname.filename[0], fname.filename[1]))

        file_dialog = QFileDialog(self)
        # the name filters must be a list
        file_dialog.setNameFilters(["Doc files (*.doc *.docx)", "pdf (*.pdf)"])
        file_dialog.selectNameFilter("Doc files (*.doc *.docx)")
        # show the dialog
        file_dialog.exec_()
        if str(file_dialog.selectedFiles()) == "[]":
             self.form.fileChose_2.setText("")
        else:
            self.form.fileChose_2.setText(str('{0}'.format(file_dialog.selectedFiles()[0])))#Отображение пути к файлу
    
    def sendForm(self): #Рассылка сообщений
        print("Отправка сообщений")
        if self.form.fileChose_2.text() != "":
            with open("data\data.json", "r") as f:
                data = json.load(f)     
            ent = entering(data['account']['login'], base64.b64decode(data['account']['pasword'].encode("UTF-8")).decode("UTF-8"))
            
            subj = self.form.subjEdit_2.text() #Получение темы
            body = self.form.body_2.toPlainText() #Получение текста
            file = self.form.fileChose_2.text() #Получение файла

            procent = 100 / len(BaseObl) #Расчёт прогрес бара
            value = 0 #Начальное значение
            try:
                for adress in BaseObl: #Функция отправки сообщений
                    try:
                        ent.send(
                        to= adress,
                        subject=subj,
                        contents=body, 
                        attachments=file,
                        )
                        for i in range(round(procent) + 1):
                            value += 1
                            self.progressBar.setValue(value)
                            time.sleep(0.1)   
                        print("Отпрвлен на" + adress)
                    except smtplib.SMTPRecipientsRefused:
                        print("пропущен " + adress)
                        for i in range(round(procent) + 1):
                            value += 1
                            self.progressBar.setValue(value)
                            time.sleep(0.001)   
                        continue
                    except:
                        for i in range(round(procent) + 1):
                            value += 1
                            self.progressBar.setValue(value)
                            time.sleep(0.001)   
                        continue                
                self.close()
                BackForm = BkTo(self) #Переход к конечной вкладке
                BackForm.exec_()     
            except TypeError: #Исключение, если пропушена апликашка
                sys.path.append(os.getcwd())
                with open("data\data.json", "r") as read_file:
                        data = json.load(read_file)
                lang = data["language"]               
                QMessageBox.about(self, languages[lang]["sending"]["warning"], languages[lang]["sending"]["warningInfo"])
           

        else:      
            sys.path.append(os.getcwd())
            with open("data\data.json", "r") as read_file:
                    data = json.load(read_file)
            lang = data["language"]               
            QMessageBox.about(self, languages[lang]["sending"]["warning"], languages[lang]["sending"]["warningInfo"])
           

    def msgButtonClick(self):
        pass      




class SelectObj(QtWidgets.QMainWindow): #Выбор области
    
    def __init__(self, parent = None):
        super(SelectObj, self).__init__(parent)
        self.so = Ui_SelectObl()
        self.so.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))
#Иницилизация всех кнопок
        self.so.frame.setStyleSheet("background-image: url(bg-01.jpg);")
        self.so.Vintis.clicked.connect(self.vinits)
        self.so.Volinsk.clicked.connect(self.volin)
        self.so.Dnipropentrovsk.clicked.connect(self.dnipro)
        self.so.Donteska.clicked.connect(self.dontes)
        self.so.Zhitomirska.clicked.connect(self.zhitomir)
        self.so.Zakarpatska.clicked.connect(self.zakarpat)
        self.so.Zaporizka.clicked.connect(self.zaporis)
        self.so.Ivanofrankivska.clicked.connect(self.ivanofrank)
        self.so.Kievska.clicked.connect(self.kievska)
        self.so.Kirovogradska.clicked.connect(self.kirovograd)
        self.so.Luganska.clicked.connect(self.lugansk)
        self.so.Lvivska.clicked.connect(self.lvivsk)
        self.so.Mikolaevska.clicked.connect(self.mikolaevsk)
        self.so.Sumska.clicked.connect(self.sumska)
        self.so.Hmelnitska.clicked.connect(self.hmelnitska)
        self.so.Harkivska.clicked.connect(self.harkivsk)
        self.so.Chekaska.clicked.connect(self.cherkaska)
        self.so.Chernivetksa.clicked.connect(self.chernivetska)
        self.so.Rivnenska.clicked.connect(self.rivnenska)
        self.so.Chernikibska.clicked.connect(self.chernigivska)
        self.so.Poltavska.clicked.connect(self.poltavska)
        self.so.mKiev.clicked.connect(self.mstKiev)
        self.so.Vinitska.clicked.connect(self.vinits)
        self.so.Ukraine.clicked.connect(self.fullUkraine)
        self.so.Ternopilska.clicked.connect(self.ternopilska)
        self.so.Hersonska.clicked.connect(self.hersonska)
        self.so.Odeska.clicked.connect(self.odessa)  


#Работа кнопок
    def odessa(self):
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Одеська область"]
        self.close()
        dial = selectMode(self)
        dial.show()
        
    def vinits(self): #Виницкая область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)
        global BaseObl
        BaseObl = dataEmail["Море"]["Віницька область"]
        self.close()
        dial = selectMode(self)
        dial.show()         

    def volin(self): #Волинская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Волинська область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def dnipro(self): #Днипропетровская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Дніпропетровська область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def dontes(self): #Донецкая область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)
        global BaseObl
        BaseObl = dataEmail["Море"]["Донецька область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def zhitomir(self): #Житомирская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Житомирська область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def zakarpat(self): #Закарпатская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)
        global BaseObl
        BaseObl = dataEmail["Море"]["Закарпатська область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def zaporis(self): #Запорижская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Запорізька область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         
    
    def ivanofrank(self): #Иванофранковская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Іванофранківська область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def kievska(self): #Киевская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Київська область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def kirovograd(self): #Кировоградская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Кіровоградська область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def lugansk(self): #Луганская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Луганська область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def lvivsk(self): #Львовская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Львівська область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def mikolaevsk(self): #Миколаевская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Миколаївська область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def mstKiev(self): #Город Киев
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Місто Київ"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def harkivsk(self): #Харьковская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Харківська область"]
        self.close()
        dial = selectMode(self)
       
        dial.show()         
  
    def poltavska(self): #Полтавская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Полтавська область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def rivnenska(self): #Ровенская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Рівненська область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         


    def sumska(self): #Сумская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Сумська область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         


    def ternopilska(self): #Тернопольская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Тернопільська область"]
        self.close()
        dial = selectMode(self)
       
        dial.show()         

    def hersonska(self): #Херсонская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Херсонька область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def hmelnitska(self): #Хмельницкая область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Хмельницька область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def cherkaska(self): #Черкаская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Черкаська область"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def chernivetska(self): #Чернивецкая область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Чернивецька область"]
        self.close()
        dial = selectMode(self)
    
        dial.show()         

    def chernigivska(self): #Чернигевская область
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Чернігіська"]
        self.close()
        dial = selectMode(self)
        
        dial.show()          

    def fullUkraine(self): #Вся Украина
        with open("database.json", "r", encoding = "utf-8") as f:
            dataEmail = json.load(f)        
        global BaseObl
        BaseObl = dataEmail["Море"]["Вся Україна"]
        self.close()
        dial = selectMode(self)
        
        dial.show()         


class MyWin(QtWidgets.QMainWindow):
#Иницилизация приложения
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        with open("data\data.json", "r") as f:
            data = json.load(f)    
        if data["language"] == "Ukrainian":
            languagesList = ["Ukrainian", "English"]
        else:      
            languagesList = ["English","Ukrainian"]
        self.ui = Ui_MainWindow()
        self.nx = None
        self.ui.setupUi(self)
        box = QComboBox(self)
        box.addItems(languagesList)
        box.setStyleSheet('''
    background-color: #a64bf4;\n;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: bold 14px;
    min-width: 10em;
    padding: 6px;
''')
        box.move(5, 10)
        self.ui.Enter.clicked.connect(self.enterOpen) #Иницилизация кнопки
        box.activated[str].connect(self.changLn)
        self.setWindowIcon(QIcon('icon.png'))

    
    def changLn(self, text):
        with open("data\data.json", "r") as f:
            data = json.load(f) 
        data["language"] = text
        with open("data\data.json", "w") as write_file:
            json.dump(data, write_file, indent = 4)        
        # if data["language"] != text:
        os.execl(executable, os.path.abspath(__file__), *argv)

            
        
#Работа кнопки входа
    def enterOpen(self):
        self.ui.status.setText("Вход в учётную запись")

        errorLogin = False
        print("Вход в учётную запись")
        global ent
        # yag = yagmail.SMTP(self.ui.Email.text(), self.ui.Pasword.text())
        # yag.login()
        with open("data\data.json", "r") as f:
            data = json.load(f) 

        data['account']['login'] = self.ui.Email.text()
        data['account']['pasword'] = base64.b64encode(self.ui.Pasword.text().encode("UTF-8")).decode("UTF-8")

        with open("data\data.json", "w") as write_file:
            json.dump(data, write_file, indent = 4)

        ent = entering(self.ui.Email.text(), self.ui.Pasword.text()) #Запоминание данных для входа

        if entering(self.ui.Email.text(), self.ui.Pasword.text()): #Проверка на правильлность логина и пароля
            with open("data\data.json", "r") as read_file:
                data = json.load(read_file) 
            data['enterInAccount'] = True       
        
            with open("data\data.json", "w") as write_file:
                json.dump(data, write_file, indent = 4)

            
            self.dial = SelectObj(self.nx)            
            self.dial.show()
            self.close()

        else:
            self.ui.status.setText("Невірний пароль")  #Вывод ошибки



#Вход в учётную запись
def entering(email,pasword):
    yag = yagmail.SMTP(email,pasword)

    try: #Попытка  входа
        yag.login()


    except smtplib.SMTPAuthenticationError: #Исключение на случай ошибки авторизации от смтп
            print("Невірно вказано логін або пароль")
            return False

    except yagmail.error.YagInvalidEmailAddress: #Исключение на случай неверного формата адреса
            print("Не вірно вказано електронну пошту")
            return False
    return yag





#Запуск программы
if __name__ == "__main__":   
    try:    
        app = QtWidgets.QApplication([])

        with open("data\data.json", "r") as read_file:
            data = json.load(read_file)
        if data['enterInAccount']:
            try:
                yag = yagmail.SMTP(base64.b64decode(data['account']['login'].encode("UTF-8")).decode("UTF-8"),base64.b64decode(data['account']['pasword'].encode("UTF-8")).decode("UTF-8"))
                yag.login()

                if data["startPage"] == 1:
                    application = SelectObj()

                if data["startPage"] == 2: 
                    application = selectMode()
                
                if data["startPage"] == 3:
                    application = quest()
                
                if data["startPage"] == 4:
                    application = MyForm()

                if data["startPage"] == 5:
                    application = BkTo()
                if data["startPage"] == 6:
                    application = Error()                

            except smtplib.SMTPAuthenticationError: #Исключение на случай ошибки авторизации от смтп
                print("Неверный логин или пароль")
                errorLogin = True
                application = MyWin()
            except AttributeError as e:
                print(e)
                errorLogin = True
                application = MyWin()     
            except:
                application = MyWin(n )            


                
        else:
            application = MyWin()

        application.show()
        sys.exit(app.exec())
    except Exception as e:
        f = open("logs.txt")
        f.write(str(e))
        f.close()

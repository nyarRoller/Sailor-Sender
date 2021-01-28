import yagmail
import sys

import base64

import smtplib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from GUI import *

from database import *

import time
import codecs
from back import *

from enum import Enum, auto

from dialog import *
import time
from SelectObj import *

from questions import *

from selectMode import *
from docxtpl import DocxTemplate
import json
errorLogin = True




class selectMode(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self,parent)
        self.SM = Ui_selectMode()
        self.SM.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))
        
        self.SM.ManualMode.clicked.connect(self.ManualModeFunk)
        self.SM.ApGenerator.clicked.connect(self.ApMode)

        with open("data.json", "r") as read_file:
            data = json.load(read_file) 

        self.SM.email.setText(base64.b64decode(data['account']['login'].encode("UTF-8")).decode("UTF-8"))
        self.SM.email.adjustSize()
        self.SM.LogOut.clicked.connect(self.logOut)
        self.SM.back.clicked.connect(self.back)

    def back(self):
        self.close()
        win = SelectObj(self)
        win.show()
    def logOut(self):
        with open("data.json", "r") as read_file:
            data = json.load(read_file)
        
        data["account"]["login"] = None
        data["account"]["pasword"] = None
        data["enterInAccount"] = False
        with open("data.json", "w") as write_file:
            json.dump(data, write_file, indent = 4)
        
        self.close()

        win = MyWin(self)
        win.show()
        
    def ManualModeFunk(self):
        
        self.close()
        nextWindow = MyForm(self) #Переход к конечной вкладке
        nextWindow.show()


    def ApMode(self):
        with open("data.json", "r") as read_file:
            data = json.load(read_file)
        if data["ApGenMode"]:
            self.close()
            nextWindow = quest(self) #Переход к конечной вкладке
            nextWindow.show()
        else:
            pass
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
        
        self.qst.email.setText(base64.b64decode(data['account']['login'].encode("UTF-8")).decode("UTF-8"))
        self.qst.email.adjustSize()
        self.qst.LogOut.clicked.connect(self.logOut)
        self.qst.back.clicked.connect(self.back)

    def back(self):
        self.close()
        win = selectMode(self)
        win.show()
    def logOut(self):
        with open("data.json", "r") as read_file:
            data = json.load(read_file)
        
        data["account"]["login"] = None
        data["account"]["pasword"] = None
        data["enterInAccount"] = False
        with open("data.json", "w") as write_file:
            json.dump(data, write_file, indent = 4)
        
        self.close()

        
  
    def next(self):
        with open("quest.json", "r") as read_file:
            questData = json.load(read_file)

        try:
            questData["answers"][str(self.questNum + 1)] = self.qst.questionAnswer.text()
            questData["questCount"] = self.questNum
            self.qst.questionAnswer.setText("")
            self.questNum += 1
            self.qst.question.setText(QuestList[self.questNum])
            
            with open("quest.json", "w") as write_file:
                json.dump(questData, write_file, indent = 4)

                   

        except IndexError:
            self.qst.question.setText("Вопросы кончились")
            # anketa()
        

    # def anketa(self):
    #     context = {}
    #     with open("quest.json","r") as read_file:
    #         questData = json.load(read_file)
    #     doc = DocxTemplate("Novikontas application.doc")
    #     for key in questData["answers"]:
    #         context[key] = questData["answers"][key]
        
    #     doc.render(context)
    #     doc.save("newDoc.docx")



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
        self.form = Ui_Dialog() #иницилизация диалога
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
"QProgressBar::chunk {\n"
"    background-color: lightblue;\n"
"    width: 10px;\n"
"}")

        self.progressBar.setProperty("value", 0) #Значение прогресабара по умолчанию
        self.progressBar.setObjectName("progressBar")

        self.form.sendFile_2.clicked.connect(self.showDialog) #Кнопка прикрепить файл

        self.form.sendForm_2.clicked.connect(self.sendForm) #Кнопка "Отправить"

        self.form.email.setText(base64.b64decode(data['account']['login'].encode("UTF-8")).decode("UTF-8"))
        self.form.email.adjustSize()
        self.form.LogOut.clicked.connect(self.logOut)
        self.form.back.clicked.connect(self.back)

    def back(self):
        self.close()
        win = selectMode(self)
        win.show()
    def logOut(self):
        with open("data.json", "r") as read_file:
            data = json.load(read_file)
        
        data["account"]["login"] = None
        data["account"]["pasword"] = None
        data["enterInAccount"] = False
        with open("data.json", "w") as write_file:
            json.dump(data, write_file, indent = 4)
        
        self.close()

        win = MyWin(self)
        win.show()        
    def showDialog(self):
 
        fname = QFileDialog.getOpenFileName(self, 'Open file') #Получение имени файла через проводник

        self.form.fileChose_2.setText(str(fname[0])) #Отображение пути к файлу
    
    def sendForm(self): #Рассылка сообщений
        print("Отправка сообщений")
        with open("data.json", "r") as read_file:
            data = json.load(read_file)     
        ent = entering(base64.b64decode(data['account']['login'].encode("UTF-8")).decode("UTF-8"), base64.b64decode(data['account']['pasword'].encode("UTF-8")).decode("UTF-8"))
        
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
                except yagmail.error.YagInvalidEmailAddress:
                    print("пропущен " + adress)
                    for i in range(round(procent) + 1):
                        value += 1
                        self.progressBar.setValue(value)
                        time.sleep(0.001)   
                    continue
                    
        except TypeError: #Исключение, если пропушена апликашка
            for adress in BaseObl:
                try:
                    ent.send(
                    to= adress,
                    subject=subj,
                    contents=body, 
                    )      
                    for i in range(round(procent) + 1):
                        value += 1
                        self.progressBar.setValue(value)
                        time.sleep(0.1)   
                    print("Отпрвлен на " + adress)     
                    
                except yagmail.error.YagInvalidEmailAddress:
                    for i in range(round(procent) + 1):
                        value += 1
                        self.progressBar.setValue(value)
                        time.sleep(0.1)   
                    continue
                    

        self.close()
        BackForm = BkTo(self) #Переход к конечной вкладке
        BackForm.exec_()

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
        global BaseObl

        BaseObl = database["Одеська область"]
        self.close()
        dial = selectMode(self)
        dial.show()
        
    def vinits(self): #Виницкая область
        global BaseObl
        BaseObl = VinnitObl

        self.close()
        dial = selectMode(self)
        dial.show()         

    def volin(self): #Волинская область
        global BaseObl
        BaseObl = VolinObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def dnipro(self): #Днипропетровская область
        global BaseObl
        BaseObl = DniprObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def dontes(self): #Донецкая область
        global BaseObl
        BaseObl = DonetskObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def zhitomir(self): #Житомирская область
        global BaseObl
        BaseObl = ZjitObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def zakarpat(self): #Закарпатская область
        global BaseObl
        BaseObl = ZakarpatObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def zaporis(self): #Запорижская область
        global BaseObl
        BaseObl = ZaporizObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         
    
    def ivanofrank(self): #Иванофранковская область
        global BaseObl
        BaseObl = IvanoFrankObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def kievska(self): #Киевская область
        global BaseObl
        BaseObl = KievskaObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def kirovograd(self): #Кировоградская область
        global BaseObl
        BaseObl = KirovogradObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def lugansk(self): #Луганская область
        global BaseObl
        BaseObl = LuganskaObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def lvivsk(self): #Львовская область
        global BaseObl
        BaseObl = LvivskaObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def mikolaevsk(self): #Миколаевская область
        global BaseObl
        BaseObl = MikolaevObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def mstKiev(self): #Город Киев
        global BaseObl
        BaseObl = Kiev
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def harkivsk(self): #Харьковская область
        global BaseObl
        BaseObl = HarkivObl
        self.close()
        dial = selectMode(self)
       
        dial.show()         

    def odeska(self): #Одеская область
        global BaseObl
        BaseObl = OdeskaObl
        self.close()
        dial = selectMode(self)
        dial.show()         

    def poltavska(self): #Полтавская область
        global BaseObl
        BaseObl = PoltavObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def rivnenska(self): #Ровенская область
        global BaseObl
        BaseObl = RivnenskaObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         


    def sumska(self): #Сумская область
        global BaseObl
        BaseObl = SumskaObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         


    def ternopilska(self): #Тернопольская область
        global BaseObl
        BaseObl = TernopilObl
        self.close()
        dial = selectMode(self)
       
        dial.show()         

    def hersonska(self): #Херсонская область
        global BaseObl
        BaseObl = HersonObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def hmelnitska(self): #Хмельницкая область
        global BaseObl
        BaseObl = HmelnitskaObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def cherkaska(self): #Черкаская область
        global BaseObl
        BaseObl = CherkaskaObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def chernivetska(self): #Чернивецкая область
        global BaseObl
        BaseObl = ChernivetskaObl
        self.close()
        dial = selectMode(self)
    
        dial.show()         

    def chernigivska(self): #Чернигевская область
        global BaseObl
        BaseObl = ChernigivskaObl
        self.close()
        dial = selectMode(self)
        
        dial.show()         

    def fullUkraine(self): #Вся Украина
        global BaseObl
        BaseObl = fUkraine
        self.close()
        dial = selectMode(self)
        
        dial.show()         


class MyWin(QtWidgets.QMainWindow):
#Иницилизация приложения
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.Enter.clicked.connect(self.enterOpen) #Иницилизация кнопки

        self.setWindowIcon(QIcon('icon.png'))


#Работа кнопки входа
    def enterOpen(self):
        self.ui.status.setText("Вход в учётную запись")

        errorLogin = False
        print("Вход в учётную запись")
        global ent
        # yag = yagmail.SMTP(self.ui.Email.text(), self.ui.Pasword.text())
        # yag.login()
        with open("data.json", "r") as read_file:
            data = json.load(read_file)

        data['account']['login'] = base64.b64encode(self.ui.Email.text().encode("UTF-8")).decode("UTF-8")
        data['account']['pasword'] = base64.b64encode(self.ui.Pasword.text().encode("UTF-8")).decode("UTF-8")

        with open("data.json", "w") as write_file:
            json.dump(data, write_file, indent = 4)

        ent = entering(self.ui.Email.text(), self.ui.Pasword.text()) #Запоминание данных для входа

        if entering(self.ui.Email.text(), self.ui.Pasword.text()): #Проверка на правильлность логина и пароля
            with open("data.json", "r") as read_file:
                data = json.load(read_file) 
            data['enterInAccount'] = True       
        
            with open("data.json", "w") as write_file:
                json.dump(data, write_file, indent = 4)

            self.close()
            self.dial = SelectObj(self)            
            self.dial.show()

        else:
            self.ui.status.setText("Wrong email or pasword")  #Вывод ошибки



#Вход в учётную запись
def entering(email,pasword):
    yag = yagmail.SMTP(email,pasword)

    try: #Попытка  входа
        yag.login()

    except yagmail.error.YagInvalidEmailAddress: #Исключение на случай неверного формата адреса
            print("Invalid email")
            return False

    except smtplib.SMTPAuthenticationError: #Исключение на случай ошибки авторизации от смтп
            print("Wrong email or pasword")
            return False
    return yag





#Запуск программы
if __name__ == "__main__":       
    app = QtWidgets.QApplication([])

    with open("data.json", "r") as read_file:
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

        except smtplib.SMTPAuthenticationError: #Исключение на случай ошибки авторизации от смтп
            print("Неверный логин или пароль")
            errorLogin = True
            application = MyWin()


            
    else:
        application = MyWin()

    application.show()
    sys.exit(app.exec())


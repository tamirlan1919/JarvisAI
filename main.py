import random
import sys
import wolframalpha
import functional
import pyttsx3
import speech_recognition as sr
from PyQt5 import QtCore, QtGui, QtWebEngineWidgets
from PyQt5 import QtWidgets


# Инициализируем SAPI5
engine = pyttsx3.init()
# Получение списка голосов
voices = engine.getProperty('voices')
# Установка русского языка
engine.setProperty('voice', 'eng')
# Добавляем распознавание речи Google
r = sr.Recognizer()
# Получаем html шаблон для сообщений в окне чата
htmlcode='<div class="robot">Чем я могу помочь?</div>';
f=open('index.html','r',encoding='UTF-8')
htmltemplate=f.read()
f.close()
#Работаем с Wolframaplha

client = wolframalpha.Client('52HHA3-8QTWVTA53Q')

for voice in voices:
    if voice.name == 'Elena':
        engine.setProperty('voice', voice.id)
    else:
        pass
    # Получение доступа к микрофону

text = ''


def record_volume():
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source, duration=0.5)  # настройка посторонних шумов
        print('Слушаю...')
        audio = r.listen(source)
    print('Услышала.')
    try:

        query = r.recognize_google(audio, language='ru-RU')

        text = query.lower()
        query = text
        ui.plainTextEdit.setPlainText(query)

        # engine.say('Вы сказали '+ query)
        # engine.runAndWait()
    except sr.UnknownValueError:
        return record_volume()
    except sr.RequestError:
        print('У меня нет доступа к серверам Google, для распознования вашей команды')

    return query


def start():
    myquestion(record_volume())


def stop():
    engine.stop()


def quit():  # функция выхода из программы

    x = ['Тамирлан, жаль что ты уходишь', 'рада была помочь', 'всегда к вашим услугам']  # Несколько вариаций
    engine.say(random.choice(x))  # Проговорить переменную x с помощью биб pyttsx3
    engine.runAndWait()
    engine.stop()
    exit(0)  # завершение


def AI(command):
    pass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(937, 519)
        MainWindow.setStyleSheet("background-color: #22222e")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 360, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color: #22222e;\n"
                                      "border: 2px solid #f66867;\n"
                                      "border-radius: 25%;\n"
                                      "color:white;\n"
                                      "}\n"
                                      "QPushButton::hover\n"
                                      "{\n"
                                      "    background-color:silver;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed\n"
                                      "{\n"
                                      "    background-color:red;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 120, 360, 49))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "background-color: #22222e;\n"
                                        "border: 2px solid #f66867;\n"
                                        "border-radius: 25%;\n"
                                        "color:white;\n"
                                        "}\n"
                                        "QPushButton::hover\n"
                                        "{\n"
                                        "    background-color:silver;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed\n"
                                        "{\n"
                                        "    background-color:red;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 200, 360, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "background-color: #22222e;\n"
                                        "border: 2px solid #f66867;\n"
                                        "border-radius: 25%;\n"
                                        "color:white;\n"
                                        "}\n"
                                        "QPushButton::hover\n"
                                        "{\n"
                                        "    background-color:silver;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed\n"
                                        "{\n"
                                        "    background-color:red;\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 290, 360, 310))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: white;\n"
                                         "border: 2px solid #f66867;\n"
                                         "border-radius: 25%;\n"
                                         "color:black;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 260, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
                                 "color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(430, 10, 900, 581))
        self.textEdit.setStyleSheet("background-color: white;\n"
                                    "border: 2px solid #f66867;\n"
                                    "border-radius: 25%;\n"
                                    "color:black;font-size:16px;")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Слушать"))
        self.pushButton_2.setText(_translate("MainWindow", "Остановить"))
        self.pushButton_3.setText(_translate("MainWindow", "Выход"))
        self.label.setText(_translate("MainWindow", "Вы сказали:"))
        self.label_2.setText(_translate("MainWindow", "Информация:"))


def myquestion(command):

    if 'привет' in command:
        engine.say('Привет человек')
        engine.runAndWait()
    elif 'погода' in command:
        engine.say('Вот погода на ближайшие дни')
        engine.runAndWait()
        ui.textEdit.load(QtCore.QUrl('https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&sxsrf=ALeKk014aEh7iR8XI88ApKajO8NYopJYuw%3A1618161291608&ei=iy5zYJXNJOLGrgTJw5uwDw&oq=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQsAMQJzIHCCMQsAMQJzIHCCMQsAMQJzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwA1AAWABgkowCaABwAXgAgAFPiAGdAZIBATKYAQCqAQdnd3Mtd2l6yAEKwAEB&sclient=gws-wiz'))
    elif 'время' in command:
        functional.time()
        ui.textEdit.load(QtCore.QUrl('https://www.google.com/search?q=%D0%B2%D1%80%D0%B5%D0%BC%D1%8F&oq=dhtv&aqs=chrome.1.69i57j0i1i10l5j46i1i10j0i1i10l3.1449j0j7&sourceid=chrome&ie=UTF-8'))
    elif 'запусти' in command:
        functional.zapusti(command)
    elif 'ютуб'  in command:
        ui.textEdit.load(QtCore.QUrl('https://youtube.com'))

    elif 'ринх' in command:
        engine.say("Ростовский государственный университет находится на улице Большая Садовая ул., 69, Ростов-на-Дону")
        engine.say("Открываю официальный сайт")
        engine.runAndWait()
        ui.textEdit.load(QtCore.QUrl('https://rsue.ru'))
        ui.textEdit.load
    else:
        #res = client.query(command)
        #answer = next(res.results).text
        print('answer')


while True:
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.resize(1340, 615)
    ui.pushButton.clicked.connect(start)
    ui.pushButton_2.clicked.connect(stop)
    ui.pushButton_3.clicked.connect(quit)
    sys.exit(app.exec_())

import json
import random
import sys
import webbrowser

import pyttsx3
import speech_recognition as sr
import wolframalpha
from PyQt5 import QtCore, QtGui, QtWebEngineWidgets
from PyQt5 import QtWidgets
from translate import Translator

import functional

translator = Translator(from_lang="ru", to_lang="eng")
translator2 = Translator(from_lang="eng", to_lang="ru")
# Инициализируем SAPI5
engine = pyttsx3.init()
# Получение списка голосов
voices = engine.getProperty('voices')
# Установка русского языка
engine.setProperty('voice', 'eng')
# Добавляем распознавание речи Google
r = sr.Recognizer()

# Получаем html шаблон для сообщений в окне чата
htmlcode = '<div class="robot">Что вас интересует? </div>';
engine.say(htmlcode)
engine.runAndWait()

f = open('index.html', 'r', encoding='UTF-8')
htmltemplate = f.read()
f.close()

# Работаем с Wolframaplha

client = wolframalpha.Client('52HHA3-8QTWVTA53Q')

file = open('base.json', 'r').read()

for voice in voices:
    if voice.name == 'Elena':
        engine.setProperty('voice', voice.id)
    else:
        pass
    # Получение доступа к микрофону

global text


def record_volume():
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source, duration=0.5)  # настройка посторонних шумов
        print('Слушаю...')
        engine.say('Слушаю')
        engine.runAndWait()
        audio = r.listen(source)
    print('Услышала.')
    engine.say('Услышала')
    engine.runAndWait()
    try:

        query = r.recognize_google(audio, language='ru-RU')

        text = query.lower()
        # query = text

        # engine.say('Вы сказали '+ query)
        # engine.runAndWait()
    except sr.UnknownValueError:
        return record_volume()
    except sr.RequestError:
        print('У меня нет доступа к серверам Google, для распознования вашей команды')

    return text


def start():
    myquestion(record_volume())


def send():
    engine.say(
        'Привет пользователь это дема кнопка, а так меня зовут Jarvis я мини искусственный интелект и голосовой помощник, вскорем времени я надеюсь что мой разработчик ТамИрлан меня улучшит, вместо этой кнопки будет выступать сайт с информацие обо мне')
    engine.runAndWait()
    addyouphrasetohtml('О нас')
    addrobotphrasetohtml(
        'Привет пользователь это дема кнопка, а так меня зовут Jarvis я мини искусственный интелект и голосовой помощник, вскорем времени я надеюсь что мой разработчик Тамирлан меня улучшит, вместо этой кнопки будет выступать сайт с информацие обо мне')


def quit():  # функция выхода из программы

    x = ['Тамирлан, жаль что ты уходишь', 'рада была помочь', 'всегда к вашим услугам']  # Несколько вариаций
    engine.say(random.choice(x))  # Проговорить переменную x с помощью биб pyttsx3
    engine.runAndWait()
    engine.stop()
    exit(0)  # завершение


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
        self.textEdit2 = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.textEdit2.setGeometry(QtCore.QRect(10, 290, 360, 310))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.textEdit2.setFont(font)
        self.textEdit2.setStyleSheet("background-color: white;\n"
                                     "border: 2px solid #f66867;\n"
                                     "border-radius: 25%;\n"
                                     "color:black;")
        self.textEdit2.setObjectName("plainTextEdit")
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
        self.pushButton.setText(_translate("MainWindow", "Старт"))
        self.pushButton_2.setText(_translate("MainWindow", "О нас"))
        self.pushButton_3.setText(_translate("MainWindow", "Выход"))
        self.label.setText(_translate("MainWindow", "Чат:"))
        self.label_2.setText(_translate("MainWindow", "Информация:"))


def addrobotphrasetohtml(phrase):
    global htmltemplate
    global htmlcode
    htmlcode = '<div class="robot">' + phrase + '</div>' + htmlcode
    htmlresult = htmltemplate.replace('%code%', htmlcode)
    ui.textEdit2.setHtml(htmlresult, QtCore.QUrl("file://"));
    ui.textEdit2.show()


# Добавление в html чат фразы пользователя
def addyouphrasetohtml(phrase):
    global htmltemplate
    global htmlcode
    htmlcode = '<div class="you">' + phrase + '</div>' + htmlcode
    htmlresult = htmltemplate.replace('%code%', htmlcode)
    ui.textEdit2.setHtml(htmlresult, QtCore.QUrl("file://"));
    ui.textEdit2.show()


def AI(command):
    pars = json.loads(file)
    if command in pars:
        z = random.choice(pars[command])
        dlina = len(z)
        if dlina > 1:
            engine.say(z)
            engine.runAndWait()
            addrobotphrasetohtml(z)
        else:
            z = pars[command]
            engine.say(z)
            engine.runAndWait()
            addrobotphrasetohtml(z)
    else:
        engine.say('я не знаю как на это отвечать, научите меня')
        engine.runAndWait()
        with open('base.json', 'r') as json_file:
            pars = json.load(json_file)
        engine.say('Задайте вопрос')
        engine.runAndWait()
        a = record_volume()
        engine.say('скажите как я должен ответить на это')
        engine.runAndWait()
        b = record_volume()
        pars[a] = b
        with open('base.json', 'w') as json_file:
            json.dump(pars, json_file, indent=2, sort_keys=True, ensure_ascii=False)


def myquestion(command):
    addyouphrasetohtml(command)
    if 'пока' in command:
        engine.say('До свидания  человек')
        engine.runAndWait()
        addrobotphrasetohtml('До свидания  человек')
        quit()
    elif 'погода' in command:
        engine.say('Вот погода на ближайшие дни')
        engine.runAndWait()
        ui.textEdit.load(QtCore.QUrl(
            'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&sxsrf=ALeKk014aEh7iR8XI88ApKajO8NYopJYuw%3A1618161291608&ei=iy5zYJXNJOLGrgTJw5uwDw&oq=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQsAMQJzIHCCMQsAMQJzIHCCMQsAMQJzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwA1AAWABgkowCaABwAXgAgAFPiAGdAZIBATKYAQCqAQdnd3Mtd2l6yAEKwAEB&sclient=gws-wiz'))
        addrobotphrasetohtml('Вот погода на ближайшие дни')
    elif ('время' in command) or ('текущее время' in command):
        functional.time()
        ui.textEdit.load(QtCore.QUrl(
            'https://www.google.com/search?q=%D0%B2%D1%80%D0%B5%D0%BC%D1%8F&oq=dhtv&aqs=chrome.1.69i57j0i1i10l5j46i1i10j0i1i10l3.1449j0j7&sourceid=chrome&ie=UTF-8'))
        addrobotphrasetohtml('Вот ответ')
    elif ('запусти' in command):
        functional.zapusti(command)
        addrobotphrasetohtml('Запустил')
    elif ('ютуб' in command) or ('youtube' in command):
        ui.textEdit.load(QtCore.QUrl('https://youtube.com'))
        addrobotphrasetohtml('Вот ответ')

    elif ('ринх' in command) or ('универ' in command):
        engine.say("Ростовский государственный университет находится на улице Большая Садовая ул., 69, Ростов-на-Дону")
        engine.say("Открываю официальный сайт")
        engine.runAndWait()
        ui.textEdit.load(QtCore.QUrl('https://rsue.ru'))
        ui.textEdit.load
        addrobotphrasetohtml('Вот ответ')
    elif ('открой почту' in command) or ('почта' in command):
        engine.say('Сделано')
        engine.runAndWait()
        ui.textEdit.load(QtCore.QUrl('https://mail.ru'))
        addrobotphrasetohtml('Открыл')
    elif ('открой вконтакте' in command) or ('открой vk' in command):
        ui.textEdit.load(QtCore.QUrl('https://vk.com'))
        addrobotphrasetohtml('Открыл')
    elif ('включи музыку' in command) or ('музыка' in command):
        ui.textEdit.load(QtCore.QUrl('https://vk.com/audios265260473'))
        addrobotphrasetohtml('Включил')
    elif 'посмотреть фильм' in command:
        webbrowser.open('https://www.film.ru/online')
        addrobotphrasetohtml('Вот ответ')
    elif ('новости' in command) or ('текущие новости' in command):
        engine.say('Вот такие новости в РостОве')
        engine.runAndWait()
        ui.textEdit.load(QtCore.QUrl('https://161.ru/'))
        addrobotphrasetohtml('Вот такие новости в Ростове')
    elif ('расскажи анекдот' in command) or ('анекдот' in command):
        z = functional.anekdot()
        engine.say(z)
        engine.runAndWait()
        addrobotphrasetohtml(z)
    elif 'вызвать такси' in command:
        webbrowser.open('https://taxi.yandex.ru/')
        addrobotphrasetohtml('вот ответ')
    elif ('перевести' in command) or ('переводчик' in command):
        engine.say('перевести с английского или русского языка')
        engine.runAndWait()
        z = record_volume()
        if 'с русского' in z:
            engine.say('Скажите что перевести')
            engine.runAndWait()
            word = record_volume()
            end_text = translator.translate(word)
            addrobotphrasetohtml(end_text)
            engine.say(end_text)
            engine.runAndWait()

        else:
            engine.say('Скажите что перевести')
            engine.runAndWait()
            word = record_volume()
            end_text = translator2.translate(word)

            addrobotphrasetohtml(end_text)
            engine.say(end_text)
            engine.runAndWait()
            # addrobotphrasetohtml(end_text)
    elif ('найти' in command) or ('найди' in command):
        words = (
            'найди', 'найти', 'ищи', 'кто такой',
            'что такое', 'о том')  # Создание словаря с ключевыми словами для выполнения запроса
        remove = ["пожалуйста", "ладно", "давай", "сейчас"]  # Создание списка со слов которые будут удалены из запроса
        for i in words:  # Создание цикла для очистки слов находящихся в словаре words в запросе
            command = command.replace(i, '')  # Очистка ключевых слов, находящихся в словаре words с запроса
            for j in remove:  # Создание цикла для очистки слов находящихся в списке remove в запросе
                command = command.replace(j, '')  # Очистки слов находящихся в списке remove в запросе
                command = command.strip()  # Преобразование переменной search в строку

        ui.textEdit.load(QtCore.QUrl(
            f'https://www.google.com/search?q={command}&oq={command}'f'81&aqs=chrome..69i57j46i131i433j0l5.2567j0j7&sourceid=chrome&ie=UTF-8'))  # выполнение запроса в браузере
        addrobotphrasetohtml('вот ответ')
    elif 'список команд' in command:
        webbrowser.open('list.html')
    else:
        AI(command)

    # Добавление ответов


while True:
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.resize(1340, 615)
    ui.pushButton.clicked.connect(start)
    ui.pushButton_2.clicked.connect(send)
    ui.pushButton_3.clicked.connect(quit)
    sys.exit(app.exec_())

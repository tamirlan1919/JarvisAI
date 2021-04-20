# Чистит фразу от ключевых слов

import datetime
import subprocess

import bs4
import pyttsx3
import re
import requests
import webbrowser

# from main import  *
engine = pyttsx3.init()


# Очистка ключевых фраз
def cleanphrase(statement, spisok):
    for x in spisok:
        statement = statement.replace(x, '')
    statement = statement.strip()
    return statement


def osrun(cmd):
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)


def openurl(url):
    webbrowser.open(url)


def anekdot():
    s = requests.get('http://anekdotme.ru/random')
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p = b.select('.anekdot_text')
    s = (p[0].getText().strip())
    reg = re.compile('[^0-9a-zA-Zа-яА-я .,!?-]')
    s = reg.sub('', s)
    return (s)


def zapusti(statement):
    ot = 'Такой команды я пока не знаю'
    statement = cleanphrase(statement, ['запусти', 'запустить', 'открой'])
    if ((statement.find("калькулятор") != -1) or (statement.find("calculator") != -1)):
        osrun('calc')
        ot = 'Калькулятор запущен'
    if ((statement.find("блокнот") != -1) or (statement.find("notepad") != -1)):
        osrun('notepad')
        ot = 'Блокнот запущен'
    if ((statement.find("paint") != -1) or (statement.find("паинт") != -1)):
        osrun('mspaint')
        ot = 'Графический редактор запущен'
    if ((statement.find("browser") != -1) or (statement.find("браузер") != -1)):
        openurl('http://google.ru')
        ot = 'Запускаю браузер'
    if ((statement.find("проводник") != -1) or (statement.find("файловый менеджер") != -1)):
        osrun('explorer')
        ot = 'Проводник запущен'
    return ot


def time():
    now = datetime.datetime.now()
    engine.say("Сейчас " + str(now.hour) + ":" + str(now.minute))
    # k = "Сейчас " + str(now.hour) + ":" + str(now.minute)
    engine.runAndWait()
    engine.stop()

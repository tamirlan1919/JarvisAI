# Чистит фразу от ключевых слов
import urllib

import requests, bs4, re, webbrowser
import os, sys, subprocess
from urllib import request
from urllib.parse import quote
import urllib.request
import html2text
import datetime
import pyttsx3

engine = pyttsx3.init()
#Очистка ключевых фраз
def cleanphrase(statement, spisok):
    for x in spisok:
        statement=statement.replace(x, '')
    statement=statement.strip()
    return statement

def osrun(cmd):
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)

def openurl(url):
    webbrowser.open(url)

def zapusti(statement):
    ot='Такой команды я пока не знаю'
    statement=cleanphrase(statement,['запусти', 'запустить'])
    if((statement.find("калькулятор")!=-1) or (statement.find("calculator")!=-1)):
        osrun('calc')
        ot='Калькулятор запущен'
    if((statement.find("блокнот")!=-1) or (statement.find("notepad")!=-1)):
        osrun('notepad')
        ot='Блокнот запущен'
    if((statement.find("paint")!=-1) or (statement.find("паинт")!=-1)):
        osrun('mspaint')
        ot='Графический редактор запущен'
    if((statement.find("browser")!=-1) or (statement.find("браузер")!=-1)):
        openurl('http://google.ru')
        ot='Запускаю браузер'
    if((statement.find("проводник")!=-1) or (statement.find("файловый менеджер")!=-1)):
        osrun('explorer')
        ot='Проводник запущен'
    return ot

def time():
    now = datetime.datetime.now()
    engine.say("Сейчас " + str(now.hour) + ":" + str(now.minute))
    #k = "Сейчас " + str(now.hour) + ":" + str(now.minute)
    engine.runAndWait()
    engine.stop()

def mysearch(z):
    doc = urllib.request.urlopen('http://go.mail.ru/search?fm=1&q='+quote(z)).read().decode('unicode-escape',errors='ignore')
    sp=re.compile('title":"(.*?)orig').findall(doc)
    mas1=[]
    mas2=[]
    for x in sp:
        if((x.rfind('wikihow')==-1) and (x.rfind('an.yandex')==-1) and (x.rfind('wikipedia')==-1) and (x.rfind('otvet.mail.ru')==-1) and (x.rfind('youtube')==-1) and(x.rfind('.jpg')==-1) and (x.rfind('.png')==-1) and (x.rfind('.gif')==-1)):
            a=x.replace(',','')
            a=a.replace('"','')
            a=a.replace('<b>','')
            a=a.replace('</b>','')
            a=a.split('url:')
            if(len(a)>1):
                z=a[0].split('}')
                mas1.append(z[0])
                z=a[1].split('}')
                z=z[0].split('title')
                mas2.append(z[0])
    return mas2

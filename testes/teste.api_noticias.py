from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import pyaudio
import os
import sys
from datetime import datetime 
import webbrowser as browser
import pyautogui
import time
from requests import get
from bs4 import BeautifulSoup


site = get('https://news.google.com/news/rss?ned=pt_br&gl=BR&hl=pt')
noticias = BeautifulSoup(site.text, 'lxml-xml')  # Usando o analisador XML
for item in noticias.find_all('item')[:4]:
    mensagem = item.title.text
    print(mensagem)

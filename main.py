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


def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)

cria_audio('audios/welcome.mp3','Olá sou Ada sua assistente virtual. Em que posso ajudar?')

#-----------------------------------------------------#
def monitora_audio():
    recon = sr.Recognizer()

    with sr.Microphone() as source:
        while True:
            print('Diga algo')
            audio = recon.listen(source)
            try:
                mensagem = recon.recognize_google(audio, language='pt-br')
                mensagem = mensagem.lower()
                executa_comando(mensagem)
                break
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
        return mensagem

#-----------------------------------------------------#
def executa_comando(mensagem):
    if 'fechar assistente' in mensagem:
        sys.exit()
    elif 'horas' in mensagem:
        hora = datetime.now().strftime('%H:%M')
        frase = f'Agora são {hora}'
        cria_audio('audios/mensagem.mp3', frase)
    elif 'desligar computador' and 'uma hora' in mensagem:
        os.system('shutdown -s -t 3600')
    elif 'desligar computador' and 'meia hora' in mensagem:
        os.system('shutdown -s -t 1800')
    elif 'cancelar desligamento' in mensagem:
        os.system('shutdown -a')
    elif 'toca' and 'vampiro' in mensagem:
        tocar_musicas('vampiro')
        cria_audio('audios/mensagem.mp3','Tocando Vampiro no Spotify')
    elif 'notícias' in mensagem:
        ultimas_noticias()

#-----------------------------------------------------#
def ultimas_noticias():
    site = get('https://news.google.com/news/rss?ned=pt-br&gl=BR&hl=pt')
    noticias = BeautifulSoup(site.text, 'lxml-xml')  # Usando o analisador XML
    for item in noticias.find_all('item')[:4]:
        mensagem = item.title.text
        cria_audio('audios/mensagem.mp3',mensagem)

#-----------------------------------------------------#
def tocar_musicas(musica):
    if musica == 'vampiro':
        browser.open("https://open.spotify.com/intl-pt/track/6bTdZ7xfKp3NqqADJ8HLyj?si=14c5e310956047d5")

#-----------------------------------------------------#

def main():
    while True:
        monitora_audio()

main()

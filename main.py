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
import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
from random import randint
import json



headers = CaseInsensitiveDict()
headers['Accept'] = 'application/json'
headers['Authorization'] = 'Bearer live_6bb50dbeb75a454dc38b14a1c1a13b'
url ='https://api.api-futebol.com.br/v1/campeonatos/10/tabela'

#-----------------------------------------------------#
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
        print('Desligando Ada')
        sys.exit()
    elif 'horas' in mensagem:
        hora = datetime.now().strftime('%H:%M')
        frase = f'Agora são {hora}'
        cria_audio('audios/mensagem.mp3', frase)
    elif 'desligar computador' in mensagem and 'uma hora' in mensagem:
        os.system('shutdown -s -t 3600')
    elif 'desligar computador' in mensagem and 'meia hora' in mensagem:
        os.system('shutdown -s -t 1800')
    elif 'cancelar desligamento' in mensagem:
        os.system('shutdown -a')
    elif 'toca' in mensagem and 'vampiro' in mensagem:
        tocar_musicas('vampiro')
        cria_audio('audios/mensagem.mp3','Tocando Vampiro no Spotify')
    elif 'notícias' in mensagem:
        ultimas_noticias()
    elif 'jogo de adivinhação' in mensagem:
        jogo_adivinhacao()
    elif 'cotação' in mensagem and 'dólar' in mensagem:
        cotacao_moeda('Dólar')
    elif 'cotação' in mensagem and 'euro' in mensagem:
        cotacao_moeda('Euro')
    elif 'cotação' in mensagem and 'bitcoin' in mensagem:
        cotacao_moeda('Bitcoin')
    elif 'times' in mensagem and 'libertadores' or 'primeiras colocações' in mensagem:
        lista_g6()
    elif 'times' in mensagem and 'zona de rebaixamento' in mensagem:
        lista_rebaixamento()

#-----------------------------------------------------#
def jogo_adivinhacao():
    cria_audio('audios/adivinha.mp3','Escolha um número entre 1 a 10')
    recon = sr.Recognizer()

    with sr.Microphone() as source:
        print('Diga algo')
        audio = recon.listen(source) #Ouve o que for dito na captura de audio

    numero = recon.recognize_google(audio,language="pt-br")
    resultado = randint(1,10)

    if numero == str(resultado):
        cria_audio('audios/venceu.mp3', 'Parabéns! Você adivinhou o número.')
    else:
        mensagem = f'Que pena! Você errou, o número era {resultado}.'
        cria_audio('audios/perdeu.mp3', mensagem)

#-----------------------------------------------------#
def ultimas_noticias():
    site = get('https://news.google.com/news/rss?ned=pt-br&gl=BR&hl=pt')
    noticias = BeautifulSoup(site.text, 'lxml-xml')  # Usando o analisador XML
    for item in noticias.find_all('item')[:4]:
        mensagem = item.title.text
        cria_audio('audios/mensagem.mp3',mensagem)

#-----------------------------------------------------#
def cotacao_moeda(moeda):
    if moeda == 'Dólar':
        requisicao = get('https://economia.awesomeapi.com.br/all/USD-BRL')
        cotacao = requisicao.json()
        nome = cotacao['USD']['name']
        data = cotacao['USD']['create_date']
        valor = cotacao['USD']['bid']
        mensagem = f'Cotação do {nome} em {data} é {valor} reais.'
        cria_audio('audios/mensagem.mp3',mensagem)
    elif moeda == 'Euro':
        requisicao = get('https://economia.awesomeapi.com.br/all/EUR-BRL')
        cotacao = requisicao.json()
        nome = cotacao['EUR']['name']
        data = cotacao['EUR']['create_date']
        valor = cotacao['EUR']['bid']
        mensagem = f'Cotação do {nome} em {data} é {valor} reais.'
        cria_audio('audios/mensagem.mp3',mensagem)
    elif moeda == 'Bitcoin':
        requisicao = get('https://economia.awesomeapi.com.br/all/BTC-BRL')
        cotacao = requisicao.json()
        nome = cotacao['BTC']['name']
        data = cotacao['BTC']['create_date']
        valor = cotacao['BTC']['bid']
        mensagem = f'Cotação do {nome} em {data} é {valor} reais.'
        cria_audio('audios/mensagem.mp3',mensagem)

#-----------------------------------------------------#
def tocar_musicas(musica):
    if musica == 'vampiro':
        browser.open("https://open.spotify.com/intl-pt/track/6bTdZ7xfKp3NqqADJ8HLyj?si=14c5e310956047d5")

#-----------------------------------------------------#
def lista_g6():
    response = requests.get(url, headers=headers)
    classificacao = json.loads(response.text)
    for g6 in classificacao[:6]:
        times = g6['time']['nome_popular']
        cria_audio('audios/mensagem.mp3', times)

def lista_rebaixamento():
    response = requests.get(url, headers=headers)
    classificacao = json.loads(response.text)
    for z4 in classificacao[-4:]:
        times = z4['time']['nome_popular']
        cria_audio('audios/mensagem.mp3', times)

#-----------------------------------------------------#

def main():
    while True:
        monitora_audio()

main()

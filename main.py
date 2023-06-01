from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import pyaudio
import os
import sys
from datetime import datetime 



def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)

cria_audio('audios/welcome.mp3','Olá sou Ada sua assistente virtual. Em que posso ajudar?')

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

def main():
    while True:
        monitora_audio()

main()

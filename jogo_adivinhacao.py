import speech_recognition as sr
import pyaudio
from gtts import gTTS
from playsound import playsound
from random import randint



#Modo reconhecimento de voz
def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)

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

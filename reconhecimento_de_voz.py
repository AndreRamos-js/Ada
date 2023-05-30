import speech_recognition as sr
import pyaudio
from gtts import gTTS
from playsound import playsound



#Modo reconhecimento de voz
def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)

cria_audio('audios/welcome.mp3','Olá sou Ada sua assistente virtual. Em que posso ajudar?')

recon = sr.Recognizer()

with sr.Microphone() as source:
    print('Diga algo')
    audio = recon.listen(source) #Ouve o que for dito na captura de audio

frase = recon.recognize_google(audio,language="pt-br")
cria_audio('audios/mensagem.mp3',frase)

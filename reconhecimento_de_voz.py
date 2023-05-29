import speech_recognition as sr
import pyaudio
from gtts import gTTS
from playsound import playsound



'''
#Modo reconhecimento de voz
recon = sr.Recognizer()

with sr.Microphone() as source:
    print('Diga algo')
    audio = recon.listen(source) #Ouve o que for dito na captura de audio

print(recon.recognize_google(audio, language='pt-br'))
'''


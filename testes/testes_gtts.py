from gtts import gTTS
from playsound import playsound



'''
def cria_audio(mensagem):
    tts = gTTS (text=mensagem, lang="pt-br")
    tts.save("hello.mp3")
    playsound("hello.mp3")
'''
    
'''
Ultilização simples

cria_audio('Olá eu sou o Jarvis seu assistente!')
'''

'''
Ultilização via entrada de dados

frase = input('Digite algo a ser falado: \n')
cria_audio(frase)
'''
'''
arquivo = open("frase.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
cria_audio(conteudo)
'''

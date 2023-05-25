import pyttsx3



'''
Testando sintetização de voz por mensagem pré definida

engine = pyttsx3.init()
engine.setProperty("voice","brazil")
engine.say ('Eu sou o Jarvis')
engine.runAndWait()
'''

'''
Testando sintetização de voz por mensagem recebida

engine = pyttsx3.init()
engine.setProperty("voice","brazil")
frase = input('Digite a frase a ser falada:\n')
engine.say(frase)
engine.runAndWait()
'''

'''
Testando sintetização de voz por arquivo de texto

engine = pyttsx3.init()
engine.setProperty("voice","brazil")
arquivo = open("frase.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
print(conteudo)
engine.say(conteudo)
engine.runAndWait()
'''

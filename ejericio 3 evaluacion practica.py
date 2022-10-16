from gtts import gTTS
import os

file = open("ejercicio 3 evaluacion practica.txt", "r").read().replace("\n", " ")

language = 'es-us'

speech = gTTS(text = str(file), lang = language, slow = False)

speech.save("ejercicio 3 evalacion practica.mp3")

os.system("ejercicio 3 evalacion practica.mp3")
import random

from io import open

from werkzeug.security import generate_password_hash

minus = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "@()[]{}*,;/-_¿?.¡!$<#>&+%="
mayus = minus.upper()


base = minus+mayus+numeros+simbolos
longitud = 8

for _ in range(1):
    muestra = random.sample(base, longitud)
    password = "".join(muestra)
    password_encriptado = generate_password_hash(password)
    print("{} => {}".format(password, password_encriptado))

archivo_texto = open("ejercicio-1-evaluacion-practica.txt","w")
archivo_texto = open("ejercicio-1-evaluacion-practica.txt", "r")
texto = archivo_texto.read()
archivo_texto.close()
print(texto)

archivo_texto= open("ejercicio-1-evaluacion-practica.txt", "r")
lineas_texto = archivo_texto.readline()
archivo_texto.close()
print(lineas_texto)

archivo_texto = open("ejercicio-1-evaluacion-practica.txt", "a")
archivo_texto.write("{} => {}".format(password, password_encriptado))
archivo_texto.close()

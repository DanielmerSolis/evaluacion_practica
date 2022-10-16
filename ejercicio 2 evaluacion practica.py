from io import open

archivo_texto = open("ejercicio 2 evaluacion practica.txt","w")

Expresion = "Buen momento para estudiar en la USTA \n y estudiar Ingenieria Informática"

archivo_texto.write(Expresion)

archivo_texto.close()


archivo_texto = open("ejercicio 2 evaluacion practica.txt", "r")

texto = archivo_texto.read()

archivo_texto.close()

print(texto)

archivo_texto = open("ejercicio 2 evaluacion practica.txt", "r")

lineas_texto = archivo_texto.readline()

archivo_texto.close()

print(lineas_texto[2])

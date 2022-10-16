import pytesseract
import sys
import os
from pdf2image import convert_from_path

filename = 'imagen con texto.jpg'
outfile = 'texto de imagen.txt'

f = open(outfile, "a")
text = str(((pytesseract.image_to_string(Image.open(filename)))))
text = text.replace('-\n', '')
f.write(text)
f.close()
print("Finalizado")

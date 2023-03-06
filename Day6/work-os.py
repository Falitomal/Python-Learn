import os
from pathlib import Path
ruta = os.getcwd()
os.mkdir('test')
os.chdir('test')
print(os.getcwd())
file = open('test.txt', 'w')
file.write('Hola mundo')
file.close()
file = open('test.txt', 'r')
print(file.read())
print(ruta)
carpeta = Path('D:/Cursos/test')
archivo = carpeta / 'test2.txt'
miarchivo = open(archivo, 'w')

miarchivo.write('Hola mundtest')
miarchivo.close()
miarchivo = open(archivo, 'r')
print(miarchivo.read())
miarchivo.close()

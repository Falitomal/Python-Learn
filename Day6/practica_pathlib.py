from pathlib import Path

carpeta = Path("D:\Cursos\Python-Learn\Day6\prueba.txt")
if carpeta.exists():
    print("El archivo existe y continene lo siguiente: \n")
    print(carpeta.read_text())
else:
    print("El archivo no existe")

base = Path.home()
guia = Path( base, 'Ruta_Nueva', 'Espana', "guia.txt")

print(guia)

busqueda = Path(carpeta.parent.parent.parent)

print(f'Buscamos en {busqueda} , todos los archivos txt')
for txt in busqueda.glob('**/*.txt'):
    print(txt)
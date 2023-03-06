mi_archivo = open("D:\Cursos\Python-Learn\Day6\prueba.txt", "r")

print(mi_archivo.read())

mi_archivo.close()

mi_archivo = open("D:\Cursos\Python-Learn\Day6\prueba.txt", "a")

mi_archivo.write("Nueva linea agregada\n")
mi_archivo.close()

mi_archivo = open("D:\Cursos\Python-Learn\Day6\prueba.txt", "r")
print(mi_archivo.read())
mi_archivo.close()
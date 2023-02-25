from random import *

colores = ['azul', 'verde', "amarillo"]
aletorio_color = choice(colores)
aleatorio = randint(1,10)

print(f"un numero aleatorio es : {aleatorio}")
print(f"un color aleatorio es : {aletorio_color}")

numeros = list(range(1, 50,5))
shuffle(numeros)

print(numeros)

numrandom = random()
print(f"un number random between 0 and 1 : {numrandom}")
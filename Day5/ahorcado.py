from random import choice
# Juego del ahorcado
lista_palabras = ['python', 'java', 'kotlin', 'javascript', 'Typescript', "VisualBasic", "React", "Angular", "Vue", "Android", "Windows", "Linux", "MacOS", "Ubuntu", "Debian", "Arch", "Manjaro", "Fedora", "CentOS"] 
letras_correctas = []
letra_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


def elige_palabra(lista_palabras):
	palabra_elegida = choice(lista_palabras)
	palabra_elegida = palabra_elegida.lower()
	letras_unicas = len(set(palabra_elegida))
	return palabra_elegida, letras_unicas

def pedir_letra():
	pedir_letra = ''
	es_valida = False
	letra_elegida = ''
	abecedario = 'abcdefghijklmnñopqrstuvwxyz'

	while not es_valida:
		letra_elegida = input("Elige una letra: ").lower()
		if letra_elegida in abecedario and len(letra_elegida) == 1:
			es_valida = True
		else:
			print("No es valida pon una letra")
	
	return letra_elegida

def mostrar_tablero(palabra_elegida):
	lista_oculta = []

	for i in palabra_elegida:
		if i in letras_correctas:
			lista_oculta.append(i)
		else:
			lista_oculta.append('-')
	print(" ".join(lista_oculta))

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):

	fin = False

	if letra_elegida in palabra_oculta:
		letras_correctas.append(letra_elegida)
		coincidencias += 1
	else:
		letra_incorrectas.append(letra_elegida)
		vidas -= 1

	if vidas == 0:
		fin = perder()
	elif coincidencias == letras_unicas:
		fin = ganar(palabra_oculta)
		
	return vidas, fin, coincidencias

def perder():
	print("\n" * 5 +  "*" * 30 + "\n")
	print("Perdiste te has queda sin intentos")
	print(f"La palabra era {palabra}")
	print("\n" * 5 +  "*" * 30 + "\n")
	return True

def ganar(palabra_descubierta):
	mostrar_tablero(palabra_descubierta)
	print("\n" * 5 +  "*" * 30 + "\n")
	print("Ganaste! la palabra era: ", palabra_descubierta)
	print("\n" * 5 +  "*" * 30 + "\n")
	return True
	
palabra, letras_unicas = elige_palabra(lista_palabras)

while not juego_terminado:
	print("\n" + "*" * 30 + "\n")
	mostrar_tablero(palabra)
	print("\n")
	print("letras incorrectas: ", "-".join(letra_incorrectas))
	print(f"Intentos restantes: {intentos}")
	print("\n" + "*" * 30 + "\n")
	letra = pedir_letra()
	intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)
	juego_terminado = terminado


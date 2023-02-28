from random import randint

def lanzar_moneda():
	valor = randint(1,2)
	if valor == 1:
		return "Cara"
	else:
		return "Cruz"

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def probar_suerte(lanzar_moneda(), lista_numeros):
	
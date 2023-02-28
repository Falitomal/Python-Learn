from random import randint

def lanzar_moneda():
	valor = randint(1,2)
	if valor == 1:
		return "Cara"
	else:
		return "Cruz"

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lanzar_monedas = str(lanzar_moneda())

def probar_suerte(lanzar_monedas, lista_numeros):
	if lanzar_monedas == "Cara":
		print("La lista se autodestruirá")
		lista_numeros = []
		return lista_numeros
	else:
		print("La lista fue salvada")
		return lista_numeros

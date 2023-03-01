#reducir una lista que tome una lista como argumento
def reducir_lista(lista):
	lista_numeros = []
	max = 0
	for elemento in lista:
		if elemento not in lista_numeros:
			lista_numeros.append(elemento)
		if elemento > max:
			max = elemento
			
	lista_numeros.remove(max)
	return lista_numeros

def promedio(lista_reducida):
	lista_numeros = 0
	for elemento in lista_reducida:
		lista_numeros += elemento
	promedio = lista_numeros / len(lista_reducida)
	return promedio

lista_numeros = [12, 2, 3, 4, 5, 6, 7, 8, 9, 20]
lista_reducida = reducir_lista(lista_numeros)
print(lista_reducida)
print(promedio(lista_reducida))
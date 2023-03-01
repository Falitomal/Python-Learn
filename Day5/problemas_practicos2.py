#Funcion que devuelva una palabra con todas sus letras separadas y en orden alfabetico sin repetir ninguna letra
#Ejemplo: "entretenido" -> "['d', 'e', 'i', 'n', 'o', 'r', 't']"`]"

def ordena_alfabetico(palabra):
	lista = []
	for letra in palabra:
		if letra not in lista:
			lista.append(letra)
	lista.sort()
	return lista

print(ordena_alfabetico("entretenido"))
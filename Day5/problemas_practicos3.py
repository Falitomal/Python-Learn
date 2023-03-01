

#escribe una funcion que requiera una cantidad indeterminada de argumentos numericos y devuelta true si se ingresan dos 0 repetidos dos veces

def problema_duple(*args):
	contador = 0
	for i in args:
		if contador + 1 == len(args):
			return False
		elif args[contador] == 0 and args[contador+1] == 0 :
			return True
		else:
			contador += 1

	return False
	
print(problema_duple(0, 2, 1, 2, 3, 4))
print(problema_duple(0, 2, 1, 2, 3, 4, 0, 0))
#funcion suma_cuadrados que sume los cuadrados de varios args
def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma += arg ** 2
    return suma

print(suma_cuadrados(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

#funcion suma_absolutos que sume los valores absolutos de varios args
def suma_absolutos(*args):
	suma = 0
	for arg in args:
		suma += abs(arg)
	return suma

#funcion numeros_personas que reciba un primer argumento nombre y luego una cantidad indefina de numeros y retorne el nombre y la suma
def numeros_persona(nombre, *args):
	suma = 0
	for arg in args:
		suma += arg
	return print(f"{nombre}, la suma de tus números es {suma}")

print(numeros_persona("Juan", 75, 20, 65))
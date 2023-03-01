#funcion cantidad de atributos que ponga la cantidad de atributos y devuelva como resultado

def cantidad_atributos(**kwargs):
	return len(kwargs)

#funcion llama lista_atributos que duevuelva una lista con los atributos en forma de palabras clave
def lista_atributos(**kwargs):
	return list(kwargs.values())

#funcion llamada describir_persona, que tome su nombre como parametro y una serie indeterminado de argumentos
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs:
      print(f"{clave}: {valor}")
#Eliminar caracteres de una cadena ala izquierda
letes = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

letes = letes.lstrip(",:_#")
print(letes)

#Insertar en una lista en posicion 4
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(3, "naranja")
print(frutas)

#Eliminar elementos de una lista duplicados
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)

def saludar_usuario(nombre):
	'''Saluda al usuario'''
	print(f"Hola {nombre}")

saludar_usuario("Juan")
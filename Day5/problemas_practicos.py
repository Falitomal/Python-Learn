#funcion devolver mayor
def num_mayor(num1, num2, num3):
    return max(num1, num2, num3)
#funcion devolver el menor
def num_menor(num1, num2, num3):
	return min(num1, num2, num3)


#Funcion devolver distintos
def distintos(num1, num2, num3):
    suma = sum((num1, num2, num3))
    lista = [num1, num2, num3]
    
    if suma > 15:
        return num_mayor(num1, num2, num3)
    elif suma < 10:
        return num_menor(num1, num2, num3)
    else:
       lista.sort()
       return lista[1]
    
print(distintos(6, 1, 4))
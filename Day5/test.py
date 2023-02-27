def cuadrado(n):
    un_numero = n**2
    print(un_numero)
cuadrado(5)

#hacer una funcion sobre la potencia de un numero
def potencia(n1,n2):
    return n1**n2
#hacer una fucion que deveulva un valor numerico el resultado de dollar a euros
def usd_a_eur(dollar):
    dolares = dollar*0.90
    return dolares

#Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.
def usd_a_eur(dollar):
    dolares = dollar*0.90
    return dolares    
dolares = 100

#crear una funcion de invertir una cadena y ponerla mayusculas
def invertir_palabra(cadena):
    invertir = cadena[::-1]
    invertir = invertir.upper()
    return invertir
#funcion numeros positivos dentro de una lista
def todos_positivos(lista):
    for i in lista:
        if i < 0:
            return False
    return True

#crea funcion que sume numeros de la lista almacenado en var lista_numeros si son > a 0 y < a 1000, y de devuelva el resultado
def suma_menores(lista_numeros):
    suma = 0
    for i in lista_numeros:
        if i > 0 and i < 1000:
          suma += i
    return suma

lista_numeros = [100, -2, 33]
print(suma_menores(lista_numeros))

#Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
def cantidad_pares(lista_numeros):
    cantidad_pares = 0
    for i in lista_numeros:
        if i%2==0:
            cantidad_pares += 1
    return cantidad_pares
            
lista_numeros = [2, 3, 4]
print(cantidad_pares(lista_numeros))
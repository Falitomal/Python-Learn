def sumare():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(n1 + n2)
    print("Gracoas")

try:
    sumare()
except TypeError:
    print("Concatenando diferentes tipos   ")
except ValueError:
    print("No es el tipo esperado   ")

else:
    print("haz esto")

finally:
    print("Eso salio")

def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("No es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("adios")

pedir_numero()
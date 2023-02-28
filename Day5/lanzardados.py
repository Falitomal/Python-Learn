from random import *

#tarea de lanzar lanzar_dados
def lanzar_dados():
    valor1 = randint(1,6)    
    valor2 = randint(1,6)    
    return valor1, valor2


#evaluar la jugada de lanzamiento

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados > 6 and suma_dados < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

dado1, dado2 = lanzar_dados()   
evaluar_jugada(dado1, dado2)
from pathlib import Path
from os import system, os

mi_ruta = Path(Path.home(), "Recetas")

def saludar():
    print(f"Bienvenido al recetario")
    nombre = input("¿Cómo te llamas? ")
    return nombre

def contar_recetas(ruta):
    cont = 0
    for txt in Path(ruta).glob("**/*.txt"):
        cont +=1
    return cont

def mostrar_categoria(ruta):
    print(f"Estas son las categorias disponibles : ")
    categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in categorias.iterdir("*"):
        carpeta_str = str(carpeta.name)
        print(f"{contador} : Categoria : {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias

def elegir_categoria(lista):

    eleccion_coorecta = 'x'
    while not eleccion_coorecta.isnumeric() or int(eleccion_coorecta) not in range(1, len(lista) + 1):
        eleccion_coorecta = input("\n Elige una categoria:")
    return lista[int(eleccion_coorecta) - 1]

def mostrar_recetas(ruta):
    print("Recetas: ")
    laruta = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in laruta.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"{contador} : {receta_str}")
        lista_recetas.append(receta_str)
        contador +=1
    
    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = 's'
    while not eleccion_receta.isnumeric() or int(eleccion_receta) is not range(1, len(lista) + 1):
        eleccion_receta = input("\n Elige una receta: ")

    return lista[int(eleccion_receta - 1)]

def leer_receta(receta):
    print(Path.read_text(receta))
    
def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta")
        nombre_receta = input() + '.txt'
        print("Escribe la nueva receta: \n")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exist(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada ")
            existe = True
        else:
            print("Tu receta ya existe")

def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu categoria")
        nombre_categoria = input() 
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exist(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu categoria {nombre_categoria} ha sido creada ")
            existe = True
        else:
            print("Tu categoria ya existe")
#mostar menu inicio
menu = 0

if menu == 1:
    mis_categorias = mostrar_categoria(mi_ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    mi_listas_recetas = mostrar_recetas(mi_categoria)
    mi_receta = elegir_recetas(mi_listas_recetas)
    leer_receta(mi_receta)
    #volver a inicio
    pass
elif menu == 2:
    mis_categorias = mostrar_categoria(mi_ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    crear_receta(mi_categoria)
    #volver a inicio
    pass
elif menu == 3:
    crear_categoria(mi_ruta)
    #volver a inicio
    pass
elif menu == 4:
    mis_categorias = mostrar_categoria(mi_ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    mi_listas_recetas = mostrar_recetas(mi_categoria)
    mi_receta = elegir_recetas(mi_listas_recetas)
    #eliminar receta
    #volver a inicio
    pass
elif menu == 4:
    mis_categorias = mostrar_categoria(mi_ruta)
    #elegir categoria
    #mostrar recetas
    #elegir recetas
    #eliminar receta
    #volver a inicio
    pass
elif menu == 5:
    mis_categorias = mostrar_categoria(mi_ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    #eliminar categoria
    #volver a inicio
    pass
elif menu == 6:
    ##Finalizar
    pass

def mostar_menu(nombre):
    system("clear")
    print('*' * 50)
    print(f"Estas son las opciones {nombre}: ")
    print('*' * 50)
    print(f"En mi carpeta de recetas : {mi_ruta}")
    print(f"Existen estas recetas : {contar_recetas(mi_ruta)}")

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        system("clear")
        print(f"1. Leer receta")
        print(f"2. Crear receta")
        print(f"3. Crear Categoria")
        print(f"4. Eliminar receta")
        print(f"5. Eliminar Categoria")
        print(f"6. Salir")
        print("Elige un opcion: \n")
        eleccion_menu = input()
    
    return(eleccion_menu)



    



def comprobar_receta(palabra):
    recetas = Path("recetas")
    for receta in recetas.glob(palabra):
        print(receta.read_text)


mostar_menu("Rafa")
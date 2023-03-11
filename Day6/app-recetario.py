import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(),'Downloads', "Recetas")

def mostar_menu():
    system("cls")
    print('*' * 50)
    print('*' * 11 + " Estas son las opciones : "           + '*' *11)
    print('*' * 50)
    print(f"En mi carpeta de recetas : {mi_ruta}")
    print(f"Existen estas recetas : {contar_recetas(mi_ruta)}\n")

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print(f"1. Leer receta")
        print(f"2. Crear receta")
        print(f"3. Crear Categoria")
        print(f"4. Eliminar receta")
        print(f"5. Eliminar Categoria")
        print(f"6. Salir\n")
        print("Elige un opcion:")
        eleccion_menu = input()
    
    return(int(eleccion_menu))


def contar_recetas(ruta):
    cont = 0
    for txt in Path(ruta).glob("**/*.txt"):
        cont +=1
    return cont

def mostrar_categoria(ruta):
    print(f"Estas son las categorias disponibles : \n")
    categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in categorias.iterdir():
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
        lista_recetas.append(receta)
        contador +=1
    
    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = 's'
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\n Elige una receta: ")

    return lista[int(eleccion_receta) - 1]

def leer_receta(receta):
    print(Path.read_text(receta))
    
def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta:")
        nombre_receta = input() + '.txt'
        print("Escribe la nueva receta: \n")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
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

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu categoria {nombre_categoria} ha sido creada ")
            existe = True
        else:
            print("Tu categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion_regresar = 's'
    while eleccion_regresar.lower() != 'y':
        eleccion_regresar = input("\n Pulsa 'Y' para regresar\n")
#mostar menu inicio
finalizar_programa = False
while  not finalizar_programa:
    menu = mostar_menu()
    if menu == 1:
        mis_categorias = mostrar_categoria(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mi_listas_recetas = mostrar_recetas(mi_categoria)
        if len(mi_listas_recetas) <1:
            print("No hay recetas disponibles")
        else:
            mi_receta = elegir_recetas(mi_listas_recetas)
            leer_receta(mi_receta)
        volver_inicio()
        pass
    elif menu == 2:
        mis_categorias = mostrar_categoria(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
        pass
    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()
        pass
    elif menu == 4:
        mis_categorias = mostrar_categoria(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mi_listas_recetas = mostrar_recetas(mi_categoria)
        if len(mi_listas_recetas) < 1:
            print("No hay recetas")
        else:
            mi_receta = elegir_recetas(mi_listas_recetas)
            eliminar_receta(mi_receta)
        volver_inicio()
    elif menu == 5:
        mis_categorias = mostrar_categoria(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()

    elif menu == 6:
        finalizar_programa = True

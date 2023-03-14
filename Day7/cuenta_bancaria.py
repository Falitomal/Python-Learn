class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"Nombre: {self.nombre}, apellido: {self.apellido}"

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Nombre: {self.nombre}, apellido: {self.apellido}, numero de cliente: {self.numero_cuenta}, balance: {self.balance}"
    
    def depositar(self, money):
        self.balance += money
        print(f"Se ha depositado {money} en la cuenta {self.numero_cuenta}")
    
    def retirar(self, money):
        self.balance -= money
        print(f"Se ha retirado {money} de la cuenta {self.numero_cuenta}")


def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    numero_cuenta = input("Ingrese el numero de cuenta del cliente: ")
    balance = float(input("Ingrese el balance del cliente: "))
    return Cliente(nombre, apellido, numero_cuenta, balance)

def inicio():
    print("Bienvenido al banco")
    print("1. Crear cliente")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    opcion = int(input("Ingrese la opcion: "))
    return opcion


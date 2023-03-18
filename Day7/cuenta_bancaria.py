class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"Nombre: {self.nombre}, apellido: {self.apellido}"

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Nombre: {self.nombre}, apellido: {self.apellido}\n numero de cliente: {self.numero_cuenta}, balance: {self.balance}"
    
    def depositar(self, money):
        self.balance += money
        print(f"Se ha depositado {money} en la cuenta {self.numero_cuenta}")
    
    def retirar(self, money_retired):
        if self.balance >= money_retired:
            self.balance -= money_retired
            print(f"Se ha retirado {money_retired} de la cuenta {self.numero_cuenta}")
        else:
            print(f"\nNo hay suficiente dinero, este es tu saldo: {self.balance}\n")


def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    numero_cuenta = input("Ingrese el numero de cuenta del cliente: ")
    balance = float(input("Ingrese el balance del cliente: "))
    return Cliente(nombre, apellido, numero_cuenta, balance)

def inicio():
    mi_cliente = crear_cliente()
    opcion = 0
    while opcion != 3:
        print("+" * 10)
        print("Bienvenido al banco")
        print("+" * 10)
        print(mi_cliente)
        print("+" * 10)
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")
        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            money = int(input(print("Cuanto dinero quiere ingresar: ")))
            mi_cliente.depositar(money)
        elif opcion == 2:
            money = int(input(print("Cuanto dinero quiere retirar: ")))
            mi_cliente.retirar(money)
    print(f"Gracias {mi_cliente.nombre} por usar nuestros servicios")
    
inicio()


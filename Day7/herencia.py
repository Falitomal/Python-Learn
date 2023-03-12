class Animal:
    def __init__(self, edad, color) -> None:
        self.edad = edad
        self.color = color

    def nacer(self):
        print("El animal esta vivo")
        
class Mamifero(Animal):
    def nacer(self):
        print("Naci aman y muero")
    
class Pajaro(Mamifero):
    pass


piolin = Pajaro(2, "Amarillo")

piolin.nacer()
print(Pajaro.__mro__)
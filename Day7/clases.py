class Pajaro:

    alas = True
    pico = True
    plumas = True
    def __init__(self, color, especie) -> None:
        self.color = color
        self.especie = especie

# Metodo de instancia, acceden y modifican atributos
# Acceden a otros metodos y modifican el estado de la clase

    def piar(self):
        print(f"Pio pio pio mi color es {self.color}")

    def volar(self, metros):
        print(f"El pajaro {self.especie} volo {metros}")
        self.piar()

    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es {self.color}")


# Metodos de clase
# No necesitan instancias para ejecutarse, no acceden a parametros pero si atributos
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)


# Metodos estaticos, no pueden acceder ni a parametros, ni atributos ni metodos

    @staticmethod
    def mirar():
        print("El pajaro mira")

Pajaro.poner_huevos(3)

mi_pajaro = Pajaro('Rojo', "Loro")
print(f"Mi pajaro {mi_pajaro.especie} es de color {mi_pajaro.color}")
mi_pajaro.piar()
mi_pajaro.volar(100)

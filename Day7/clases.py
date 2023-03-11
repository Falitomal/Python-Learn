class Pajaro:

    alas = True
    pico = True
    plumas = True
    def __init__(self, color, especie) -> None:
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('Rojo', "Loro")
print(f"Mi pajaro {mi_pajaro.especie} es de color {mi_pajaro.color}")
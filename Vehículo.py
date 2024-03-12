class Vehiculo:

    def __init__(self, *, ruedas: int, color: str)-> None:
        self.ruedas = ruedas
        self.color = color


    def información(self) -> None:
        print("Ruedas: ", self.ruedas, " color: ", self.color)



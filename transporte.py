class Transporte:

    def __init__(self, *, ruedas: int, asientos: int)-> None:
        self.ruedas = ruedas
        self.asientos = asientos


    
    def información(self) -> None:
        print("Ruedas: ", self.ruedas, " Asientos: ", self.asientos)


    def desplazamiento(self, x: int, y: int = 0) -> None:
        print("Desplazando a: ", x, y)


from Automovil import automovil
from Camion import camion
from Bicicleta import bicicleta
from Moto import moto

def main():
    Auto = automovil(ruedas=4, color="rojo")
    Cam = camion(ruedas=6, color="azul")
    Bicicleta = bicicleta(ruedas=2, color="morado")
    Moto = moto(ruedas=2, color="amarillo")

    Auto.información()
    Cam.información()
    Bicicleta.información()
    Moto.información()

main()
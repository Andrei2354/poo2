from guagua import Guagua

def main():
    intercity = Guagua(asientos=50, ruedas=6)
    lanzarote = Guagua(asientos=70, ruedas=8)

    intercity.desplazamiento(30)
    lanzarote.desplazamiento(40, 60)

    intercity.información()
    lanzarote.información()

main()
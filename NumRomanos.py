class NumerosRomanos:

    def __init__(self, romano: int)-> None:
        self.romano = romano

    
    def calculo(self) -> None:
        listaRomano =  ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        listaDecimal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numeral_romano = ''
        i = 0
        while self.romano > 0:
            if self.romano - listaDecimal[i] >= 0:
                numeral_romano += listaRomano[i]
                self.romano -= listaDecimal[i]
            else:
                i += 1
        return numeral_romano


def main():
    numero1 = NumerosRomanos(7)

    print(numero1.calculo())

main()

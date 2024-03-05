### Parametro posicional / par= parametro
* Segun la posicion del argumento, ejemplo:
def ejemplofun(unpar:int, dospar:int)-->None:
def ejemplofun(unpar:int, dospar:int, /)-->None:  # Cuidado con el caracter "/"
    pass

ejemplofun(3, 6)
#un par = 3
#dos par  = 6

### Parametros con valor por defecto / par= parametro / ( parametro = 7, )
* Se le asigna un valor, ejemplo:
def ejemplofun(unpar:int, dospar = 6:int)->None:
    pass

ejemplofun(3)
#un par = 3
#dos par  = 6

### Parametros arbitrario / par= parametro 7 ( *parametro, )
* Según un número determinado de argumentos, ejemplo:
def ejemplofun(unpar:int, *dospar = 6:int, content:int )->None:
    pass

ejemplofun(3, 6, 6, 6,content=3)


### Parametros nominal / par= parametro / ( *,)
* Ejemplo:
def ejemplofun(*, unpar:int, dospar = 6:int)->None:
    pass

ejemplofun(dospar= 6, unpar=3)



### Ejercicio 3
def myDiv(id:str, *clas:str, content:str)->str:
    resultado = ''

    resultado += '<div id="' + id + '" '

    if len(clas) != 0:
        resultado += 'class = "'
        
        for e in clas:
            resultado += e + ', ' 

        resultado += '\b\b"'

    resultado += '>' + content + '</div>'

    return resultado


### Ejercicio 5
def myScrip(*src:str)->str:
Función que tiene como entrada un número indeterminado de cadenas de caracteres
y como salida de una cadena de caracteres Probablemente transforma las entradas en la salida.
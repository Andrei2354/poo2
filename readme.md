## Apuntes de Markdown

https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

### Diagram Class
https://mermaid.js.org/syntax/classDiagram.html

# Programación orientada a objetos
![Alt text](https://aprendepython.es/_images/oop.jpg "Programación orientada a objetos")
https://aprendepython.es/core/modularity/oop/

### Encapsulamiento
Permite empaquetar el código dentro de una unidad (objeto) donde se puede determinar el ámbito de actuación.

### Abstracción
Permite generalizar los tipos de objetos a través de las clases y simplificar el programa.

### Herencia
Permite reutilizar código al poder heredar atributos y comportamientos de una clase a otra.

### Polimorfismo
Permite crear múltiples objetos a partir de una misma pieza flexible de código.

---
title: Animal example
---
classDiagram
    note "From Duck till Zebra"
    Animal <|-- Duck
    note for Duck "can fly\ncan swim\ncan dive\ncan help in debugging"
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
        +String beakColor
        +swim()
        +quack()
    }
    class Fish{
        -int sizeInFeet
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }
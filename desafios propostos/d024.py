"""
Simule uma cafeteira orientada a objetos
 'Não tem atributos apenas métodos'
 ______________________________
|    BebidaQuente {abstract}   |
|------------------------------|
|+ preparar()                  |
|+ ferver_agua()               |
|+ misturar() {abstract}       |
|+ servir() {abstract}         |
|______________________________|

Subclasses:
 ___________________
|      Cafe         |
|-------------------|
|+ misturar()       |
|+ servir()         |
|___________________|

 ____________________
|        Cha         |
|--------------------|
|+ misturar()        |
|+ servir()          |
|____________________|

 ____________________
|       Leite        |
|--------------------|
|+ misturar()        |
|+ servir()          |
|____________________|

"""
"""
Simule o sistema de batalha entre personagens de um RPG

 ___________________________
|   Funcionario {abstract}  |
|---------------------------|
|+ nome                     |
|+ vida                     |    
|+ golpes                   |
|+ inss = 7.5               |
|---------------------------|
|+ atacar(alvo, força)      |
|+ receber_dano(dano)       |
|+ curar() {abstract}       |
|___________________________|

subclasses:
 _________________
|   Guerreiro     |
|-----------------|
|-----------------|
|+ curar()        |
|_________________|

 _________________
|      mago       |
|-----------------|
|-----------------|
|+ curar()        |
|_________________|
"""

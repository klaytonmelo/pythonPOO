"""
Crie classes capazes de calcular fretes
de veiculos diferentes.

diagrama:
 ___________________________
|   Transporte {abstract}   |
|---------------------------|
|+ distancia                |
|+ frete                    |
|---------------------------|
|+ calc_frete() {abstract}  |
|___________________________|

subclasses:

'fator deve ser um Atributo de classe'

 _________________
|      moto       | 'moto: livre'
|-----------------|
|+ fator = 0.50   |
|-----------------|
|+ calc_frete()   |
|_________________|

 _________________
|    Caminhao     | 'Caminhão: min 50 km'
|-----------------|
|+ fator = 1.20   |
|-----------------|
|+ calc_frete()   |
|_________________|

 _________________
|      Drone      | 'drone: max 10km'
|-----------------|
|+ fator = 9.50   |
|-----------------|
|+ calc_frete()   |
|_________________|

"""
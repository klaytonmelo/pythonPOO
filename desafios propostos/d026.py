"""
Crie um estrutura capaz de calcular salários de funcionários diferentes

diagrama:
 ___________________________
|   Funcionario {abstract}  |
|---------------------------|
|+ nome                     |
|+ sal_bruto                |      
|+ salario                  |
|+ sal_min = 1612           | "atributos de classe: 'sal_min' e 'inss' "
|+ inss = 7.5               |
|---------------------------|
|+ calc_sal() {abstract}    |
|+ analizar_sal()           |
|___________________________|

subclasses:

 _________________
|     Horista     |
|-----------------|
|+ valor_hora     |
|+ horas_trab     |
|-----------------|
|+ calc_sal()     |
|_________________|

 _________________
|   mensalista    | 
|-----------------|
|-----------------|
|+ calc_sal()     |
|_________________|

"""
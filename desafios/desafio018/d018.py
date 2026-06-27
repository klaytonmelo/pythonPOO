"""
    Crie a classe Churrasco, onde seja possível informar
    quantas pessoas vão participar e mostre quanto de carne
    deve ser comprado, o custo total do churrasco e o preço
    por pessoa.1
"""

#CONSIDERE
# Consumo padrão: 400g por pessoa
# Preço: R$82,40/kg

from rich import print
from rich.panel import Panel

class Churrasco:
    #atributos de classe
    consumo_padrão = 0.400
    preço_kg = 82.40

    def __init__(self, titulo, quant):
        #atributos de instância
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        return f"Esse é o {self.titulo} com {self.participantes} pessoas participantes"
    
c1 = Churrasco("Churras dos amigos", 15)
print(c1)

    

    

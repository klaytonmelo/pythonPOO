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
    consumo_padrão:float = 0.400
    preço_kg:float = 82.40 #kg de carne

    def __init__(self, titulo, quant):
        #atributos de instância
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        return f"Esse é o {self.titulo} com {self.participantes} pessoas participantes"

    def calcular_qtd_carne(self)-> float:
        return self.participantes * Churrasco.consumo_padrão
    
    def calcular_custo_total(self)-> float:
        return self.calcular_qtd_carne() * self.__class__.preço_kg

    def calcular_custo_individual(self)-> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.participantes} convidados [/]"
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrão} kg e cada Kg custa R$ {Churrasco.preço_kg:,.2f}"
        conteudo += f"\nRecomendo [blue]comprar {self.calcular_qtd_carne():.3f} kg[/] de carne"
        conteudo += f"\nO custo total será de [green]R${self.calcular_custo_total():,.2f}[/] "
        conteudo += f"\nCada pessoa pagará [yellow]R${self.calcular_custo_individual():,.2f}[/] para participar."
        painel = Panel(conteudo, title=self.titulo)
        print(painel)
    
c1 = Churrasco("Churras dos amigos", 15)
print(c1)
c1.analisar()

c2 = Churrasco("festa do fim de ano", 80)
c2.analisar()
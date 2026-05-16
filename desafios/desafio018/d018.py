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
#from rich.traceback import install
#install()

class Churrasco:
    def __init__(self, titulo, quant):
        self.nome = titulo
        self.quant = quant

    def analisar(self):
        consumop = 400/1000
        qtotal = consumop * self.quant
        ctotal = qtotal * 82.40
        totalp = ctotal/self.quant

        analise = f"Analisando [green]{self.nome}[/green] com [blue]{self.quant} convidados[/blue]\n"
        analise += f"cada participante comerá {consumop}Kg de carne\n"
        analise += f"Recomendo [blue] comprar {qtotal:.2f}kg [/blue]de carne\n"
        analise += f"ocusto total será de R${ctotal:,.2f}\n"
        analise += f"cada pessoa pagará R${totalp:,.2f}"

        tabela = Panel(analise ,title=self.nome)
        print(tabela)

c1 = Churrasco("churras dos amigos ", 15)
c1.analisar()

c2 = Churrasco("familia", 17)
c2.analisar()
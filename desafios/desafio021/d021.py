"""
    Crie uma classe Caneta, que simula o funcionamento de uma caneta colorida,
    podendo escrever frases na cor relativa.
"""
from rich import print

class Caneta:
    def __init__(self, cor = "Azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelha" | "vermelho":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"

        self.cor = escolha
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True
    

    def escrever(self, frase):
        if self.tampada:
            print(f":prohibited: A {self.cor}caneta[/] está tampada!")
        else:
            print(f"{self.cor}{frase}[/]", end="")

    def quebrar_linha(self, qtd = 1):
        for c in range(0, qtd):
            print("\n", end="")


c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("olá, tudo bem ?")
c1.quebrar_linha(1)
c2.escrever("olá, Gafanhoto!")
c3.escrever("Vamos exercitar!")

c1.tampar()
c1.escrever("Será que funciona ?")
"""
    Crie uma classe Gamer, onde podemos cadastrar nome, nike e os jogos favoritos de
    uma pessoa. Crie também um método que permita mostrar a ficha desse gamer.
"""
from rich.traceback import install
from rich import print
from rich.panel import Panel
from rich import inspect

install()

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f"Nome real: [black on blue]{self.nome}[/]"
        conteudo += f"\nJogos favoritos: "

        for num, game in enumerate(self.favoritos):
            conteudo += f"\n:video_game: [blue]{game}[/]" 

        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=50)
        print(painel)

j1 = Gamer("Fabricio da Silva", "detonator2025")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("Good of War")
j1.add_favoritos("Fortnite")
#inspect(j1)
j1.ficha()

j2 = Gamer("Olivia Souza", "peach_raivosa")
j2.add_favoritos("Mario Bros")
j2.add_favoritos("Call of duty")
j2.ficha()
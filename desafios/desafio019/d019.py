"""
    Crie a classe Livro que vai simular a passagem de páginas de um livro,
    considerando também se o usuário chegou ao fim da leitura.
"""
from rich import print
from rich.traceback import install
from time import sleep
install()
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1
        print(f":open_book: [blue]Você acabou de abrir o livro [red]{self.titulo}[/] que tem [green]{self.total_paginas} paginas[/]. você agora está na [yellow]página {self.pagina_atual}[/yellow][/blue]")

    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Página{self.pagina_atual} :arrow_forward: ", end="")
                sleep(0.3)
                cont += 1
        print(f"[blue]você avançou {cont} páginas e agora está na [yellow]página {self.pagina_atual}[/yellow][/blue]")

        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro [black]'{self.titulo}'[/][/]")

    def fim_do_livro(self) ->bool:
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False
    
    def voltar_pagina(self):
        pass

    def __str__(self):
        pass
        #return f"O livro {self.titulo} tem {self.total_paginas} páginas, e está na página {self.pagina_atual}"

l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)
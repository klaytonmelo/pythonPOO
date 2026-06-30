"""
    Crie a classe Livro que vai simular a passagem de páginas de um livro,
    considerando também se o usuário chegou ao fim da leitura.
"""

class Livro:
    def __init__(self, nome, paginas):
        self.nome_livro = nome
        self.quantidade_paginas = paginas
        self.pagina = 1

    def passar_pagina(self):
        self.pagina += 1
        print(f"Você passou para a pagina {self.pagina}")
    
    def voltar_pagina(self):
        self.pagina -= 1
        print(f"Você voltou para a pagina {self.pagina}")

    def __str__(self):
        return f"O livro {self.nome_livro} tem {self.quantidade_paginas} páginas, e está na página {self.pagina}"

livro1 = Livro("Chaves", 100)
print(livro1)
livro1.passar_pagina()
livro1.voltar_pagina()

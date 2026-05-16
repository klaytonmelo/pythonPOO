from rich import print
from rich import inspect
from rich.traceback import install
install()

class Funcionario:
    #Atributos de Classe
    empresa = "Curso em Video"

    def __init__(self, nome, setor, cargo):
        #atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f":handshake: Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}!"

#Funcionario.empresa = "Hostnet"

c1 = Funcionario("klayton", "TI", "programador")
print(c1.apresentacao())
c1.empresa = "Estudonalta"
print(c1.empresa)
#inspect(c1)

c2 = Funcionario("Pedro", "Administração", "Diretor")
print(c2.apresentacao())
#inspect(c2)

#inspect(Funcionario)

#declaração de classe
class Gafanhoto:
    """
    Essa class cria um gafanhoto, que é uma pessoa que tem nome e idade
    para criar uma nova pessoa, use:
    vaiavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "vazil", idade = 0):  #metodo construtor
        #atributos de instancia
        self.nome = nome
        self.idade = idade

    #métodos de instancia
    def aniversario(self):
        self.idade += 1

    def __str__(self):#Dunder Method
        return f"{self.nome} é gafahoto(a) e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

#declaração de atributos
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
#print(g1)
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)
print(g1.__doc__) #Dunder Attribute

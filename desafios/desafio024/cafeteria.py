from abc import ABC, abstractmethod
from rich import print
from time import sleep

class Cafeteira(ABC):
    def __init__(self):
        pass

    def preparar(self):
        print("--- [blue]Iniciando Preparo[/] ---")
        sleep(4)
        print(f"1. {self.ferver_agua()}")
        sleep(2)
        print(f"2. {self.misturar()}")
        sleep(2)
        print(f"3. {self.servir()}")
        sleep(1.5)
        print("[blue]--- Bebida pronta ---[/]")
    
    def ferver_agua(self):
        return "Fervendo água a 100 graus Celcius."

    @abstractmethod

    def misturar(self):
        pass

    def servir(self):
        pass


class Cafe(Cafeteira):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return "Passando água pressurizada pelo pó de café moido."

    def servir(self):
        return "Servindo em xicara pequena."


class Cha(Cafeteira):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return "Mergulhando o sachê de ervas na água."

    def servir(self):
        return "Servindo na caneca de porcelana com limão."


class Leite(Cafeteira):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return "Passando vapor pressurizado pelo bico do leite."

    def servir(self):
        return "Servindo na caneca grande, já com café."
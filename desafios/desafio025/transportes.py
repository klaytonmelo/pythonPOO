from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
       self.distancia = distancia
       self.frete = 0

    @abstractmethod
    def calc_frete():
        pass


class Moto(Transporte):
    fator = 0.50
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        self.frete = self.distancia * Moto.fator
        return f"R${self.frete:.2f}"


class Caminhao(Transporte): #min 50km
    fator = 1.20
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia < 50:
            self.frete = 0
            return "Raio mínimo de 50km"
        else:
            self.frete = self.distancia * Caminhao.fator
            return f"R${self.frete:.2f}"


class Drone(Transporte): #max 10km
    fator = 9.50
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia > 10:
            return "Raio maximo de 10km"
        else:
            self.frete = self.distancia * Drone.fator
            return f"R${self.frete:.2f}"


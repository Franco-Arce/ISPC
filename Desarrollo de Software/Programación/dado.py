import random

class Dado:

    def __init__(self, numeroCaras=6):
        self.__numeroCaras = numeroCaras
    
    def lanzar(self):
        return random.randint(1, self.__numeroCaras)

    def __str__(self):
        resultado = self.lanzar()
        return f"El resultado del lanzamiento es: {resultado}"

dado = Dado()

print(dado)

import random

class Dado:

    def __init__(self, numeroCaras = 6):
        self.__numeroCaras = numeroCaras
    
    def lanzar(self):
        return random.randint(1, self.__numeroCaras)
    
dado= Dado()

resultado = dado.lanzar()

print(f"El resultado del lanzamiento es: {resultado}")

from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        self.__personagem = personagem

    @property
    def personagem(self) -> Personagem:
        return self.__personagem

    def valor_total_carta(self) -> int:
        valor = 0
        valor += self.__personagem.energia
        valor += self.__personagem.habilidade
        valor += self.__personagem.velocidade
        valor += self.__personagem.resistencia
        return valor

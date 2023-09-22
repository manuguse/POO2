from abc import ABC, abstractmethod
from Carta import *
from AbstractJogador import *
import random


class Jogador(AbstractJogador):

    def __init__(self, nome: str):
        self.__nome = nome
        self.__cartas = []

    @property
    def nome(self) -> str:
        return self.__nome

    def baixa_carta_da_mao(self) -> Carta:
        num = random.randint(0, len(self.__cartas)-1)
        carta = self.__cartas[num]
        self.__cartas.remove(carta)
        return carta

    @property
    def mao(self) -> list:
        return self.__cartas
        
    def inclui_carta_na_mao(self, carta:Carta):
        self.__cartas.append(carta)

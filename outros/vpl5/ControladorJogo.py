from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__baralho = []
        self.__personagens = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagens

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        personagem = Personagem(energia, habilidade, velocidade,
                                resistencia, tipo)
        self.__personagens.append(personagem)
        return personagem

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        carta = Carta(personagem)
        self.__baralho.append(carta)
        return carta

    def iniciaJogo(self, jogador1: Jogador, jogador2: Jogador):
        for i in range(5):
            num = random.randint(0, (len(self.__baralho) - 1))
            carta = self.__baralho[num]
            jogador1.inclui_carta_na_mao(carta)

            num = random.randint(0, (len(self.__baralho) - 1))
            carta = self.__baralho[num]
            jogador2.inclui_carta_na_mao(carta)

    def jogada(self, mesa: Mesa) -> Jogador:
        carta1 = mesa.carta_jogador1
        carta2 = mesa.carta_jogador2
        valor1 = carta1.valor_total_carta()
        valor2 = carta2.valor_total_carta()
        if valor1 > valor2:
            mesa.jogador1.inclui_carta_na_mao(carta1)
            mesa.jogador1.inclui_carta_na_mao(carta2)
            return mesa.jogador1
        elif valor2 > valor1:
            mesa.jogador2.inclui_carta_na_mao(carta1)
            mesa.jogador2.inclui_carta_na_mao(carta2)
            return mesa.jogador2
        else:
            mesa.jogador1.inclui_carta_na_mao(carta1)
            mesa.jogador2.inclui_carta_na_mao(carta2)
            return None

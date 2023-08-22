class Votacao():
    
    def __init__(self, votos) -> None:
        self.votos = votos
        
    def calcula_num_votos(self):
        num_votos = 0
        for voto in self.votos:
            num_votos += voto
        return num_votos
    
    def melhor_jogador(self):
        return self.votos.index(max(self.votos))
    
    def calcula_porcentagem(self, jogador):
        return (((jogador/self.calcula_num_votos())*100))
    
    def mostra_infos(self):
        for i, jogador in enumerate(self.votos):
            if jogador != 0:
                print(f"{i:<12} {jogador:<5} {self.calcula_porcentagem(jogador):.2f}%")
    
    def mostra_resultado(self):
        print("\nResultado da votação:")
        print(f"\nForam computados {self.calcula_num_votos()} votos")
        print(f"\nJogador    Votos     %")
        self.mostra_infos()
        print(f"\nO melhor jogador foi o número {self.melhor_jogador()}, com {max(self.votos)}, correspondendo a {self.calcula_porcentagem(self.votos[self.melhor_jogador()]):.2f}% do total de votos.")

jogadores = [0]*24

print("Enquete: Quem foi o melhor jogador?")
while True:
    jogador = int(input("Número do jogador: "))
    if jogador == 0:
        break
    if jogador > 23 or jogador < 0:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")
    else:
        jogadores[jogador] += 1

votacao = Votacao(jogadores)
votacao.mostra_resultado()
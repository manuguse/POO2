class Pessoas():
    def __init__(self, matriz):
        self.matriz = matriz
        self.tamanho = len(matriz)

    def mostra_valores(self):
        for i in range(self.tamanho):
            print(f'\nPessoa {i+1}: \n Altura = {self.matriz[i][1]} \n Idade = {self.matriz[i][0]}')

matriz = []
for i in range(5):
    pessoa = []
    pessoa.append(int(input(f'Idade pessoa {i+1}: ')))
    pessoa.append(float(input(f'Altura pessoa {i+1}: ')))
    matriz.append(pessoa)

pessoas = Pessoas(matriz)
pessoas.mostra_valores()

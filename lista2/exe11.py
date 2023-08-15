class Intercalacao():
    def __init__(self, vetor1, vetor2, vetor3):
        self.vetor1 = vetor1
        self.vetor2 = vetor2
        self.vetor3 = vetor3
        self.tamanho = 10

    def calcula_novo_vetor(self):
        novo_vetor = []
        for i in range(self.tamanho):
            novo_vetor.append(self.vetor1[i])
            novo_vetor.append(self.vetor2[i])
            novo_vetor.append(self.vetor3[i])
        print(novo_vetor)
        
"""
vetor1 = [1,2,3,4,5,6,7,8,9,10]
vetor2 = [11,12,13,14,15,16,17,18,19,20]
vetor3 = [100,101,102,103,104,105,106,107,108,109]
int = Intercalacao(vetor1,vetor2,vetor3)
int.calcula_novo_vetor()
"""
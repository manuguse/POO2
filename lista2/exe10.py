class Intercalacao():
    def __init__(self, vetor1, vetor2):
        self.__vetor1 = vetor1
        self.__vetor2 = vetor2
        self.tamanho = 10

    def calcula_novo_vetor(self):
        novo_vetor = []
        for i in range(self.tamanho):
            novo_vetor.append(self.__vetor1[i])
            novo_vetor.append(self.__vetor2[i])
        print(novo_vetor)

vetor1 = [1,2,3,4,5,6,7,8,9,10]
vetor2 = [11,12,89,-23,15,16,45,18,27,20]
int = Intercalacao(vetor1,vetor2)
int.calcula_novo_vetor()
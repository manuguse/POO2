class Alturas():

    def __init__(self, vetor):
        self.__vetor = vetor
        self.__tamanho = len(vetor)

    def calcula_media(self):
        soma = 0
        for pessoa in self.__vetor:
            soma += pessoa[1]
        media = soma/self.__tamanho
        return media
    
    def compara(self):
        soma = 0
        media = self.calcula_media()
        for pessoa in self.__vetor:
            if pessoa[0] > 13:
                if pessoa[1] < media:
                    soma += 1
        print("Alunos com mais de 13 anos e altura menor que a media: ", soma)
        
alunos = Alturas([[40,1.7], [13,1.2], [30,1.65], [10,1.25], [1,1.1], [3,1.7], [33,1.1]])
alunos.compara()
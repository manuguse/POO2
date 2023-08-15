class Alturas():

    def __init__(self, vetor):
        self.vetor = vetor
        self.tamanho = len(self.vetor)

    def calcula_media(self):
        soma = 0
        for pessoa in self.vetor:
            soma += pessoa[1]
        media = soma/self.tamanho
        return media
    
    def compara(self):
        soma = 0
        media = self.calcula_media()
        for pessoa in self.vetor:
            if pessoa[0] > 13:
                if pessoa[1] < media:
                    soma += 1
        print(soma)
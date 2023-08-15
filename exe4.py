consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

class Consoantes():

    def __init__(self, vetor):
        self.vetor = vetor

    def calcula_consoantes(self):
        cont = 0
        cons = []
        for i in range(10):
            if self.vetor[i] in consoantes:
                cont += 1
                cons.append(self.vetor[i])
        print(cont)
        print(cons)
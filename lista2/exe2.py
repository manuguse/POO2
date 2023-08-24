class Vetor():
    
    def __init__(self, vetor):
        self.__vetor = vetor

    def mostra_inverso(self):
        novo_vetor = self.__vetor[:]
        novo_vetor.reverse()
        print(novo_vetor)
        
vetor = Vetor([1,4,6,7,9,17,23,3,5,6])
vetor.mostra_inverso()
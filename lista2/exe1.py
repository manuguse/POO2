class Vetor():
    def __init__(self, vetor):
        self.__vetor = vetor

    def mostra_vetor(self):
        print(self.__vetor)
        
vetor = Vetor([1,4,6,7,9])
vetor.mostra_vetor()
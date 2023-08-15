class Vetor():
    
    def __init__(self, vetor):
        self.vetor = vetor

    def mostra_inverso(self):
        novo_vetor = self.vetor[:]
        novo_vetor.reverse()
        print(novo_vetor)
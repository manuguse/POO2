class SomaQuadrados():
    def __init__(self, vetor):
        self.vetor = vetor
        self.tamanho = 10

    def calcula(self):
        resultado = 0
        for numero in self.vetor:
            resultado += numero**2
        print(resultado)
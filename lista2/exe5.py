class Numeros():

    def __init__(self, vetor):
        self.vetor = vetor
        self.pares = []
        self.impares = []

    def separa(self):
        for numero in self.vetor:
            if self.calcula_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)
        print('pares:', self.pares)
        print('impares:', self.impares)
        print('todos:', self.vetor)

    def calcula_par(self, num):
        if num%2 == 0:
            return True
        return False
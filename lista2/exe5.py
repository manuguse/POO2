class Numeros():

    def __init__(self, __vetor):
        self.__vetor = __vetor
        self.__pares = []
        self.__impares = []

    def separa(self):
        for numero in self.__vetor:
            if self.calcula_par(numero):
                self.__pares.append(numero)
            else:
                self.__impares.append(numero)
        print('pares:', self.__pares)
        print('impares:', self.__impares)
        print('todos:', self.__vetor)
        print()
        
    def calcula_par(self, num):
        if num%2 == 0:
            return True
        return False
    
num1 = Numeros([2,5,6,7,11,-32])
num1.separa()

num2 = Numeros([1,2,99,654,24])
num2.separa()
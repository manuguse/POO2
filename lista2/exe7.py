class Operacoes():

    def __init__(self, vetor):
        self.__vetor = vetor
        self.__tamanho = len(vetor)

    def calcula_soma(self):
        soma = 0
        for numero in self.__vetor:
            soma += numero
        return soma

    def calcula_mult(self):
        mult = 1
        for numero in self.__vetor:
            mult = mult*numero
        return mult
    
    def mostra_num(self):
        nums = ""
        for i in range(self.__tamanho):
            nums += str(self.__vetor[i])
            if i != self.__tamanho-1:
                nums += ", "
        return nums

    def mostra_operacoes(self):
        print("soma:", self.calcula_soma())
        print("multiplicacao:", self.calcula_mult())
        print("numeros:", self.mostra_num())
        print()
        
opera = Operacoes([4,5,7,2,3])
opera.mostra_operacoes()

opera = Operacoes([5,7,9,10,5])
opera.mostra_operacoes()
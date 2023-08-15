class Operacoes():

    def __init__(self, vetor):
        self.vetor = vetor
        self.tamanho = 5

    def calcula_soma(self):
        soma = 0
        for numero in self.vetor:
            soma += numero
        return soma

    def calcula_mult(self):
        mult = 1
        for numero in self.vetor:
            mult = mult*numero
        return mult
    
    def mostra_num(self):
        nums = ""
        for i in range(self.tamanho):
            nums += str(self.vetor[i])
            if i != self.tamanho-1:
                nums += ", "
        return nums

    def mostra_operacoes(self):
        print("soma:", self.calcula_soma())
        print("multiplicacao:", self.calcula_mult())
        print("numeros:", self.mostra_num())
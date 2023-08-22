class OperacoesValores():
    
    def __init__(self,valores) -> None:
        self.valores = valores
    
    def calcula_qtde(self):
        return len(self.valores)
        
    def mostra_qtde(self):
        print(self.calcula_qtde())
        
    def mostra_ordem(self):
        for numero in self.valores:
            print(f"{numero} ", end="")
        print()
        
    def mostra_inverso(self):
        for numero in self.valores[::-1]:
            print(f"{numero} ")
            
    def calcula_soma(self):
        soma = 0
        for numero in self.valores:
            soma += numero
        return soma
    
    def mostra_soma(self):
        print(self.calcula_soma())
        
    def calcula_media(self):
        return (self.calcula_soma()/self.calcula_qtde())
    
    def mostra_media(self):
        media = self.calcula_media()
        print(f"{media:.2f}")
        
    def acima_media(self):
        soma = 0
        media = self.calcula_media()
        for valor in self.valores:
            if valor > media:
                soma += 1
        print(soma)
        
    def abaixo_sete(self):
        soma = 0
        for valor in self.valores:
            if valor < 7:
                soma += 1
        print(soma)

valores = []
while True:
    valor = int(input("Digite um valor: "))
    if valor == -1:
        break
    valores.append(valor)
    
operacoes = OperacoesValores(valores)

print("\nQuantidade de valores: ")
operacoes.mostra_qtde()

print("\nMostra todos em ordem:")
operacoes.mostra_ordem()

print("\nMostra todos em ordem inversa:")
operacoes.mostra_inverso()

print("\nSoma de todos os valores:")
operacoes.mostra_soma()

print("\nMédia dos valores:")
operacoes.mostra_media()

print("\nValores acima da média:")
operacoes.acima_media()

print("\nValores abaixo de sete:")
operacoes.abaixo_sete()

print("\nFim do programa!")
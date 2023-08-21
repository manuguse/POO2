class Series():
    
    def __init__(self) -> None:
        self.maximo = 1000
    
    def opcoes(self):
        opcoes = [self.calcula_fibonacci, self.calcula_fatorial, self.calcula_fibonarial, self.calcula_primo]
        opcao = int(input("Digite a opção desejada: \n 1 - fibonacci \n 2 - fatorial \n 3 - fibonarial \n 4 - primo \n 5 - sair \n"))
        if opcao == 5:
            return False
        else:
            opcoes[opcao-1]()
            return True
    
    def mostra_fibonacci(self):
        pos = int(input("Digite a posicao do numero de fibonacci: "))
        print(f"O numero de fibonacci na posicao {pos} é {self.calcula_fibonacci(pos)}")

    def calcula_fibonacci(self, pos):
        if pos <= 0:
            return 0
        elif pos == 1:
            return 1
        else:
            return self.calcula_fibonacci(pos-1) + self.calcula_fibonacci(pos-2)
    
    def calcula_fatorial(self):
        num = int(input("Digite o numero para calcular o fatorial: "))
        if num < 0:
            print("Numero invalido")
            return
        fatorial = 1
        for i in range(1, num+1):
            fatorial *= i
        print(f"{num}! = {fatorial}\n")
            
    def calcula_fibonarial(self):
        fibonarial = 1
        for i in range(1, self.maximo+1):
            fibonarial *= self.calcula_fibonacci()
            print(fibonarial)
            
    def calcula_primo(self):
        
        print(f"\nNúmeros primos até {self.maximo}: ")
        # crivo de erastotenes
        
        numeros = [True]*self.maximo
        numeros[0] = False
        numeros[1] = False
        
        primos = []
        
        for numero, primo in enumerate(numeros):
            if primo == True:
                primos.append(numero)
                print(numero, end = ' ')
                for i in range(numero*2, self.maximo, numero):
                    numeros[i] = False
        print("\n")
        #return primos
    
series = Series()
while True:
    opcao = series.opcoes()
    if opcao == False:
        break
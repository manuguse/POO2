class Casa():
    def __init__(self, cor, num_janelas) -> None:
        self.cor = cor
        self.num_janelas = num_janelas
    
    def troca_cor(self):
        self.cor = input('Digite a nova cor: ')
        
casa1 = Casa('cinza', 6)
casa2 = Casa('branco',4)
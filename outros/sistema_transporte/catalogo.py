class Catalogo:
    
    def __init__(self, veiculos) -> None:
        self.__veiculos = veiculos
        
    def apresentacao(self):
        for veiculo in self.__veiculos:
            print(veiculo) ## eita, vai ter que mostrar tudo
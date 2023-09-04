class MinhaLista():
    def __init__(self,tupla) -> None:
        self.__tupla = tupla
        
    def adiciona(self, elemento):
        self.__tupla += (elemento,)
        print(self.__tupla)
    
    def remove(self, elemento,):
        pass
    
    def organiza(self):
        pass
    
    def inverte(self):
        pass
    
    def remove(self):
        pass
    
lista = MinhaLista((1,2,3))
lista.adiciona((8,9,10))
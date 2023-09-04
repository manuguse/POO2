class Editora():
    def __init__(self, numero, titulo) -> None:
        self.__numero = numero
        self.__titulo = titulo
        
    def get_numero(self):
        return self.__numero
    
    def set_numero(self, numero):
        self.__numero = numero
        
    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo
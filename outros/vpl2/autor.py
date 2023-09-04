class Autor():
    def __init__(self, codigo, nome) -> None:
        self.__codigo = codigo
        self.__nome = nome
        
    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self, codigo):
        self.__codigo = codigo
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
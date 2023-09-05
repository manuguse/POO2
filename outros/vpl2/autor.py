class Autor():
    def __init__(self, codigo, nome) -> None:
        self.__codigo = codigo
        self.__nome = nome
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def set_nome(self, nome):
        self.__nome = nome
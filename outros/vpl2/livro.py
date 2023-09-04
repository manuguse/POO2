from editora import Editora
from autor import Autor


class Livro():
    def __init__(self, codigo, titulo, ano, autores, editora):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = autores
        
    def get_codigo(self):
        return self.__codigo
    
    def get_ano(self):
        return self.__ano
    
    def get_editora(self):
        return self.__editora
    
    def get_autor(self):
        return self.__editora
    
    def get_titulo(self):
        return self.__titulo
    
    def get_autores(self):
        return self.__autores
    
    def set_codigo(self, codigo):
        self.__codigo = codigo
        
    def set_titulo(self, titulo):
        self.__titulo = titulo
        
    def set_ano(self, ano):
        self.__ano = ano
        
    def set_editora(self, editora):
        self.__editora = editora
        
    def incluir_autor(self, autor):
        self.__autores.append(autor)
        
    def excluir_autores(self, autor):
        if autor in self.__autores:
            self.__autores.delete(autor)
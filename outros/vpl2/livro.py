from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro():
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = None
        self.__autores = []
        self.__capitulos = [Capitulo(numeroCapitulo, tituloCapitulo)]
        
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def editora(self):
        return self.__editora
    
    @property
    def autor(self):
        return self.__editora
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autores(self):
        return self.__autores
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
        
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
        
    @ano.setter
    def ano(self, ano):
        self.__ano = ano
        
    @editora.setter
    def editora(self, editora):
        self.__editora = editora
        
    def incluirAutor(self, autor):
        if autor not in self.__autores and type(autor) == Autor:
            self.__autores.append(autor)
        
    def excluirAutor(self, autor):
        if autor in self.__autores:
            self.__autores.remove(autor)

    def incluirCapitulo(self, numero, titulo):
        if self.findCapituloByTitulo(titulo) == None:
            self.__capitulos.append(Capitulo(numero, titulo))

    def excluirCapitulo(self, titulo):
        capitulo = self.findCapituloByTitulo(titulo)
        if capitulo != None:
            self.__capitulos.remove(capitulo)

    def findCapituloByTitulo(self, titulo):
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                return capitulo
        return None
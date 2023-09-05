from livro import Livro

class Biblioteca():

    def __init__(self) -> None:
        self.__livros = []

    def incluirLivro(self, livro:Livro):
        if type(livro) == Livro and livro not in self.__livros:
            self.__livros.append(livro)

    def excluirLivro(self, livro:Livro):
        if type(livro) == Livro and livro in self.__livros:
            self.__livros.remove(livro)

    @property
    def livros(self):
        return self.__livros
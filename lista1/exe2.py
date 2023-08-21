class Biblioteca():
    
    def __init__(self, livros):
        self.livros = livros
        
    def inicia(self):
        opcoes = {1: self.adiciona_livro, 2: self.remove_livro, 3: self.busca}
        opcao = int(input("Bem vindo a biblioteca, o que deseja fazer? \n 1 - Adicionar livro \n 2 - Remover livro \n 3 - Buscar livro \n 4 - Sair "))
        if opcao == 4:
            return False
        opcoes[opcao]()
        return True

    def adiciona_livro(self):
        livro = Livro(input("Digite o titulo do livro: "), input("Digite o nome do autor: "), int(input("Digite o ano de publicacao: ")), input("Digite a editora: "), int(input("Digite a edicao: ")), int(input("Digite o volume: ")))
        self.livros.append(livro)
    
    def remove_livro(self):
        livro = int(input("Digite o nome do livro que deseja remover: "))
        for livro in self.livros:
            if livro.titulo == livro:
                self.livros.pop(livro)
        
    def busca(self):
        busca = {1: self.busca_titulo, 2: self.busca_autor}
        modo = int(input("Digite o modo de busca: \n 1 - Titulo \n 2 - Autor "))
        encontrados = busca[modo](input("Digite o termo de busca: "))
        if encontrados == []:
            print("Nenhum livro encontrado")
        else:
            print("Livros encontrados: ")
            cont = 0
            for livro in encontrados:
                cont += 1
                print(f'{cont} - {livro.titulo}')
            
            escolha = input("Deseja ver as informações de algum livro? (s/n) ").lower()
            if escolha == 's':
                livro = int(input("Digite o numero do livro: "))
                encontrados[livro-1].mostra_infos()
        
    def busca_titulo(self, titulo):
        encontrados = []
        for livro in self.livros:
            if livro.titulo == titulo:
                encontrados.append(livro)            
        return encontrados
    
    def busca_autor(self, autor):
        encontrados = []
        for livro in self.livros:
            if autor in livro.autores:
                encontrados.append(livro)
        return encontrados
    
    

class Livro():
    
    def __init__(self, titulo, autor, ano, editora, edicao, volume):
        self.titulo = titulo.upper()
        self.autor = autor.upper()
        self.ano = ano
        self.editora = editora.upper()
        self.edicao = edicao
        self.volume = volume
        
    def mostra_infos(self):
        print("Titulo: ", self.titulo)
        print("Autor: ", self.autores)
        print("Ano: ", self.ano)
        print("Editora: ", self.editora)
        print("Edicao: ", self.edicao)
        print("Volume: ", self.volume)


biblio = Biblioteca([])

while True:
    opcao = biblio.inicia()
    if opcao == False:
        break
class Site():

    def __init__(self, usuarios, livros):
        self.usuarios = usuarios
        self.livros = livros
        
    def inicia(self):
        usuario_ativo = input('Digite o nome do usuario: ')
        for usuario in self.usuarios:
            if usuario.nome == usuario_ativo:
                return usuario
        print("Usuario nao encontrado")
        
    def busca(self):
        busca = {1: self.busca_titulo, 2: self.busca_autor}
        modo = int(input("Você não está lendo nada. Para achar um livro, digite o modo de busca: \n 1 - Titulo \n 2 - Autor "))
        encontrados = busca[modo]((input("Digite o termo de busca: ")).capitalize())
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
                
                opcao2 = input("Deseja iniciar a leitura? (s/n) ").lower()
                if opcao2 == 's':
                    return encontrados[livro-1]
                else:
                    return True
        
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


class Usuarios():

    def __init__(self, user):
        self.nome = user
        self.pagina_atual = 0
        self.livro_atual = None
        
    def inicia_leitura(self, site):
        if self.livro_atual == None:
            while True:
                livro = site.busca()
                if livro != True:
                    self.livro_atual = livro
                    break
                    
        print(f'\nLendo {self.livro_atual.titulo}:')
        while True:
            print(f'\nPagina: {self.pagina_atual}')
            opcao = int(input(' 1 - passar\n 2 - voltar \n 3 - abandonar leitura\n 4 - sair\n'))
            if opcao == 4:
                return False
            elif opcao == 3:
                self.livro_atual = None
                return True
            elif opcao == 2:
                self.volta_pagina()
            elif opcao == 1:
                condicao = self.pula_pagina()
                if not condicao:
                    return True
        
    def pula_pagina(self):
        if self.pagina_atual == self.livro_atual.paginas:
            print("Você acabou a leitura!")
            self.livro_atual = None
            return False
        else:
            self.pagina_atual += 1
            return True
        
    def volta_pagina(self):
        if self.pagina_atual == 0:
            print("Você está na primeira página!")
        else:
            self.pagina_atual -= 1


class Livro():

    def __init__(self, titulo, autor, ano, editora, edicao, volume, paginas):
        self.titulo = titulo.capitalize()
        self.autor = autor.capitalize()
        self.ano = ano
        self.editora = editora.capitalize()
        self.edicao = edicao
        self.volume = volume
        self.paginas = paginas
        
    def mostra_infos(self):
        print()
        print("Titulo:", self.titulo)
        print("Autor:", self.autor)
        print("Ano:", self.ano)
        print("Editora:", self.editora)
        print("Edicao:", self.edicao)
        print("Volume:", self.volume)


site = Site([Usuarios('mariah'), Usuarios('joao')], [Livro('Livro1', 'Autor1', 2000, 'Editora1', 1, 1, 10), Livro(
    'Livro2', 'Autor2', 2001, 'Editora2', 2, 2, 200), Livro('Livro3', 'Autor3', 2002, 'Editora3', 3, 3, 300)])

usuario = site.inicia()
while True:
    opcao = usuario.inicia_leitura(site)
    if not opcao:
        break
class Aluno():
    def __init__(self, nome, notas) -> None:
        self.__nome = nome
        self.__notas = notas
        self.__num_notas = len(notas)
        
    def calcula_media(self):
        soma = 0
        for nota in self.__notas:
            soma += nota
        media = soma/self.__num_notas
        return media
    
    def mostra_media(self):
        media = self.calcula_media()
        print(f'A média de {self.__nome} é {media:.2f}')
        
alunos = {}

while True:
    nome = input('Insira o nome do aluno: ').capitalize()
    if nome == '':
        break
    notas = []
    for i in range(2):
        nota = float(input(f'Insira a nota {i+1} do aluno: '))
        notas.append(nota)
    alunos[nome] = Aluno(nome, notas)

pesquisa = input('\nInsira o nome do aluno que deseja pesquisar: ').capitalize()
alunos[pesquisa].mostra_media()
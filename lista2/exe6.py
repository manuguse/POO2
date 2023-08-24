class Media():

    def __init__(self, matriz):
        self.__matriz = matriz
        self.__maior7 = 0
        self.__medias = []

    def calcula_media(self):
        for aluno in self.__matriz:
            total = 0
            for nota in aluno:
                total += nota
            media = total/4
            self.add_medias(media)
            if media >= 7:
                self.adiciona_aluno_media()
    
    def mostra_maior(self):
        self.calcula_media()
        print(self.__maior7)
    
    def adiciona_aluno_media(self):
        self.__maior7 += 1
        
    def add_medias(self, media):
        self.__medias.append(media)
        
notas = Media([[3,7,8,9], [10,10,5.5,6.7], [10,10,2,10]])
notas.mostra_maior()
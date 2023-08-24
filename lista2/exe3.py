class Notas():

    def __init__(self, notas):
        self.__notas = notas
        self.__tamanho = 4
        
    def calcula_media(self):
        total = 0
        for nota in self.__notas:
            total += nota
        media = total/self.__tamanho
        print(f"{media:.2f}")
        
notas1 = Notas([4,5,9,9.6])
notas1.calcula_media()

notas2 = Notas([3,7,8,3.5])
notas2.calcula_media()
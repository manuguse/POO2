class Notas():

    def __init__(self, notas):
        self.notas = notas
        self.tamanho = 4
        
    def calcula_media(self):
        total = 0
        for nota in self.notas:
            total += nota
        media = total/self.tamanho
        print(media)
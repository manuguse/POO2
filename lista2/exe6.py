class Media():

    def __init__(self, matriz):
        self.matriz = matriz

    def calcula_media(self):
        medias = []
        total = 0
        for aluno in self.matriz:
            for nota in aluno:
                total += nota
            media = total/4

class Temperatura():
    
    def __init__(self, temperaturas) -> None:
        self.temperaturas = temperaturas
        
    def calcula_media(self):
        soma = 0
        for temperatura in self.temperaturas:
            soma += temperatura
        media = soma/12
        return media
    
    def compara(self):
        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        media = self.calcula_media()
        for i, temperatura in enumerate(self.temperaturas):
            if temperatura > media:
                print(f"{i+1} - {meses[i]}")
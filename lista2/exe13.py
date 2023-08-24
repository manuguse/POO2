class Temperatura():
    
    def __init__(self, temperaturas) -> None:
        self.__temperaturas = temperaturas
        
    def calcula_media(self):
        soma = 0
        for temperatura in self.__temperaturas:
            soma += temperatura
        media = soma/12
        return media
    
    def compara(self):
        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        media = self.calcula_media()
        print('Temperaturas acima da media:')
        for i, temperatura in enumerate(self.__temperaturas):
            if temperatura > media:
                print(f"{i+1} - {meses[i]}: {temperatura}")
                
temp1 = Temperatura([5,9,32,46,3,2,78,6,5,3,33.4,32])
temp1.compara()
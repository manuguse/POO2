class Interrogratorio():
    
    def __init__(self) -> None:
        self.__pontos = 0
        self.__respostas = []
        
    def inicia(self):
        self.pergunta()
        self.calcula()
        print(self.classifica())
        
    def pergunta(self):
        opcoes = {"s":True, "n":False}
        
        pergunta1 = input("Telefonou para a vítima? (s/n) ").lower()
        self.__respostas.append(opcoes[pergunta1])
            
        pergunta2 = input("Esteve no local do crime? (s/n) ").lower()
        self.__respostas.append(opcoes[pergunta2])
            
        pergunta3 = input("Mora perto da vítima? (s/n) ").lower()
        self.__respostas.append(opcoes[pergunta3])
            
        pergunta4 = input("Devia para a vítima? (s/n) ").lower()
        self.__respostas.append(opcoes[pergunta4])
            
        pergunta5 = input("Já trabalhou com a vítima? (s/n) ").lower()
        self.__respostas.append(opcoes[pergunta5])        
        
    def classifica(self):
        if self.__pontos == 5:
            return "Assassino"
        if self.__pontos >= 3:
            return "Cúmplice"
        if self.__pontos == 2:
            return "Suspeita"
        return "Inocente"
    
    def calcula(self):
        for pergunta in self.__respostas:
            if pergunta == True:
                self.__pontos += 1
                
interrogatorio = Interrogratorio()
interrogatorio.inicia()
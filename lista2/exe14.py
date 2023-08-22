class Interrogratorio():
    
    def __init__(self) -> None:
        self.pontos = 0
        self.respostas = []
        
    def inicia(self):
        self.pergunta()
        self.calcula()
        print(self.classifica())
        
    def pergunta(self):
        pergunta1 = input("Telefonou para a vítima? (s/n) ").lower()
        if pergunta1 == "s":
            self.respostas.append("True")
        else:
            self.respostas.append("False")
            
        pergunta2 = input("Esteve no local do crime? (s/n) ").lower()
        if pergunta2 == "s":
            self.respostas.append("True")
        else:
            self.respostas.append("False")
        pergunta3 = input("Mora perto da vítima? (s/n) ").lower()
        if pergunta3 == "s":
            self.respostas.append("True")
        else:
            self.respostas.append("False")
        pergunta4 = input("Devia para a vítima? (s/n) ").lower()
        if pergunta4 == "s":
            self.respostas.append("True")
        else:
            self.respostas.append("False")
        pergunta5 = input("Já trabalhou com a vítima? (s/n) ").lower()
        if pergunta5 == "s":
            self.respostas.append("True")
        else:
            self.respostas.append("False")
        
    def classifica(self):
        if self.pontos == 5:
            return "Assassino"
        if self.pontos == 4 or self.pontos == 3:
            return "Cúmplice"
        if self.pontos == 2:
            return "Suspeita"
        return "Inocente"
    
    def calcula(self):
        for pergunta in self.respostas:
            if pergunta == "True":
                self.pontos += 1
                
interrogatorio = Interrogratorio()
interrogatorio.inicia()
class Atleta():
    
    def __init__(self, nome, saltos) -> None:
        self.__nome = nome
        self.__saltos = saltos
        self.__num_saltos = len(self.__saltos)
        
    def calcula_media(self):
        soma = 0
        for salto in self.__saltos:
            soma += salto
        media = (soma/self.__num_saltos)
        return media
    
    def mostra_saltos(self):
        print("Saltos: ", end="")
        for i, salto in enumerate(self.__saltos):
            if i == self.__num_saltos-1:
                print(f"{salto}")
            else:
                print(f"{salto} ", end="- ")
            
    def mostra_infos(self):
        print(f"\nResultado final:")
        print(f"Atleta: {self.__nome}")
        {self.mostra_saltos()}
        print(f"Média dos saltos: {self.calcula_media():.1f} m")
        print()
        
while True:
    num = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
    nome = input("Atleta: ").capitalize()
    if nome == "":
        break
    saltos = []
    for i in range(5):
        salto = float(input(f"{num[i]} salto: "))
        if salto < 0:
            print("Valor inválido")
            break
        saltos.append(salto)
    atleta = Atleta(nome, saltos)
    atleta.mostra_infos()
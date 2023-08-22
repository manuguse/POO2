class Atleta():
    
    def __init__(self, nome, saltos) -> None:
        self.nome = nome
        self.saltos = saltos
        self.num_saltos = len(self.saltos)
        
    def calcula_media(self):
        soma = 0
        for salto in self.saltos:
            soma += salto
        media = (soma/self.num_saltos)
        return media
    
    def mostra_saltos(self):
        print("Saltos: ", end="")
        for i, salto in enumerate(self.saltos):
            if i == self.num_saltos-1:
                print(f"{salto}")
            else:
                print(f"{salto} ", end="- ")
            
    def mostra_infos(self):
        print(f"\nResultado final:")
        print(f"Atleta: {self.nome}")
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
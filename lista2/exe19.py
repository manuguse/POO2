class Pesquisa():
    
    def __init__(self, respostas):
        self.__respostas = respostas
        self.__opcoes = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
        
    def mostra_resultado(self):
        print("\nSistema Operacional     Votos     %")
        print("---------------------------------------")
        self.mostra_infos()
        print("---------------------------------------")
        print(f"\nO Sistema Operacional mais votado foi o {self.__opcoes[self.calcula_melhor()]}, com {max(self.__respostas)} votos, correspondendo a {self.calcula_porcentagem(self.__respostas[self.calcula_melhor()]):.2f}% dos votos.")
    
    def calcula_porcentagem(self, resposta):
        return (resposta/self.calcula_num_respostas())*100
    
    def calcula_num_respostas(self):
        num_respostas = 0
        for resposta in self.__respostas:
            num_respostas += resposta
        return num_respostas
    
    def calcula_melhor(self):
        return self.__respostas.index(max(self.__respostas))
    
    def mostra_infos(self):
        for i, resposta in enumerate(self.__respostas):
            print(f"{self.__opcoes[i]:<25} {resposta:<5} {self.calcula_porcentagem(resposta):.1f}%")
        

def recebe_respostas():

    print("Qual o melhor Sistema Operacional para uso em servidores?")
    opcoes = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
    respostas = [0]*6

    for i, opcao in enumerate(opcoes):
        print(f"{i+1} - {opcao}")
        
    while True:
        melhor = int(input("Resposta: "))
        if melhor == 0:
            return respostas
        if melhor > 6 or melhor < 0:
            print("Informe um valor entre 1 e 6 ou 0 para sair!")
        else:
            respostas[melhor-1] += 1
    
pesquisa = Pesquisa(recebe_respostas())
pesquisa.mostra_resultado()
class Consoantes():

    def __init__(self, vetor):
        self.__vetor = vetor
        self.__consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        self.__tamanho = len(vetor)

    def calcula_consoantes(self):
        contagem = 0
        consoantes_vt = []
        for i in range(self.__tamanho):
            if self.__vetor[i] in self.__consoantes:
                contagem += 1
                consoantes_vt.append(self.__vetor[i])
        print(f"num de consoantes: {contagem}")
        print(f"consoantes: ", end="")
        print(consoantes_vt)
        
vetor1 = Consoantes(["c", "d", "a", "e"])
vetor1.calcula_consoantes()
import string

class Frequencia():
    def __init__(self, nome_arquivo, palavra) -> None:
        self.__texto = open(nome_arquivo, "r").read()
        self.__palavra = palavra
        self.__dicionario = {}
        self.adiciona_dict()

    def adiciona_dict(self):
        for palavra in self.__texto.split():
            palavra = palavra.strip(string.punctuation).lower()
            if palavra in self.__dicionario:
                self.__dicionario[palavra] += 1
            else:
                self.__dicionario[palavra] = 1

    def mostra_quantidade(self):
        if self.__palavra not in self.__dicionario:
            print("A palavra não aparece no texto")
        else:
            print(f"A palavra aparece {self.__dicionario[self.__palavra]} vezes")

nome_arquivo = "lista3/texto01.txt"
palavra_busca = "oi"
freq = Frequencia(nome_arquivo, palavra_busca)
freq.mostra_quantidade()

# nao sei como fazer para fechar o arquivo nesse caso
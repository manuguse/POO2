import string

class Frequencia():
    def __init__(self, texto, palavra) -> None:
        self.texto = texto
        self.palavra = palavra
        self.dicionario = {}
        self.adiciona_dict()

    def adiciona_dict(self):
        for palavra in texto.split():
            palavra = palavra.strip(string.punctuation).lower()
            if palavra in self.dicionario:
                self.dicionario[palavra] += 1
            else:
                self.dicionario[palavra] = 1

    def mostra_quantidade(self):
        if self.palavra not in self.dicionario:
            print("A palavra não aparece no texto")
        else:
            print(f"A palavra aparece {self.dicionario[self.palavra]} vezes")

nome_arquivo = "lista3/texto01.txt"
palavra_busca = "oi"
texto = open(nome_arquivo, "r").read()
freq = Frequencia(texto, palavra_busca)
freq.mostra_quantidade()
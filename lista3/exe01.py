import string

texto = open("texto01.txt", "r").read()

def cria_dict(texto):
    dicicionario = {}
    for palavra in texto.split():
        palavra = palavra.strip(string.punctuation).lower()
        if palavra in dicicionario:
            dicicionario[palavra] += 1
        else:
            dicicionario[palavra] = 1
    return dicicionario

dicionario = cria_dict(texto)

palavra = input('Insira a palavra que deseja contar: ').lower()
print(f"A palavra aparece {dicionario[palavra]} vezes")
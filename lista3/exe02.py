import string

texto = open("texto01.txt", "r").read()
stopwords = open("texto02.txt", "r").read()

def cria_dict(texto):
    dicicionario = {}
    for palavra in texto.split():
        palavra = palavra.strip(string.punctuation).lower()
        if palavra in dicicionario:
            dicicionario[palavra] += 1
        else:
            dicicionario[palavra] = 1
    return dicicionario

def remove_stopwords(dicionario, stopwords):
    for palavra in stopwords.split():
        palavra = palavra.strip(string.punctuation).lower()
        if palavra in dicionario:
            dicionario.pop(palavra)
    return dicionario

dicionario = cria_dict(texto)
dicionario = remove_stopwords(dicionario, stopwords)
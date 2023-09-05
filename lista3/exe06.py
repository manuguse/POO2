import random

def cria_frozenset():
    frozenset = set()
    for i in range(30):
        frozenset.add(random.randint(0, 100))
    return frozenset

def cria_frozensets():
    frozensets = []
    for i in range(10):
        frozensets.append(cria_frozenset())
    return frozensets

def cria_dict(frozensets):
    dicionario = {}
    for i, frozenset in enumerate(frozensets):
        chave = tuple(frozenset)
        dicionario[chave] = 0
        for numero in frozenset:
            dicionario[chave] += numero
    return dicionario

print(cria_dict(cria_frozensets()))
##### INCOMPLETO ######

corredores = {}

num_corredores = 2
num_voltas = 2

for i in range(num_corredores):
    nome = input(f"Insira o nome do corredor {i+1}: ").capitalize()
    corredores[nome] = []
    for j in range(num_voltas):
        tempo = float(input(f"Insira o tempo do corredor {i+1} na volta {j+1}: "))
        corredores[nome].append(tempo)
                
def calcula_medias():
    medias = {}
    for corredor in corredores:
        media = 0
        for volta in corredores[corredor]:
            media += volta
        medias[corredor] = media/num_voltas
    return medias 

def calcula_ordem():
    medias = calcula_medias()
    for piloto in medias:
        pass

def calcula_melhor_volta():
    melhor_volta = {}
    melhor_volta["tempo"] = 100000000
    melhor_volta["corredor"] = ""
    for corredor in corredores:
        for volta in corredores[corredor]:
            if volta < melhor_volta["tempo"]:
                melhor_volta["tempo"] = volta
                melhor_volta["corredor"] = corredor
    print(f"Melhor Volta: {melhor_volta['corredor']} - {melhor_volta['tempo']}s")

calcula_melhor_volta()
calcula_ordem()
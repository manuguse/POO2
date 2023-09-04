class Agenda():
    def __init__(self) -> None:
        self.__telefones = {'Maria':[45775533, 4959492], 'Joao':[3949492]}

    def incluir_novo_nome(self):
        nome = input("Insira o nome de contato: ").capitalize()
        telefone = []
        while True:
            numero = int(input("Insira o numero: "))
            telefone.append(numero)
            confirma = input("Deseja inserir mais um numero? (s/n)").lower()
            if confirma == "n":
                break
        self.__telefones[nome] = telefone
        
    def incluir_telefone(self):
        nome = input("Insira o nome de contato: ").capitalize()
        if nome in self.__telefones:
            telefone = int(input("Insira o numero: "))
            self.__telefones[nome].append(telefone)
        else:
            opcao = input("Deseja inserir um novo contato? (s/n)").lower()
            if opcao == "s":
                self.incluir_novo_nome()
                
    def excluir_telefone(self):
        nome = input("Insira o nome de contato: ").capitalize()
        if nome in self.__telefones:
            if len(telefone) == 1:
                self.__telefones.pop(nome)
            else:
                telefone = int(input("Insira o numero: "))
                if telefone in self.__telefones[nome]:
                    self.__telefones[nome].remove(telefone)
                else:
                    print("Numero não encontrado")
        else:
            print("Contato não encontrado")
            
    def excluir_nome(self):
        nome = input("Insira o nome de contato: ").capitalize()
        if nome in self.__telefones:
            self.__telefones.remove(nome)
        else:
            print("Contato não encontrado")
            
    def consultar_telefone(self):
        nome = input("Insira o nome de contato: ").capitalize()
        if nome in self.__telefones:
            print(self.__telefones[nome])
        else:
            print("Contato não encontrado")
            
agenda = Agenda()
while True:
    opcoes = [agenda.incluir_novo_nome, agenda.incluir_telefone, agenda.excluir_telefone, agenda.excluir_nome, agenda.consultar_telefone]
    opcao = int(input("1 - Incluir novo nome\n2 - Incluir telefone\n3 - Excluir telefone\n4 - Excluir nome\n5 - Consultar telefone\n6 - Sair\n"))
    if opcao == 6:
        break
    else:
        print()
        opcoes[opcao-1]()
        print()
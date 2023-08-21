class Conta():
    def __init__(self, clientes):
        self.saldo = 0
        self.limite = 10000
        self.clientes = clientes
        
    def opcoes(self):
        opcoes = [self.deposita, self.saca, self.extrato, self.detalhes]
        opcao = int(input("Digite a opção desejada: \n 1 - deposito \n 2 - saque \n 3 - extrato \n 4 - detalhes \n 5 - sair \n"))
        if opcao == 5:
            return False
        else:
            opcoes[opcao-1]()
            return True
        
    def deposita(self):
        valor = int(input("Digite o valor a ser depositado: "))
        self.saldo += valor
        
    def saca(self):
        valor = int(input("Digite o valor a ser sacado: "))
        if self.saldo < valor:
            print("Saldo insuficiente\n")
        else:
            self.saldo -= valor
            
    def extrato(self):
        print(f"Saldo: {self.saldo}\n")
        
    def detalhes(self):
        print("\nDetalhes da conta: ")
        print(f"Saldo: {self.saldo}")
        print(f"Limite: {self.limite}")
        if self.clientes == []:
            print("Nenhum cliente")
        else:
            print(f"Clientes:")
            for cliente in self.clientes:
                print(f" Nome: {cliente.get_nome()}")
                print(f" Telefone: {cliente.get_telefone()}")
            print()
        
class ContaEspecial(Conta):
    def __init__(self):
        super().__init__()
        self.limite = 10000
        
    def rendimento(self):
        # nao sei como verificar se ja passou um mes
        self.saldo *= 1.1
        
class Cliente():
    def __init__(self, nome, telefone) -> None:
        self.nome = nome
        self.telefone = telefone
        
    def get_nome(self):
        return self.nome
    
    def get_telefone(self):
        return self.telefone
    
banco = Conta([Cliente("Joao", "123456789"), Cliente("Maria", "987654321")])
    
while True:
    opcao = banco.opcoes()
    if opcao == False:
        break
from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes
    
    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def incluiCliente(self, codigo:int, nome:str) -> None:
        if self.__clientes != []:
            for cliente_lista in self.__clientes:
                if cliente_lista.codigo == codigo:
                    return
        self.clientes.append(Cliente(codigo, nome))

    def incluiTecnico(self, codigo:int, nome:str) -> None:
        if self.__tecnicos != []:
            for tecnico_lista in self.__tecnicos:
                if tecnico_lista.codigo == codigo:
                    return
        self.tecnicos.append(Tecnico(codigo, nome))
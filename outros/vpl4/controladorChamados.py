from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self) -> None:
        super().__init__()
        self.__chamados = []
        self.__tiposChamados = []

    @property
    def chamados(self) -> list:
        return self.__chamados
    
    @property
    def tipoChamados(self) -> list:
        return self.__tiposChamados

    def totalChamadosPorTipo(self, tipo: TipoChamado) -> int:
        total = 0
        for chamado in self.__chamados:
            if chamado.tipo.codigo == tipo:
                total += 1
        return total
    
    def incluiChamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, 
                      descricao: str, prioridade: int, tipo: TipoChamado) -> Chamado:
        
        for chamado_lista in self.__chamados:
            if chamado_lista.data == data and chamado_lista.cliente == cliente and chamado_lista.tecnico == tecnico and chamado_lista.tipo == tipo:
                return
        self.__chamados.append(Cliente(data, cliente, tecnico, titulo, descricao, prioridade, tipo))

    def incluiTipoChamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        for chamado_lista in self.__chamados:
            if chamado_lista.codigo == codigo:
                return
        self.__tiposChamados.append(TipoChamado(codigo, nome, descricao))
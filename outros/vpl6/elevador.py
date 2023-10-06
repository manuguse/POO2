from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException
from comandoInvalidoException import ComandoInvalidoException



class Elevador(AbstractElevador):
    def __init__(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        super().__init__()
        self.__andarAtual = andarAtual
        self.__totalAndaresPredio = totalAndaresPredio
        self.__capacidade = capacidade
        self.__totalPessoas = totalPessoas
        
    @property
    def capacidade(self) -> int:
    	return self.__capacidade
    
    @property
    def totalPessoas(self) -> int:
    	return self.__totalPessoas

    @property
    def totalAndaresPredio(self) -> int:
    	return self.__totalAndaresPredio

    @property
    def andarAtual(self) -> int:
    	return self.__andarAtual

    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int):
        if type(totalAndaresPredio) != int or totalAndaresPredio <= 0:
            raise ComandoInvalidoException
        else:
    	    self.__totalAndaresPredio = totalAndaresPredio 

        
    def descer(self) -> str:
        if self.__andarAtual == 0:
            raise ElevadorJahNoTerreoException()
        else:
            self.__andarAtual -= 1
            return f"Descendo para o andar {self.__andarAtual}"
        
    def entraPessoa(self) -> str:
        if self.__totalPessoas == self.__capacidade:
            raise ElevadorCheioException()
        else:
            self.__totalPessoas += 1
            return f"Entrou uma pessoa. Total de pessoas: {self.__totalPessoas}"
        
    def saiPessoa(self) -> str:
        if self.__totalPessoas == 0:
            raise ElevadorJahVazioException()
        else:
            self.__totalPessoas -= 1
            return f"Saiu uma pessoa. Total de pessoas: {self.__totalPessoas}"
        
    def subir(self) -> str:
        
        print('andarAtual: ', self.__andarAtual)
        print('totalAndaresPredio: ', self.__totalAndaresPredio)
        if self.__andarAtual == self.__totalAndaresPredio:
            raise ElevadorJahNoUltimoAndarException()
        else:
            self.__andarAtual += 1
            return f"Subindo para o andar {self.__andarAtual}"
from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador

class ControladorElevador(AbstractControladorElevador):
    
    def __init__(self):
        super().__init__()
        self.__elevador = None
        
    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int, capacidade:int, totalPessoas:int) -> None:
        errors = [(type(andarAtual) != int or type(totalAndaresPredio) != int or type(capacidade) != int or type(totalPessoas) != int), 
                  (andarAtual < 0 or totalAndaresPredio <= 0 or capacidade <= 0 or totalPessoas < 0),
                  (andarAtual > totalAndaresPredio),
                  (totalPessoas > capacidade)]
        for i, error in enumerate(errors):
            if error:
                print('andarAtual: ', andarAtual)
                print(f"------------------------ ERRO EM {i} ---------------------------------")
                raise ComandoInvalidoException()
        self.__elevador = Elevador(andarAtual, totalAndaresPredio, capacidade, totalPessoas)
    
    def subir(self) -> str:
        self.__elevador.subir()
        
    def descer(self) -> str:
        self.__elevador.descer()
        
    def entraPessoa(self) -> str:
        self.__elevador.entraPessoa()
    
    def saiPessoa(self) -> str:
        self.__elevador.saiPessoa()
        
    @property
    def elevador(self) -> Elevador:
        return self.__elevador
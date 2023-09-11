class Transporte:
    
    def __init__(self, nome, altura, comprimento, carga, velocidade) -> None:
        self.__nome = nome
        self.__altura = altura
        self.__comprimento = comprimento
        self.__carga = carga
        self.__velocidade = velocidade
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
        
    @property
    def comprimento(self):
        return self.__comprimento
    
    @comprimento.setter
    def comprimento(self, comprimento):
        self.__comprimento = comprimento
        
    @property
    def carga(self):
        return self.__carga
    
    @carga.setter
    def carga(self, carga):
        self.__carga = carga
        
    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade
        
class TransporteAereo(Transporte):
    
    def __init__(self, nome, altura, comprimento, carga, velocidade, autonomia, envergadura) -> None:
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__autonomia = autonomia
        self.__envergadura = envergadura
        
    @property
    def autonomia(self):
        return self.__autonomia
    
    @autonomia.setter
    def autonomia(self, autonomia):
        self.__autonomia = autonomia
        
    @property
    def envergadura(self):
        return self.__envergadura
    
    @envergadura.setter
    def envergadura(self, envergadura):
        self.__envergadura = envergadura
        
class TransporteTerrestre(Transporte):
    
    def __init__(self, nome, altura, comprimento, carga, velocidade, motor, rodas):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__motor = motor
        self.__rodas = rodas
        
    @property
    def motor(self):
        return self.__motor
    
    @motor.setter
    def motor(self, motor):
        self.__motor = motor
        
    @property
    def rodas(self):
        return self.__rodas
    
    @rodas.setter
    def rodas(self, rodas):
        self.__rodas = rodas
        
class TransporteAquatico(Transporte):
    
    def __init__(self, nome, altura, comprimento, carga, velocidade, boca, calado):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__motor = boca
        self.__calado = calado
        
    @property  
    def boca(self):
        return self.__boca
    
    @boca.setter
    def boca(self, boca):
        self.__boca = boca
        
    @property
    def calado(self):
        return self.__calado
    
    @calado.setter
    def boca(self, calado):
        self.__calado = calado
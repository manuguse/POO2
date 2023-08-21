class Televisao():
    
    def __init__(self,  canal, tamanho, marca):
        self.ligada = False
        self.canal = canal
        self.tamanho = tamanho
        self.marca = marca
        self.canal_maximo = 99
        self.canal_minimo = 1
        
    def muda_canal_cima(self):
        if self.canal + 1 <= self.canal_maximo:
            self.canal += 1
        else:
            self.canal = self.canal_minimo
    
    def muda_canal_baixo(self):
        if self.canal - 1 >= self.canal_minimo:
            self.canal -= 1
        else:
            self.canal = self.canal_maximo
""" 
tv1 = Televisao(87, 32, 'LG')
tv2 = Televisao(43, 40, 'samsung')

print(tv1)
print(tv2)
"""

#7
class Estados():
    def __init__(self, nome, sigla, cidades):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades
        
    def soma_pop(self):
        soma = 0
        for cidade in self.cidades:
            soma += cidade.get_populacao()
        return soma


class Cidades():
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao
        
    def get_populacao(self):
        return self.populacao
    
estado1 = Estados('Rio Grande do Sul', 'RS', [Cidades('Porto Alegre', 1484941), Cidades('Canoas', 346682), Cidades('Caxias do Sul', 517451)])
estado2 = Estados('Santa Catarina', 'SC', [Cidades('Florianopolis', 508826), Cidades('Joinville', 590466), Cidades('Blumenau', 359728)])
estado3 = Estados('Parana', 'PR', [Cidades('Curitiba', 1948626), Cidades('Londrina', 575377), Cidades('Maringa', 430731)])

#print(estado3.soma_pop())

# 8
import math
class Calculos():
    def __init__(self, coordenadas) -> None:
        self.coordenadas = coordenadas
        
    def mostra(self, k):
        print(self.coordenadas[k].get_x())
        print(self.coordenadas[k].get_y())
        
    def distancia(self, k1, k2):
        x1 = self.coordenadas[k1].get_x()
        y1 = self.coordenadas[k1].get_y()
        x2 = self.coordenadas[k2].get_x()
        y2 = self.coordenadas[k2].get_y()
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def compara_coordenadas(self):
        # não entendi o que é pra comparar
        pass
    
    def coordenada_polar(self, k):
        x = self.coordenadas[k].get_x()
        y = self.coordenadas[k].get_y()
        raio = math.sqrt(x**2 + y**2)
        angulo = math.degrees(math.atan2(y,x))
        coordenada_polar = (raio, angulo)
        return coordenada_polar
        
class Coordenada():
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
                
coor1 = Coordenada(1,5)
coor2 = Coordenada(5,6)
coor3 = Coordenada(10,65)
calculo = Calculos([coor1, coor2, coor3])

# 9 (nao entendi direito o que quer)

class Quadrado():
    def __init__(self, lado):
        self.lado = lado
        
    def calcula_area(self):
        area = self.lado**2
        print('área: ', area)
        
    def calcula_perimetro(self):
        perimetro = self.lado*4
        print('perímetro: ', perimetro)
        
class Retangulo():
    def __init__(self, comp, larg) -> None:
        self.comp = comp
        self.larg = larg
        
    def calcula_area(self):
        area = self.comp*self.larg
        return area
    
    def calcula_perimetro(self):
        perimetro = 2*(self.comp+self.larg)
        return perimetro
    
class Circulo():
    def __init__(self, raio) -> None:
        self.raio = raio
        
    def calcula_area(self):
        area = math.pi*self.raio**2
        return area
    
    def calcula_periimetro(self):
        perimetro = 2*math.pi*self.raio
        return perimetro
    
# 10
class Fracao():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def soma(self):
        return self.num1 + self.num2
    
    def subtracao(self):
        return self.num1 - self.num2
    
    def multiplicacao(self):
        return self.num1*self.num2
    
    def divisao(self):
        return self.num1/self.num2
    
    def mostra_formato(self):
        print(f'{self.num1}/{self.num2}')
        
    def inverte(self):
        self.num1, self.num2 = self.num2, self.num1
        
    def valor_real(self):
        return self.num1/self.num2
    
    def cria_fracao(self):
        # nao entendi o que isso quis dizer
        pass
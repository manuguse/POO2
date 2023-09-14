from animal import Animal
from abc import ABC, abstractmethod

class Mamifero(Animal):
    def __init__(self, volume_som, tamanho_passo):
        super().__init__(tamanho_passo)
        self.__volume_som = volume_som
        
    @property
    def volume_som(self):
        return self.__volume_som
    
    @volume_som.setter
    def volume_som(self, volume_som):
        self.__volume_som = volume_som
       
    @abstractmethod
    def produzir_som(self):
        pass
    

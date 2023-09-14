from mamifero import Mamifero

class Gato(Mamifero):
    def __init__(self, volume_som = 2, tamanho_passo = 2):
        super().__init__(volume_som, tamanho_passo)
       
    def produzir_som(self):
        return ((f"mamifero: produz som: {self.volume_som} som: miau").upper())
     
    def miar(self):
        return self.produzir_som()
    
    def mover(self):
        return (f"ANIMAL: DESLOCOU {self.tamanho_passo}")
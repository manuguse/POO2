from random import randrange

class Forca():
    def __init__(self, palavras):
        self.palavras = palavras
        self.palavra_secreta = ''
        self.mostra_usuario = []
        self.perdeu = False
        self.vidas = 6
        
    def inicia_jogo(self):
        self.vidas = 6
        self.perdeu = False
        self.palavra_secreta = self.palavras[randrange(len(self.palavras))]
        self.mostra_usuario = ['_']*len(self.palavra_secreta)
        while True:
            print(self.mostra_usuario)
            print(f"Vidas: {self.vidas}")
            self.adivinha_letra()
            if '_' not in self.mostra_usuario:
                print("Você ganhou!")
                break
            if self.perdeu:
                print("Você perdeu!")
                break
        print(f"A palavra era {self.palavra_secreta}")
        continua = input("Deseja jogar novamente? (s/n) ").lower()
        if continua == 's':
            return True
        else:
            print("Obrigado por jogar!")
            return False
        
        
    def reinicia(self):
        self.perdeu = False
        self.vidas = 6
        
    def adivinha_letra(self):
        status = False
        letra = input("Digite uma letra: ")
        for i, letra_at in enumerate(self.palavra_secreta):
            if letra == letra_at:
                self.mostra_usuario[i] = letra_at
                status = True
        if not status:
            self.perde_vida()
                
    def perde_vida(self):
        self.vidas -= 1
        if self.vidas == 0:
            self.perdeu = True
            
forca = Forca(['livro', 'casa', 'pano', 'cores'])
while True:
    continua = forca.inicia_jogo()
    if not continua:
        break
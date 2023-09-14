from transportes import Transporte, TransporteTerrestre, TransporteAquatico, TransporteAereo

class Catalogo:
    
    def __init__(self, veiculos) -> None:
        self.__veiculos = veiculos
        self.__caracteristicas = {TransporteAereo: ["autonomia", "envergadura"], TransporteTerrestre: ["motor", "rodas"], TransporteAquatico: ["propulsao", "helicidade"]}
        
    def apresentacao(self):
        for veiculo in self.__veiculos:
            print(f"Nome: {veiculo.nome}")
            print(f"Altura: {veiculo.altura}")
            print(f"Comprimento: {veiculo.comprimento}")
            print(f"Carga: {veiculo.carga}")
            print(f"Velocidade: {veiculo.velocidade}")
        for caracteristica in self.__caracteristicas[type(veiculo)]:
            print(f"{caracteristica}: {veiculo.caracteristica}")
            
veiculos = [TransporteAereo("Boeing 747", 19.4, 70.6, 412750, 988, 14200, 64.4), TransporteTerrestre("Ferrari 488", 1.21, 4.57, 190, 330, "V8", 4), TransporteAquatico("Titanic", 53.3, 269.1, 46328, 23, "Vapor", 3)]
catalogo = Catalogo(veiculos)
catalogo.apresentacao()
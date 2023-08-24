class SomaQuadrados():
    def __init__(self, vetor):
        self.__vetor = vetor

    def calcula(self):
        resultado = 0
        for numero in self.__vetor:
            resultado += numero**2
        print(resultado)
        print()
        
nums1 = SomaQuadrados([4,5,6,7])
nums1.calcula()

nums2 = SomaQuadrados([4,5,-1,2])
nums2.calcula()
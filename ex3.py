class Retangulo:

    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mostraLado(self):
        return self.ladoA, self.ladoB
    
    def area(self):
        return self.ladoA*self.ladoB
    
    def perimetro(self):
        return 2*self.ladoA+2*self.ladoB
    
c = float(input("Qual o comprimento (em m): "))
h = float(input("Qual a altura (em m): "))

a = Retangulo(c, h)

print(f"o perimetro eh: {a.perimetro()} m")

print(f"a area eh: {a.area()} m2")
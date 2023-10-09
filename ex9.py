class Ponto:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def impValor(self):
        return f"o x eh {self.x} e o y eh {self.y}"

class Retangulo:

    def __init__(self, l, h, pontoInicial):

        self.l = l
        self.h = h
        self.pi = pontoInicial

    def acharCentro(self):

        centroX = (self.l + self.pi.x)/2
        centroY = (self.h + self.pi.y)/2

        return Ponto(centroX, centroY)

def menu():

    print("1. criar retangulo")
    print("2. achar centro do retangulo")
    print("3. sair")

retangulos = []

while True:

    menu()

    escolha = int(input("escolha uma opcao: "))

    if escolha == 1:

        largura = float(input("Qual a largura do retangulo: "))
        altura = float(input("Qual a altura do retangulo: "))
        x = float(input("Qual a coordenada x do ponto inicial: "))
        y = float(input("Qual a coordenada y do ponto inicial: "))

        pontoInicial = Ponto(x, y)

        ret = Retangulo(largura, altura, pontoInicial)
        retangulos.append(ret)

    elif escolha == 2:

        for ret in retangulos:
            centro = ret.acharCentro()
            print(centro.impValor())
    elif escolha == 3:
        break
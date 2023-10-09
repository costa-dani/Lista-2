import random

class Bichinho:

    def __init__(self, fome, tedio, saude=10):
        
        self.f = fome
        self.t = tedio
        self.s = saude

    def alimentar(self):

        self.f -= 2
        self.s += 1

    def brincar(self):

        if self.t - 2 >= 0 :
            self.t -= 2

        else:
            self.t = 0

        self.f += 1
        self.s -= 1

        if self.s < 0:

            self.s = 0
            return "voce matou o bichinho de tanto brincar"
        
        elif self.s >= 0:

            return "brincaram"

    def ouvir(self):

        self.s += 2
        self.t += 1

    def __str__(self):
        return f"\nFome: {self.f}\nTedio: {self.t}\nSaude: {self.s}"
    
def menu():
    print("1. ver status")
    print("2. alimentar")
    print("3. brincar")
    print("4. ouvir")
    print("5. sair")

tedioP = random.randint(5, 10)
fomeP = random.randint(0, 5)
porquECA = Bichinho(fomeP, tedioP)

tedioG = random.randint(5, 10)
fomeG = random.randint(0, 5)
girafECA = Bichinho(fomeG, tedioG)

tedioE = random.randint(5, 10)
fomeE = random.randint(0, 5)
elefantECA = Bichinho(fomeE, tedioE)

while True:

    menu()

    escolha = int(input("\nO que voce quer fazer: "))

    if escolha == 1:

        print(f"porquECA:\n{porquECA}")
        print(f"\ngirafECA:\n{girafECA}")
        print(f"\nelefantECA:\n{elefantECA}")

    if escolha == 2:

        porquECA.alimentar()
        girafECA.alimentar()
        elefantECA.alimentar()

    if escolha == 3:

        if porquECA and girafECA and elefantECA: 
            print(porquECA.brincar())
            print(girafECA.brincar())
            print(elefantECA.brincar())

    elif escolha == 4:

        porquECA.ouvir()
        girafECA.ouvir()
        elefantECA.ouvir()

    elif escolha == 5:
        break
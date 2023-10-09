class Carro:

    def __init__(self, consumoComb, qntdComb=0):
        
        self.cc = consumoComb
        self.qc = qntdComb

    def andar(self, km):
        
        comb = km/self.cc
        
        if self.qc - comb < 0:

            return "Nao tem combustivel suficiente"
        
        elif self.qc - comb > 0:

            self.qc -= comb

            return f"O carro andou {km} km"

    def obterGasolina(self):
        
        return f"Ainda resta(m) {self.qc:.2f}L"

    def adicionarGasolina(self, litro):
        
        self.qc += litro

def menu():

    print("1. abastecer")
    print("2. andar")
    print("3. ver gasolina")
    print("4. sair")

consumo = float(input("Qual o consumo do carro: "))

corollinha = Carro(consumo)

while True:

    menu()

    escolha = int(input("O que voce quer fazer: "))

    if escolha == 1:

        litro = float(input("Quantos litros deseja colocar: "))
        corollinha.adicionarGasolina(litro)

    elif escolha == 2:

        km = float(input("O quanto voce quer andar: "))
        print(corollinha.andar(km))

    elif escolha == 3:

        print(corollinha.obterGasolina())

    elif escolha == 4: 
        break
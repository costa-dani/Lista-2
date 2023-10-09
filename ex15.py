class Tamagotchi:

    def __init__(self, nome, fome=0, saude=10, idade=0, tedio=10):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.tedio = tedio

    def alterarNome(self, novoNome):
        self.nome = novoNome

    def alimentar(self, quantidade):
        self.fome -= quantidade

    def brincar(self, tempo):
        self.tedio -= tempo

    def envelhecer(self):
        self.idade += 1
        self.fome += 1
        self.tedio += 1

    def calcularHumor(self):
        humor = self.saude - self.fome
        return humor

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def retornarTedio(self):
        return self.tedio
    
def menu():
    print("1. alterar nome")
    print("2. alimentar")
    print("3. brincar")
    print("4. envelhecer")
    print("5. calcular humor")
    print("6. retornar nome")
    print("7. retornar fome")
    print("8. retornar saúde")
    print("9. retornar idade")
    print("10. retornar tédio")
    print("11. sair")

n = input("Qual o nome do Tamagotchi: ")

ser = Tamagotchi(n)

while True: 

    menu()

    escolha = int(input("O que voce quer fazer: "))

    if escolha == 1:
        
        nv = input("Qual o novo nome: ")
        ser.alterarNome(nv)

    elif escolha == 2:

        quantidade = int(input("Quantidade de comida: "))
        ser.alimentar(quantidade)

    elif escolha == 3:

        tempo = int(input("Tempo de brincadeira: "))
        ser.brincar(tempo)

    elif escolha == 4:
        ser.envelhecer()

    elif escolha == 5:

        humor = ser.calcularHumor()
        print(f"O humor do Tamagotchi é: {humor}")

    elif escolha == 6:
        print(ser.retornarNome())

    elif escolha == 7:
        print(ser.retornarFome())

    elif escolha == 8:
        print(ser.retornarSaude())

    elif escolha == 9:
        print(ser.retornarIdade())

    elif escolha == 10:
        print(ser.retornarTedio())

    elif escolha == 11:
        break
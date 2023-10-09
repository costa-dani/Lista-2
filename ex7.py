class Tamagotchi:

    def __init__(self, nome, fome=10, saude=10, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novoNome):
        self.nome = novoNome

    def alterarFome(self):
        self.fome += 1

    def alterarSaude(self):
        self.saude += 1

    def alterarIdade(self):
        self.idade += 1

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

n = input("Qual o nome do Tamagotchi: ")

ser = Tamagotchi(n)

while True: 

    escolha = input("O que voce quer fazer: ")

    if escolha == 'AN':

        nv = input("Qual o novo nome: ")

        ser.alterarNome(nv)

    elif escolha == 'AF':

        ser.alterarFome()

    elif escolha == 'AS':

        ser.alterarSaude()

    elif escolha == 'AI':

        ser.alterarIdade()
    
    elif escolha == 'RN':

        print(ser.retornarNome())

    elif escolha == 'RF':

        print(ser.retornarFome())

    elif escolha == 'RS':

        print(ser.retornarSaude())

    elif escolha == 'RI':

        print(ser.retornarIdade())
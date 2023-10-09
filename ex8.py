class Macaco:

    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        return f"O bucho de {self.nome} tem: {', '.join(self.bucho)}"

    def digerir(self):
        if self.bucho:
            comida_digerida = self.bucho.pop(0)
            return f"{self.nome} digeriu {comida_digerida}. O bucho agora tem: {', '.join(self.bucho)}"
        else:
            return f"{self.nome} não tem nada no bucho para digerir."

quantidade = int(input("Quantos macacos você quer criar: "))

macacos = []

for i in range(quantidade):
    nome = input(f"Qual o nome do macaco {i + 1}: ")
    macaco = Macaco(nome)
    macacos.append(macaco)

while True:
    
    escolha = input("O que você quer fazer: ")

    if escolha == 'comer':
        for i, macaco in enumerate(macacos):
            comida = input(f"O que {macaco.nome} vai comer: ")
            macaco.comer(comida)

    elif escolha == 'verbucho':
        for i, macaco in enumerate(macacos):
            print(macaco.verBucho())

    elif escolha == 'digerir':
        for i, macaco in enumerate(macacos):
            print(macaco.digerir())

    elif escolha == 'sair':
        break
class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        
        if self.idade < 21:
            ser.crescer()

    def engordar(self):
        self.peso += 1

    def emagrecer(self):
        self.peso -= 1

    def crescer(self):
        self.altura += 0.005

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura:.2f}"

n = input("Qual seu nome: ")
i = int(input("Qual a sua idade: "))
p = float(input("Qual o seu peso: "))
h = float(input("Qual a sua altura: "))

ser = Pessoa(n, i, p, h)

while True: 

    escolha = input("O que voce quer fazer: ")

    if escolha == 'env':

        ser.envelhecer()

    elif escolha == 'eng':

        ser.engordar()

    elif escolha == 'ema':

        ser.emagrecer()

    print(ser)
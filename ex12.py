class ContaInvestimento:

    def __init__(self, num, nome, taxaJuros=1.1, saldoInicial=1000):

        self.num = num
        self.nome = nome
        self.tj = taxaJuros
        self.si = saldoInicial

    def adicioneJuros(self):

        self.si = self.si * self.tj
   
n = input("Qual seu nome: ")
c = input("Qual a sua conta: ")

conta = ContaInvestimento(c, n)

for i in range(5): 
    conta.adicioneJuros()

print(f"O saldo atual eh {conta.si:.2f}")
class ContaCorrente:

    def __init__(self, num, nome, saldo=0):
        self.num = num
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, novo):
        self.nome = novo

    def deposito(self, valorDep):
        self.saldo += valorDep

    def saque(self, valorSaq):

        if self.saldo - valorSaq < 0:
            print("Ta duro, dorme, filho")
            
        elif self.saldo - valorSaq >= 0:
            self.saldo -= valorSaq

    def __str__(self):
        return f"Numero da conta: {self.num}\nNome do correntista: {self.nome}\nSaldo: {self.saldo:.2f}"
    
n = input("Qual seu nome: ")
c = input("Qual a sua conta: ")

conta = ContaCorrente(c, n)

while True: 

    escolha = input("O que voce quer fazer: ")

    if escolha == 'alterar':

        nomenovo = input("Qual o novo nome: ")

        conta.alterarNome(nomenovo)
    
    elif escolha == 'depositar':

        VD = float(input("Quanto voce quer depositar: "))

        conta.deposito(VD)

    elif escolha == 'sacar':

        VS = float(input("Quanto voce quer sacar: "))

        conta.saque(VS)

    print(conta)
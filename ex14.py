class Funcionario:

    def __init__(self, nome, salario):

        self.n = nome
        self.s = salario

    def devNome(self):

        return f"O nome eh {self.n}"
    
    def alterarNome(self, novo):

        self.n = novo

    def devSalario(self):

        return f"O salario eh RS{self.s:.2f}"
    
    def aumentarSalario(self, porcentagem):

        self.s = ((porcentagem/100)+1) * self.s
    
def menu():

    print("1. mudar nome")
    print("2. aumentar salario")
    print("3. ver nome")
    print("4. ver salario")
    print("5. sair")


n = input("Qual o nome: ")
s = float(input("Qual o salario: "))
empregado = Funcionario(n, s)

while True: 

    menu()

    escolha = int(input("O que voce quer fazer: "))

    if escolha == 1: 

        nvnm = input("Qual o novo nome: ")
        empregado.alterarNome(nvnm)

    elif escolha == 2:

        pctg = float(input("Qual a porcentagem do aumento: "))
        empregado.aumentarSalario(pctg)

    elif escolha == 3:
        
        print(empregado.devNome())
        
    elif escolha == 4:
        
        print(empregado.devSalario())
        
    elif escolha == 5:
        break
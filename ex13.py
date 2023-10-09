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
    
    def alterarSalario(self, nvsal):

        self.s = nvsal
    
def menu():

    print("1. mudar nome")
    print("2. mudar salario")
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

        nvs = float(input("Qual o novo salario: "))
        empregado.alterarSalario(nvs)

    elif escolha == 3:
        
        print(empregado.devNome())
        
    elif escolha == 4:
        
        print(empregado.devSalario())
        
    elif escolha == 5:
        break
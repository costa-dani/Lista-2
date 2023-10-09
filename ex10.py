class bombaCombustivel:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):

        self.tc = tipoCombustivel
        self.vl = valorLitro
        self.qc = quantidadeCombustivel
        
    def abastecerPorValor(self, valor):
        
        qntdComb = valor/self.vl
        self.alterarQuantidadeCombustivel(qntdComb)
        return f"Isso paga {qntdComb:.2f}L\nA bomba tem {self.qc}L"

    def abastecerPorLitro(self, litro):
        
        preco = litro * self.vl
        self.alterarQuantidadeCombustivel(litro)
        return f"O preco a se pagar eh {preco:.2f} reais\nA bomba tem {self.qc}L"
    
    def alterarValor(self, novoPreco):
        
        self.vl = novoPreco

    def alterarCombustivel(self, novoCombustivel):
        
        self.tc = novoCombustivel

    def alterarQuantidadeCombustivel(self, qntd):
        
        self.qc = self.qc - qntd

def menu():

    print("1. abastecer por valor")
    print("2. abastecer por litro")
    print("3. alterar valor")
    print("4. alterar combustivel")
    print("5. sair")

tipoCombustivel = input("Qual eh o tipo de combustivel: ")
valorLitro = float(input("Qual eh o valor do litro: "))
quantidadeCombustivel = float(input("Qual eh a quantidade de combustivel: "))

posto = bombaCombustivel(tipoCombustivel, valorLitro, quantidadeCombustivel)

while True: 

    menu()

    escolha = int(input("O que voce quer fazer: "))

    if escolha == 1:

        valor = float(input("O quanto voce quer pagar: "))
        print(posto.abastecerPorValor(valor))

    elif escolha == 2:

        litro = float(input("Quantos litros deseja colocar: "))
        print(posto.abastecerPorLitro(litro))

    elif escolha == 3: 

        novoValor = float(input("Qual eh o novo valor: "))
        posto.alterarValor(novoValor)

    elif escolha == 4:

        novoComb = input("Qual eh o novo combustivel: ")
        posto.alterarCombustivel(novoComb)

    elif escolha == 5:
        break
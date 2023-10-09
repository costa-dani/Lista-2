class TV:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def aumentarVolume(self):

        if self.volume < 100:
            self.volume += 1

    def diminuirVolume(self):

        if self.volume > 0:
            self.volume -= 1

    def canalTV(self, canal):
        self.canal = canal

    def __str__(self):
        return f"Canal: {self.canal}\nVolume: {self.volume}"

c = int(input("Qual canal voce deseja assitir: "))
v = int(input("Qual o volume desejado: "))

tv = TV(c, v)

while True:

    escolha = input("O que voce deseja fazer: ")

    if escolha == 'mudarcanal':

        novocanal = int(input("Qual o novo canal: "))
        tv.canalTV(novocanal)

    elif escolha == 'dim':

        tv.diminuirVolume()

    elif escolha == 'aum':

        tv.aumentarVolume()

    print(tv)
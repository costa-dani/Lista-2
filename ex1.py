class Bola:
    def __init__(self, cor, circ, mat):
        self.cor = cor
        self.circ = circ
        self.mat = mat

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        return self.cor
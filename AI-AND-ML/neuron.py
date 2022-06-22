class Neuron:
    def __init__(self, y=False):
        self.x = []  # lista com todas as entradas
        self.w = []  # lista com todos os pesos de todas as entradas
        self.xw = []  # multiplicação de cada entrada por seu respectivo peso
        self.y = y  # saída desejada
        self.d1 = 0  # saída efetiva
        self.e = 0  # erro
        self.dk = 0.2  # velocidade de aprendizagem, sempre um valor entre 0.1 e 0.2

    def process(self, x, w):
        for i in x:  # lista com todas entradas
            self.x.append(i)

        for i in w:  # lista com todos os pesos das respectivas entradas
            self.w.append(i)

        for i in self.x:  # multiplicação de cada entrada por seu respectivo peso
            self.xw.append(i * self.w[self.x.index(i)])

        for i in self.xw:  # soma de todos os pesos
            self.d1 += i

        if self.d1 >= 0:
            return 1
        elif self.d1 < 0:
            return -1

    def err(self):  # cálculo do erro erro = saída desejada - saída efetiva
        if not self.y == False:
            self.e = self.y - self.d1
        return self.e

    def apply_err(self):
        for i in self.w:
            new_weight = i + self.e
            self.w[self.w.index(i)] = new_weight
        
        x = self.x[:]
        w = self.w[:]
        return self.process(x, w)

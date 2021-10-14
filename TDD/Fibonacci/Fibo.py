class Fibo:
    def __init__(self, qntNum):
        self.ant = 0
        self.prox = 1
        self.iteracao = qntNum

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteracao == 0:
            raise StopIteration
            return StopIteration

        NFib = self.prox + self.ant
        self.ant = self.prox
        self.prox = NFib
        self.iteracao -= 1

        return self.prox


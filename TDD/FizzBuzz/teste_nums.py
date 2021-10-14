import test
from validnum import nunnatural, multipls

class TesteNums:
    def setup(self):
        pass

    def teste_nunnatural(self):
        resultado = nunnatural(-2)
        resultado1 = nunnatural(0)
        resultado2 = nunnatural(3)
        resultado3 = nunnatural(5.4)

        assert resultado == "Não é um número natural"
        assert resultado1 == "É um número natural"
        assert resultado2 == "É um número natural"
        assert resultado3 == "Não é um número natural"

    def teste_multipls(self):
        resultado = multipls(3)
        resultado1 = multipls(7)
        resultado2 = multipls(21)
        resultado3 = multipls(10)

        assert resultado == "Fizz!"
        assert resultado1 == "Buzz!"
        assert resultado2 == "FizzBuzz!"
        assert resultado3 == "Miss!"

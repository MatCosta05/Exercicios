from Fibo import *

qntNum = int(input("Quantos números devem ser gerados?"))
SeqFibo = Fibo(qntNum)


Fibonacci={c+1: SeqFibo for c, SeqFibo in enumerate(SeqFibo)}
print(Fibonacci)
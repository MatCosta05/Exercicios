def nunnatural(x):
    if x >= 0:
        n = int(x)
        m = x * 10
        s = n * 10
        if m == s:
            print("É um número natural")
            return ("É um número natural")
        else:
            print("Não é um número natural")
            return ("Não é um número natural")
    else:
        print("Não é um número natural")
        return ("Não é um número natural")

def multipls(x):
    if x%3 == 0 and x%7 != 0:
        print("Fizz!")
        return("Fizz!")
    elif x%3 != 0 and x%7 == 0:
        print("Buzz!")
        return("Buzz!")
    elif x%3 == 0 and x%7 == 0:
        print("FizzBuzz!")
        return("FizzBuzz!")
    else:
        print("Miss!")
        return("Miss!")


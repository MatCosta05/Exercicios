from requests import post
from json import loads

exapi = post("http://127.0.0.1:8000/exapi", json={"valor1": 24, "valor2": 4, "operação": "MULTIPLICAÇÃO"})
cont = exapi.text

def calc_api():
    resultado = loads(cont)
    if resultado["operação"] == "ADIÇÃO":
        print(resultado["valor1"] + resultado["valor2"])
    elif resultado["operação"] == "SUBTRRAÇÃO":
        print(resultado["valor1"] - resultado["valor2"])
    elif resultado["operação"] == "MULTIPLICAÇÃO":
        print(resultado["valor1"] * resultado["valor2"])
    elif resultado["operação"] == "DIVISÃO":
        print(resultado["valor1"] / resultado["valor2"])
    else:
        print("A operação deve ser escrita das seguintes formas:\n"
              "ADIÇÃO\n"
              "SUBTRAÇÃO\n"
              "MULTIPLICAÇÃO\n"
              "DIVISÃO")
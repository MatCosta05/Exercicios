from requests import get,post, delete
from json import loads, dumps


'''
resposta = get("https://pt.wikipedia.org/wiki/Hypertext_Transfer_Protocol")
#print(resposta.text)
print(resposta.ok)
'''
'''
order = get("https://order-pizza-api.herokuapp.com/api/orders")
orders = loads(order.text)
print(orders)
'''
user = {"username": "test", "password": "test"}
header = {"Content-Type": "application/json"}

token = post("https://order-pizza-api.herokuapp.com/api/auth", json=user)

pizza = {
    "Crust": "NORMAL",
    "Flavor": "CHICKEN-FAJITA",
    "Size": "M",
    "Table_No": 4
}

headers = {
    "Content-Type": "application/json",
    "Authorizations": f"Bearer {loads(token.text)['access_token']}"
}

pedido = post("https://order-pizza-api.herokuapp.com/api/orders", data=dumps(pizza), headers=headers)
print(loads(pedido.text))

cancelamento = delete(f"https://order-pizza-api.herokuapp.com/api/orders/4")
print(cancelamento.text)

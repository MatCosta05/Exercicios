from json import dump, dumps, load, loads

json_exemplo = {
    "chave1": "valor1",
    "chave2": "valor2"
}
#Conversão dicínário para string
string_json = dumps(json_exemplo)
print(string_json)

#Conversão string para dicionário
json_str2dict = loads(string_json)
print(json_str2dict)

#Salvar um arquivo usando a função dump
with open("json_exemplo.json", "w") as file:
    dump(json_str2dict, file)

#ler um arquivo json usando a função load
with open("json_exemplo.jhon") as file:
    leitura_do_json = load(file)

leitura_do_json
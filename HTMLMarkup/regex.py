from re import findall, search

texto = "Estamos estudando Pyton no curso Python Pro da mentorama"

findall("da", texto)
search("da", texto).start()

caracteres_especiais = "Estamos @ estudando #Python no curso 1 Python Pro da mentorama"
palavras = findall(r"\w+", caracteres_especiais)
print(palavras)
print(" ".join(palavras))

'''
findall(r"P.thon", texto)

padrao = r"\bpy"
texto = "python é uma linguagem pythonica e os seus arquivos possuem a extensão py"

print(findall(padrao, texto))
'''
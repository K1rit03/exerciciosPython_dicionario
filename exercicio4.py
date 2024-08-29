dicionario = {}
texto = input('Insira o texto aqui:')
vogais = 'aeiou' 

for caracter in texto:
    if caracter in vogais:
        if caracter in dicionario:
            dicionario[caracter] += 1
        else:
            [dicionario] = 1
print(dicionario)

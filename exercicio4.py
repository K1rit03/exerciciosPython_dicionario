dicionario = {'a' : 0,'e' : 0, 'o' : 0, 'u': 0}
texto = input('Insira o texto aqui:')
vogais = 'aeiou'

for caracter in texto:
    if caracter in vogais:
        dicionario[caracter] += 1 
print(dicionario)


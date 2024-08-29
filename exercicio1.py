usuario = {}
while True:
    cpf = input('CPF: ')
    if cpf == '':
        break
    nome = input('Nome: ')
    if cpf not in usuario:
        usuario[cpf] = nome
print(usuario)
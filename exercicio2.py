produto = {}
for i in range(5):
    nomeProduto = input('Insira o nome do produto:')
    if nomeProduto == '':
        break
    precoProduto = float(input('Insira o preço do produto: '))
    if precoProduto not in produto:
        produto[nomeProduto] = precoProduto
    for nome,preco in produto.items():
        if preco >50:
            print(nome)

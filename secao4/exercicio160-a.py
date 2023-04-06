from copy import deepcopy
#aumentar os preços em 10% usando deepcopy
produtos = [
    {'nome':'produto 5', 'preco': 10.00},
    {'nome':'produto 3', 'preco': 14.30},
    {'nome':'produto 4', 'preco': 20.30},
    {'nome':'produto 1', 'preco': 68.44},
    {'nome':'produto 2', 'preco': 93.80}
]
novosProdutos = deepcopy(produtos)
ordenarDictPorNome = lambda x: x["nome"]
novosProdutos.sort(key= ordenarDictPorNome)

for i in range(len(novosProdutos)):
    for x in novosProdutos[i]:
        if x == 'nome':
            novosProdutos[i][x] = novosProdutos[i][x].title()
        if x == 'preco':
            novosProdutos[i][x] += round(novosProdutos[i][x] * 0.1)
    print(novosProdutos[i])
    



from copy import deepcopy
#ordem por nome crescente usando deepcopy
produtos = [
    {'nome':'produto 5', 'preco': 10.00},
    {'nome':'produto 3', 'preco': 14.30},
    {'nome':'produto 4', 'preco': 20.30},
    {'nome':'produto 1', 'preco': 68.44},
    {'nome':'produto 2', 'preco': 93.80}
]
novosProdutos = deepcopy(produtos)

novosProdutos.sort(key=lambda x: x["nome"])

for i in range(len(novosProdutos)):
    for x in novosProdutos[i]:
        if x == 'nome':
            novosProdutos[i][x] = novosProdutos[i][x].title()
    print(novosProdutos[i])
                 


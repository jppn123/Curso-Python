import json
def ler(lista, nomeArquivo):
    dados = []
    try:
        with open(nomeArquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("deu ruim")
        salvar(lista, nomeArquivo)
    return dados

def salvar(lista, nomeArquivo):
    dados = lista
    with open(nomeArquivo, 'w', encoding="utf8") as arquivo:
        dados = json.dump(lista, arquivo)
    return dados

NOME = 'exercicio192.json'
listapdr = ler([], NOME)
ldesfaz = []
def listar(lista):
    print('\nTAREFAS:')
    for x in range(len(lista)):
        print(lista[x])
    print()

while True:
    inp = input("comandos: listar, desfazer, refazer, parar\ndigite uma tarefa ou comando: ")
    
    if inp == 'parar':
        break
    
    if inp == "listar":
        listar(listapdr)
    
    if inp not in "listar, desfazer, refazer, parar":
        listapdr.append(inp)
        listar(listapdr)
        
        
    if inp == 'desfazer':
        if listapdr == []:
            listar(listapdr)
            print("\nnão há tarefa para desfazer\n")
        else:
            ldesfaz.append(listapdr.pop())
            listar(listapdr)
    
    if inp == 'refazer':
        if ldesfaz == []:
            listar(listapdr)
            print("\nnão há tarefa para refazer\n")
        else:
            listapdr.append(ldesfaz.pop())
            listar(listapdr)
    salvar(listapdr, NOME)        
    
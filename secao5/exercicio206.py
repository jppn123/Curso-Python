import json
class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

def ler(lista, nomeArquivo):
    dados = []
    try:
        with open(nomeArquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        salvar(lista, nomeArquivo)
    return dados

def salvar(lista, nomeArquivo):
    dados = lista
    with open(nomeArquivo, 'w', encoding="utf8") as arquivo:
        dados = json.dump(lista, arquivo, indent=2)
    return dados

NOME = 'exercicio206.json'
lista_pessoas = ler([], NOME)
# for x in range(len(lista_pessoas)):
#     for chave, valor in lista_pessoas[x].items():
#         print(valor, end=' ')
#     print()
while True:

    pers = input("digite seu nome: ")
    idade = int(input('digite sua idade: '))
    control = input("deseja parar de cadastrar? [s] ou [n] ").lower()

    save = vars(pessoa(pers, idade)) #retorna um dict dos atributos da classe pessoa e atribui a save
    lista_pessoas.append(save) #append na lista pessoas
    salvar(lista_pessoas, NOME) #salva no json

    if control not in 'sn':
        print("\ninsira um valor válido entre [s] e [n]\n")
    if control == 's':
        break
import os
lista = list()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def calc(var):
    if var == "i":
        clear()
        produto = input("digite o nome do produto a ser adicionado\n").lower()
        lista.append(produto)
        print(f"produto {produto} adicionado\n")
       
    elif var == "l":
        clear()
        print("lista de produtos: ")
        if lista == []:
            print("lista vazia!\n")
        else:
            for i,x in enumerate(lista):
                print(i+1,".",x)
            print()
        
    elif var == "d":
        clear()
        try:
            for i,x in enumerate(lista):
                print(i+1,"-",x)
            print()
            delete = int(input("digite o numero do produto a ser deletado\n"))
            if lista[delete-1] in lista:
                print(f"produto {lista[delete-1]} retirado\n")
                lista.pop(delete-1)
                clear()
                
            else:
                clear()
                print("esse produto não existe na lista\n")
        except ValueError:
            print("insira um numero inteiro!")

    elif var not in 'dil1':
        clear()
        print("digite a letra correta [i], [l], [d]\n")

while True:

    atp = input("digite uma opção:\n[i]inserir produtos na lista\n[l]listar os produtos da lista\n[d]deletar produtos da lista\ndigite 1 para sair\n").lower()

    calc(atp)

    if atp == "1":
        clear()
        break


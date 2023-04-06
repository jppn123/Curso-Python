from random import randint
lista = list()
for x in range(12):
    xl = list()
    for y in range(10):
        xl.append(randint(1, 10))
    lista.append(xl)

def duplicados(lista):
    listaNums = list()
    
    primeiroDuplicado = -1
    
    for valor in lista:
        if valor in listaNums:
            primeiroDuplicado = valor
            break
        listaNums.append(valor)
        
    #listaDuplicados = list()    
    # for numeroDuplicado in lista:
    #     if lista.count(numeroDuplicado)>1:
    #         listaDuplicados.append(numeroDuplicado)
            
    return primeiroDuplicado

for x in range(len(lista)):
    print(lista[x], duplicados(lista[x]))
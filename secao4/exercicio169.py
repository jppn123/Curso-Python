lista1 = ['salvador', 'ubatuba','belo horizonte']
lista2 = ["ba", "mg","rj","sp"]

def zipper(lista1, lista2):
    indice = min(len(lista1),len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(indice)
    ]
    
print(zipper(lista1, lista2))

print(list(zip(lista1, lista2)))


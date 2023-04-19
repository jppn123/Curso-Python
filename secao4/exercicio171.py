listaA = [1,2,3,4,5,6]
listaB = [1,2,4,4]

indiceMinimo = min(len(listaA), len(listaB))

listaSoma =[
    listaA[i] + listaB[i] for i in range (indiceMinimo)
]
print(listaSoma)

# listaSoma = [
#     x + y for x,y in zip(listaA,listaB)
# ]
# print(listaSoma)

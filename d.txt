from random import randint
#044.971.170-65
#746.824.890.70
listaNums = list()
cpf = ''
listaRegressiva = list()
listaCpf = list()
primeiroDigito, segundoDigito= 0, 0

for x in range(9):
    listaNums.append(randint(0, 9))
    cpf += str(listaNums[x])

#preencher lista de 10 ate 2
for x in range(10, 1, -1):
    listaRegressiva.append(x)

for trio in cpf:
    for unidade in trio:
        listaCpf.append(int(unidade))

for x in range(len(listaRegressiva)):
    primeiroDigito+=(listaRegressiva[x] * listaCpf[x])

primeiroDigito *= 10
primeiroDigito %= 11

if primeiroDigito > 9:          
    primeiroDigito = 0

#tratando o segundo digito
listaRegressiva.insert(0, 11)
listaCpf.append(primeiroDigito)

for x in range(len(listaRegressiva)):
    segundoDigito+=(listaRegressiva[x] * listaCpf[x])

segundoDigito *= 10
segundoDigito %= 11

if segundoDigito > 9:
    segundoDigito = 0

listaCpf.pop()
cpfComplete = ''
for x in range(len(listaCpf)):
    cpfComplete += str(listaCpf[x])
    if (x+1) %3 == 0 and (x+1) != len(listaCpf):
        cpfComplete += '.'
    if x+1 == len(listaCpf):
        cpfComplete+= '-'
        cpfComplete+= str(primeiroDigito) + str(segundoDigito)
    
print(f"o cpf gerado é: {cpfComplete}")
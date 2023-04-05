def multi(*args):
    m = 1
    for x in args:
        m *= x
    return m


multiplicacao = multi(2,3,2)
print(multiplicacao)

def par_impar(valor):
    if valor % 2 == 0:
        isPar = "é par"
    else:
        isPar = "não é par"
    
    return isPar

print(par_impar(3))
print(par_impar(2))
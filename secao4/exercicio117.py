import os
def func(valor):
    def duplica():
        return valor * 2
    def triplica():
        return valor * 3
    def quadruplica():
        return valor * 4
    while True:
        
        atp = input(f"deseja duplicar[d], triplicar[t] ou quadruplicar[q] o valor[{valor}]?\n")

        if atp == 'd':
            return duplica()
        elif atp == 't':
            return triplica()
        elif atp == 'q':
            return quadruplica()

        if atp not in 'dtq':
            os.system('clear')
            print("digite apeanas [d], [t] ou [q]")

try:
    ip = int(input("digite um valor inteiro: "))
    os.system('clear')
    print(func(ip))
except ValueError:
    print("digite apenas numeros inteiros!")

# def multiplier(multiplicador):
#     def multiplicar(valor):
#         return valor * multiplicador
#     return multiplicar

# duplicar = multiplier(2)
# triplicar = multiplier(3)
# quadruplicar = multiplier(4)

# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))


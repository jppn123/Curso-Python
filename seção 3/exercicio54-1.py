try:
    num = int(input("digite um numero inteiro: "))

    if num %2 == 0:
        print('numero par')
    else:
        print('numero impar')
except ValueError:
    print("numero não inteiro!")
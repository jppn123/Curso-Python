try:
    horario = int(input("qual a hora atual?\n"))

    if horario <= 11 and horario >= 0:
        print("bom dia")
    elif horario <= 17 and horario >= 12:
        print('boa tarde')
    else:
        print('boa noite')
except ValueError:
    print("digite um inteiro")
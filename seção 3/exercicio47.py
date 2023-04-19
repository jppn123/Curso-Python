try:
    nome = input("digite seu nome: ")
    idade = int(input('digite sua idade: '))
    letters = 0
    for x in nome:
        if x == " ":
            pass
        if x != " ":
            letters+=1

    if " " in nome:
        space = 'seu nome contem espaços'
    else:
        space = 'seu nome não contem espaços'

    if nome and idade != "":
        print(f"seu nome é {nome}")
        print(f"seu nome é {nome[::-1]}")
        print(space)
        print(f"seu nome tem {letters} letras")
        print(f"a primeira letra do seu nome é {nome[0]}")
        print(f"a ultima letra do seu nome é {nome[-1]}")
    else:
        print('Desculpe, voce deixou campos vazios')
except ValueError:
    print("a idade deve ser um numero!")  
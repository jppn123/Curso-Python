nome = input("digite seu primeiro nome: ")

if " " in nome:
    print("esse não é seu primeiro nome")
    exit(1)

if len(nome) <= 4:
    print("seu nome é curto")
elif len(nome) == 5 or len(nome) == 6:
    print("seu nome é normal")
else:
    print("seu nome é muito grande")
palavra_secreta = 'testando'
contem_letra = list()
control = True
while control:
    lista_print_magico = list()
    letra = input("digite uma letra: ")
    if letra == "":
        continue
    else:
        if len(letra) > 1:
            print("digite uma letra apenas")
        
        if letra in palavra_secreta:
            if letra not in contem_letra and len(letra) == 1:
                contem_letra.append(letra)
                
            for letra in palavra_secreta:
                if letra in contem_letra:
                    lista_print_magico.append(letra)
                else:
                    lista_print_magico.append("_")
            
            for lacunas in lista_print_magico:
                print(lacunas, end="")
            print() 
            
            if "_" not in lista_print_magico:
                print("Parabens, você encontrou a palavra mágica!")
                control = False    
                
            del lista_print_magico  
        elif letra != "1":
            print("Não está contido na palavra [tecle 1 caso queira sair]")
    
    if letra == "1":
        control = False
        
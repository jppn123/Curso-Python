import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
perguntas = [
    {
        'pergunta': 'Quanto é 2+2?',
        'opções': [1,2,3,4],
        'resposta': 4
    },
    {
        'pergunta': 'Quanto é 5*5?',
        'opções': [25,55,10,15],
        'resposta': 25
    },  
    {
        'pergunta': 'Quanto é 10/2?',
        'opções': [3, 5, 7, 2],
        'resposta': 5
    } 
]
listaItens = ['a','b','c','d']
corretas = 0
for i in range(len(perguntas)):
    for key in perguntas[i]:
        if key == 'pergunta':
            clear()
            print(f'{i+1}- {perguntas[i][key]}')
            
        if key == 'opções':
            for opções in range(len(listaItens)):
                print(f'{listaItens[opções]}) {perguntas[i][key][opções]}')
            print()
        
        if key == 'resposta':
            while True:
                resp = input("digite a letra correspondente a sua resposta: ")
                
                if resp in listaItens:
                    index = listaItens.index(resp)
                    if perguntas[i][key] == perguntas[i]['opções'][index]:
                        corretas += 1
                    break
                        
                else:
                    print("\nvocê não digitou uma letra entre a,b,c,d\n")
if corretas == 3:
    print(f"\nParabéns, você acertou {corretas}/{len(perguntas)}!\n")
else:
    print(f"\nVocê acertou {corretas}/{len(perguntas)}\n")
    

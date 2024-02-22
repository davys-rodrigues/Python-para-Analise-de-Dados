import os

def conversao():
    print('Digite o Fahrenheit')
    f = float(input(''))
    c = 5/9 * (f-32)
    print(f'{f}Fahrenheits é igual a {c} Graus Celsius')


while True:
    print("""Converção de Fahrenheit em Celsius
            Gostaria de converter? 0 - Não | 1 - SIM""")
    
    selecao = int(input())

    if selecao == 1:
        os.system('clear')
        conversao()
    elif selecao == 0:
        print('Até mais!')
        break


### Usando lambda
# f = float(input())
# f
# c = lambda x: (x-32) * 5/9 
# print(c(f))
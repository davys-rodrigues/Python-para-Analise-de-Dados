import os
def calc_area():
    print('Qual a largura do retângulo?: ')
    l = float(input())
    print('Qual a altura do retângulo?: ')
    a = float(input())
    area = l * a
    print(f'A área é de {area}')

while True:
    print('''BEM VINDO!!!
            VAMOS CALCULAR A ÁREA DE UM RETÂNGULO? 
            (0- NÃO | 1- SIM)''')

    selecao = int(input())

    if selecao == 0:
        os.system('clear')
        print('OK - Até mais!')
        break
    elif selecao == 1:
        os.system('clear')
        calc_area()
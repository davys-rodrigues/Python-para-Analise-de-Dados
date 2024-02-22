import os 

print("============")
operacoes = {
    '+': 'soma',
    '-': 'subtração',
    'x': 'multiplicação',
    '/': 'divisão',
    '^': 'exponenciação'
}
while True:
    os.system('clear')
    indice = 0 
    for op, nome in operacoes.items():
        print(indice, ':', nome)
        indice+= 1
    print('')
    print('Escolha a operação desejada: ')
    op = int(input())
    op_string = list(operacoes.keys())[op]

    print('')
    print(f'{op_string} escolhida')
    print(f'Qual o primeiro valor?')
    v1 = float(input())
    print(f'Qual o segundo valor?')
    v2 = float(input())

    if op == 0:
        operacao = v1 + v2
    elif op == 1:
        operacao = v1 - v2
    elif op == 2:
        operacao = v1 * v2
    elif op == 3:
        operacao = v1 / v2
    elif op == 4:
        operacao = v1 ** v2
        
    print('')
    print(f'{v1} {op_string} {v2}, {operacao}')

    print('deseja fazer mais uma operação? (digite NAO para sair)')
    comando = input().upper().strip()
    if comando == 'NAO':
        break

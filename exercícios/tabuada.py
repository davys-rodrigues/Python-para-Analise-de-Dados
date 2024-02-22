### TABUADA DO 1 AO 10

numero = int(input('Digite o número inteiro para ver sua tabuada: '))
numero
tabuada = range(1,11)

### Loop for
for x in tabuada:
    print('---------------------')
    resultado = print(f'{numero} x {int(x)} = {numero * int(x)}')


### Tabuada em list comprehension
tab_list_comp = [print(f'{numero} x {x:2} = {x*numero}\n') for x in tabuada]
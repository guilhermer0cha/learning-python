lista = []
pares = []
ímpares = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
print(f'A lista completa é {lista}')
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
números = []
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado. Não vou adicionar...')
    r = input('Quer continuar? [S/N] ').upper()
    if r == 'N':
        break
números.sort()
print(f'Você digitou os números {números}')
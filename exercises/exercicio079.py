lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = input('Você deseja continuar? [S/N] ')
    if r in 'nN':
        break
lista.sort()
print(f'Você digitou os valores {lista}')
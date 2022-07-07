lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = input('Você deseja continuar? [S/N] ')
    if resp in 'nN':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem descrescente são {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
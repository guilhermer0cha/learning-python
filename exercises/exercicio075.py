tuplas = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))
print(f'Você digitou os valores {tuplas}')
print(f'O valor 9 apareceu {tuplas.count(9)} vezes')
contador = tuplas.count(3)
if contador == 0:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {tuplas.index(3) + 1}ª posição')
print('Os valores pares digitados foram', end=' ')
for n in tuplas:
    if n % 2 == 0:
        print(f'{n}', end=' ')


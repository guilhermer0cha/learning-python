valores = []
maior = 0
menor = 0
for n in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {n}: ')))
    if n == 0:
        maior = menor = valores[n]
    else:
        if valores[n] > maior:
            maior = valores[n]
        elif valores[n] < menor:
            menor = valores[n]
print(f'Você digitou os valores {valores}')
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print(f'\nO maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
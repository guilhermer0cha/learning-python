resposta = 'S'
media = 0
quantidade = 0
soma = 0
maior = 0
menor = 0
while resposta == 'S':
    numeros = int(input('Digite um número: '))
    quantidade += 1
    soma += numeros
    resposta = input('Você deseja continuar? [S/N] ').upper().strip()
    if quantidade == 1:
        maior = menor = numeros
    else: 
        if numeros < menor:
            menor = numeros
        if numeros > maior:
            maior = numeros
media = soma / quantidade
print(f'Você digitou {quantidade} números, e a média deles foi {media:.1f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
numero = 0
soma = 0
quantidade = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
    quantidade += 1
print(f'Você digitou {quantidade} números, e a soma deles foi {soma}.')
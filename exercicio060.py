num = int(input('Digite um número para saber seu fatorial: '))
cont = num
fatorial = 1
print(f'Calculando {num}! = ',end='')
while cont > 0:
    print(cont, end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial = fatorial * cont
    cont -= 1
print(fatorial)
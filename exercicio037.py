number = int(input('Digite um número inteiro: '))
binário = bin(number)
octal = oct(number)
hexadecimal = hex(number)
print('Escolha uma das bases para conversão:')
choice = int(input('[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL\nSua opção: '))
if choice == 1:
    print(f'{number} convertido para BINÁRIO é {binário[2:]}!')
if choice == 2:
    print(f'{number} convertido para OCTAL é {octal[2:]}!')
if choice == 3:
    print(f'{number} convertido para HEXADECIMAL é {hexadecimal[2:]}!')

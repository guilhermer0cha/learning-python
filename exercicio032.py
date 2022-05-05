ano = int(input('Digite um ANO para saber se ele é BISSEXTO ou não: '))
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('Esse é um ano BISSEXTO!')
else:
    print('Esse NÃO é um ano BISSEXTO!')
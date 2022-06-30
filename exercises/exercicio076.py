produtos = ('Computador', 800, 
            'Teclado', 40, 
            'Mouse', 35,
            'Headset', 70, 
            'Mousepad', 20, 
            'Monitor', 100)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for produto in range(0, len(produtos)):
    if produto % 2 == 0:
        print(f'{produtos[produto]:.<30}', end='')
    else:
        print(f'R${produtos[produto]:>4}')

        
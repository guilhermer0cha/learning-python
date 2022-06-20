número = int(input('Digite um número: '))
total = 0
for x in range(1, número + 1):
    if número % x == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[91m', end='')
    print('{} '.format(x), end='')
print(f'\n\033[mO número {número} foi dividido {total} vezes.')
if total == 2:
    print('E por isso ele É primo!')
else:
    print('E por isso ele NÃO É primo!')
print('=' * 23)
print('Sequência de Fibonacci')
print('=' * 23)
num = int(input('Quantos números você quer ver? '))
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end='')
contador = 3
while contador <= num:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    contador += 1
print('FIM')
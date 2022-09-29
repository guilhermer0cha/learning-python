import time

def contador(início, fim, passo):
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    if início > fim: 
        for c in range(início, fim-1, -passo):
            print(c, end=' ')
    for c in range(início, fim+1, passo):
        print(c, end=' ')
print('=' * 30)
print('Contagem de 1 até 10 de 1 em 1')
for c in range(0, 10):
    print(c+1, end=' ')
print('FIM!')
print('=' * 30)
print('Contagem de 10 até 0 de 2 em 2')
for c in range(10, -2, -2):
    print(c, end=' ')
print('FIM!')
print('=' * 30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print('=' * 30)
contador(i, f, p)
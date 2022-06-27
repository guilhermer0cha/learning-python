from random import choice


print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
número = int(input('Qual número eu pensei? '))
sorteio = [0, 1, 2, 3, 4, 5]
random = choice(sorteio)
print(f'Eu pensei em {random}!')
if número == random:
    print('Você acertou!')
else:
    print('Você não acertou.')
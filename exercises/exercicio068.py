from random import randint
print('='*31)
print('VOCÊ ESTÁ JOGANDO PAR OU ÍMPAR!')
print('='*31)
vitorias = 0
while True:
    jogada = int(input('Digite um valor: '))
    computador = randint(1, 10)
    soma = computador + jogada
    par_impar = ' '
    while par_impar not in 'PI':
        par_impar = input('Par ou Ímpar? [P/I] ').upper().strip()[0]
    print(f'O COMPUTADOR JOGOU {computador}, E VOCÊ JOGOU {jogada}. TOTAL DE {soma}')
    if par_impar == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('VOCÊ PERDEU!')
            break
    else:
        if soma % 2 == 0:
            print('VOCÊ PERDEU!')
            break
        else:
            print('VOCÊ VENCEU!')
            vitorias += 1
    print('Vamos jogar novamente...')
print(f'GAME OVER! VOCÊ VENCEU {vitorias} VEZES.')

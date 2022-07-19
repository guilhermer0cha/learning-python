import random

sorteio = []
njogos = int(input('Quantos jogos você quer que eu sorteie? '))
for j in range(1, njogos+1):
    for n in range(0, 6):
        números = random.randint(1, 60)
        if números not in sorteio:
            sorteio.append(números)
    print(f'Jogo {j}: {sorteio}')
    sorteio.clear()

    




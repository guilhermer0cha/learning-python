from random import randint
import time
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
ranking = {}
print('Números sorteados: ')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    time.sleep(.5)
print('RANKING DOS JOGADORES')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse= True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    time.sleep(.5)
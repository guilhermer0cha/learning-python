def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nomeJogador = input('Nome do Jogador: ')
númGols = input('Número de Gols: ')
if númGols.isnumeric():
    númGols = int(númGols)
else:
    númGols = 0
if nomeJogador.strip() == '':
    ficha(gols=númGols)
else:
    ficha(nomeJogador, númGols)


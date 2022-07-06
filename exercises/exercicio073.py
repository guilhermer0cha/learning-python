times = ('Palmeiras', 'Corinthians', 'Athletico-PR', 'Internacional', 
         'Atlético Mineiro', 'Fluminense', 'Santos', 'Chapecoense', 'Flamengo', 
         'Botafogo', 'Avaí', 'Bragantino', 'Atlético Goianiense', 'Goiás', 'Ceará', 
         'Coritiba', 'América-MG', 'Cuiabá', 'Juventude', 'Fortaleza')
print(f'Lista de times do Brasileirão: {times}')
print('='*100)
print(f'Os 5 primeiros colocados são {times[:5]}')
print('='*100)
print(f'Os 4 últimos colocados são {times[-4:]}')
print('='*100)
print(f'Times em ordem alfabética {sorted(times)}')
print('='*100)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}º posição')
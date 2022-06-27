print('GERADOR DE PA')
print('-=-' * 5)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
contador = 1
while contador <= 10:
    print(f'{termo} → ', end='')
    termo += razão
    contador += 1
print('FIM')

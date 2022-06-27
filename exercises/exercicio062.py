print('GERADOR DE PA')
print('-=-' * 5)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} → ', end='')
        termo += razão
        contador += 1
    print('PAUSA')
    mais = int(input('Você deseja mostrar mais quantos termos? '))
print('FIM')
print(f'Progressão finalizada com {total} termos mostrados')


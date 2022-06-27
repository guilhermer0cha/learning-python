tothomens = 0
totmulheres = 0
tot18 = 0
print('='*20)
print('CADASTRE UMA PESSOA')
print('='*20)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: ').upper().strip()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
    if sexo == 'M':
        tothomens += 1
    if sexo == 'F' and idade < 20:
        totmulheres += 1
    if idade >= 18:
        tot18 += 1
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {tothomens} homens cadastrados')
print(f'E temos {totmulheres} mulheres com menos de 20 anos')
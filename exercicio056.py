maioridadehomem = 0
nomevelho = ''
idadetotal = 0
totmulher20 = 0
for x in range(1, 5):
    print(f'{x}ª PESSOA')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    idadetotal = idadetotal + idade
    media = idadetotal / 4
    if x == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
    
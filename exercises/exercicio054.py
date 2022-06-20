from datetime import date
anoatual = date.today().year
maioridade = 0
menoridade = 0
for x in range(1, 8):
    anonascimento = int(input(f'Em que ano a {x}ª pessoa nasceu? '))
    idade = anoatual - anonascimento
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1
print(f'Ao todo tivemos {maioridade} pessoas são maiores de idade')
print(f'E também tivemos {menoridade} são menores de idade')
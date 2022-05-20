from datetime import date
nascimento = int(input('Ano de nascimento: '))
idade_atual = date.today().year - nascimento
print(f'O atleta tem {idade_atual} anos.')
if idade_atual <= 9:
    print('Classificação: MIRIM')
elif idade_atual <= 14:
    print('Classificação: INFANTIL')
elif idade_atual <= 19:
    print('Classificação: JUNIOR')
elif idade_atual <= 25:
    print('Classificação: SÊNIOR')  
else:
    print('Classificação: MASTER')

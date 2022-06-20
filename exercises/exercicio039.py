ano = int(input('Ano de nascimento: '))
print(f'Quem nasceu em {ano} tem {2022 - ano} anos em 2022.')
if (2022 - ano) > 18:
    print(f'Você ja deveria ter se alistado há {(2022 - ano) - 18} anos.')
    print(f'Seu alistamento foi em {2022 - ((2022 - ano) - 18)}.')
if (2022 - ano) == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Ainda não está na hora de você se alistar.')
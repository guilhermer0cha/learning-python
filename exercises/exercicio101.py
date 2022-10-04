def voto(ano):
    idade = 2022 - anoNascimento
    if idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    else:
        if idade == 16 or idade == 17:
            print(f'Com {idade} anos: VOTO OPCIONAL.')
        else:
            print(f'Com {idade} anos: NÃO VOTA.')


anoNascimento = int(input('Em que ano você nasceu? '))
voto(anoNascimento)
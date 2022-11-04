def aumentar(p = 0, porcentagem = 0, format = False):
    resultado = p + (p * porcentagem / 100)
    return resultado if format is False else moeda(resultado)


def diminuir(p = 0, porcentagem = 0, format = False):
    resultado = p - (p * porcentagem / 100)
    return resultado if format is False else moeda(resultado)                         #


def dobro(p = 0, format = False):
    resultado = p * 2
    return resultado if format is False else moeda(resultado)


def metade(p = 0, format = False):
    resultado = p / 2
    return resultado if format is False else moeda(resultado)


def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')


def resumo(p = 0, taxaa = 8, taxar = 14):
    print('-' * 30)
    print('RESUMO'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{taxaa}% de aumento: \t\t{aumentar(p, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(p, taxar, True)}')
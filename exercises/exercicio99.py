from time import sleep


def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('\nAnalisando...')
    for valor in núm:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
maior(2, 9, 4, 5, 6, 1)
maior(2)
maior()
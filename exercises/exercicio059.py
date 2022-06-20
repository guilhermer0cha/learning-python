n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
escolha = 0
while escolha != 5:
    print('''Operações possíveis:
[ 1 ] SOMAR
[ 2 ] MULTIPLICADOR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
    escolha = int(input('Digite a operação de sua preferência: '))
    if escolha == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}')
    elif escolha == 2:
        print(f'O número {n1} x {n2} é {n1*n2}')
    elif escolha == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior é {n1}')
        else:
            print(f'Entre {n1} e {n2} o maior é {n2} ')
    elif escolha == 4:
        print('Informe os números novamente')
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
    elif escolha == 5:
        print('Fim')
    else:
        print('Opção inválida. Tente novamente')    


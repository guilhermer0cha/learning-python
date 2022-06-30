palavras = ('chutei', 'balde', 'cavalona',
            'tragada', 'derruba', 'mandela',
            'arana', 'saudade', 'baroni',
            'montagem', 'paraisopolis')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'AEIOUaeiou':
            print(f'{letra} ', end='')



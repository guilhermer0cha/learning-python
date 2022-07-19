boletim = []
contador = 0
while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    média = (nota1 + nota2) / 2
    resp = str(input('Quer continuar? [S/N] '))
    boletim.append([nome, [nota1, nota2], média])
    if resp in 'nN':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for a, p in enumerate(boletim):
    print(f'{a:<4}{p[0]:<10}{p[2]:>8}')

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
print(f'Tirando {nota1} e {nota2}, a média do aluno é {(nota1 + nota2) / 2}.')
if (nota1 + nota2) / 2 < 5:
    print('O aluno foi REPROVADO.')
if (nota1 + nota2) / 2 > 5 and (nota1 + nota2) / 2 < 6.9:
    print('O aluno está em RECUPERAÇÃO.')
if (nota1 + nota2) / 2 > 6.9:
    print('O aluno PASSOU.')
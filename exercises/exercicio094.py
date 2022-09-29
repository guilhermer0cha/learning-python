pessoa = {}
pessoas = []
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: ').upper()[0]
        if pessoa['sexo'] not in 'FM':
            print('ERRO! Por favor digite apenas M ou F.')
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor digite apenas S ou N.')
    if resp == 'N':
        break
print(f'A) Ao todos temos {len(pessoas)} pessoas cadastradas.')
média = soma / len(pessoas)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram:', end=' ')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= média:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
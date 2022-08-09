from datetime import datetime
dicionário = {}
dicionário['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dicionário['idade'] = datetime.now().year - nascimento
dicionário['ctps'] = int(input('Carteira de Trabalho (0 se não tem): '))
if dicionário["ctps"] != 0:
    dicionário['contratação'] = int(input('Ano de Contratação: '))
    dicionário['salário'] = float(input('Salário: R$'))
    dicionário['aposentadoria'] = dicionário['idade'] + ((dicionário['contratação'] + 35) - datetime.now().year)
for k, v in dicionário.items():
    print(f'{k} tem o valor {v}')

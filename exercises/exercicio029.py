velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade e foi multado!')
    print(f'O valor da multa será de R${(velocidade - 80) * 7:.2f}.')
else:
    print('Você está dentro do limite de velocidade!')
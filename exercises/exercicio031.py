distância = float(input('Digite a distância da viagem em Km: '))
if distância < 200:
    print(f'O valor da passagem será de R${distância*0.5:.2f}!')
else:
    print(f'O valor da passagem será de R${distância*0.45:.2f}!')
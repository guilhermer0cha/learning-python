valor_casa = float(input('Digite o valor da casa que deseja comprar: '))
salário = float(input('Digite o seu salário: '))
anos = float(input('Digite em quantos anos você deseja pagar a casa: '))
prestação = valor_casa / (anos * 12)
valor_mínimo = salário * 0.3
if prestação > valor_mínimo:
    print('Você não pode comprar essa casa!')
else:
    print('O empréstimo foi aceito!')
    print(f'Você pagará {anos * 12} parcelas de R${prestação}!')
   
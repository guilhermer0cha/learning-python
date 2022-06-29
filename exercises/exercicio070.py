total = 0
totmil = 0
menor = 0
cont = 0
barato = ' '
while True:
    produto = input('Nome do Produtos: ')
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]').strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais que R$1000')
print(f'O produto mais brato foi {barato}, que custa R${menor:.2f}')
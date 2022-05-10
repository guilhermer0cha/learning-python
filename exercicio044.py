print('{:=^40}'.format(' LOJA DO BREAD '))
valor = float(input('Preço das compras: R$'))
print('''Formas de pagameno
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
parcelas = int(input('Quantas parcelas: '))
if opção == 1:
    print(f'O valor das compras com desconto será de: R${valor - (valor * 0.1)}')
elif opção == 2:
    print(f'O valor das compras com desconto será de: R${valor - (valor * 0.05)}')
elif opção == 3:
    print(f'Sua compra de {valor} será parcelada em {parcelas}x de R${valor / parcelas:.2f} COM JUROS!')
    print(f'O valor das compras com desconto será de: R${valor - (valor * 0.05)}')
elif opção == 4:
    print(f'Sua compra de {valor} será parcelada em {parcelas}x de R${valor / parcelas:.2f} COM JUROS!')
    print(f'O valor das compras com desconto será de: R${valor + (valor * 0.2)}')
    
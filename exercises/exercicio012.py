valor = float(input('Digite o preço do produto: '))
valor_desconto = valor - (valor * 0.05)
print(f'O valor do produto era de R${valor:.2f}, e com o desconto de 5% ficou R${valor_desconto:.2f}.')

km_percorridos = float(input('Digite quantos Km foram percorridos com o carro: '))
dias_alugados = int(input('Digite quantos dias o carro foi alugado: '))
valor_total = (dias_alugados * 60) + (km_percorridos * 0.15)
print(f'O preço total do aluguel do carro será de {valor_total}.')
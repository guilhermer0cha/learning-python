cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hi = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print(f'A hipotenusa  vai medir {hi:.2f}.')
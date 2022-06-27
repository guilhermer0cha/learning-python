side1 = float(input('Digite o valor do primeiro lado do triângulo: '))
side2 = float(input('Digite o valor do segundo lado do triângulo: '))
side3 = float(input('Digite o valor do terceiro lado do triângulo: '))
if (side1 + side2 < side3) or (side1 + side3 < side2) or (side2 + side3 < side1):
    print('Não é possível formar um triângulo!')
else:
    print('É possível formar um triângulo!')
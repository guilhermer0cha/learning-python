side1 = float(input('Primeiro lado: '))
side2 = float(input('Segundo lado: '))
side3 = float(input('Terceiro lado: '))
if side1 == side2 and side2 == side3:
    print('EQUILÁTERO!')
elif side1 == side2 or side1 == side3 or side2 == side3:
    print('ISÓSCELES!')
elif (side1 + side2 < side3) or (side1 + side3 < side2) or (side2 + side3 < side1):
    print('Não é possível formar um triângulo!')
else:
    print('ESCALENO!')

peso = float(input('Informe um peso (Kg): '))
altura = float(input('Informe uma altura (m): '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Pouca sombra.')
elif imc > 18.5 and imc < 24.9:
    print('Normal.')
elif imc >= 25 and imc < 29.9:
    print('Sobrepeso.')
elif imc >= 30 and imc < 39.9:
    print('Obesidade.')
else:
    print('Wellington.')

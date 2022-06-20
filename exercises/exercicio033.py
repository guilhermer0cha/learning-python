number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
number3 = int(input('Digite o terceiro número: '))
minor = number1
if number2 < number1 and number2 < number3: 
    minor = number2
if number3 < number1 and number3 < number2:
    minor = number3
print(f'O menor valor digitado foi {minor}!')
# Verificando o maior
major = number1
if number2 > number1 and number2 > number3:
    major = number2
if number3 > number1 and number3 > number2:
    major = number3
print(f'O maior valor digitado foi {major}!')
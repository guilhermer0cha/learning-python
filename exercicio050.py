s = 0
for x in range(1, 7):
    number = int(input('Digite um número: '))
    if (number % 2) == 0:
        s = s + number
print(f'A soma dos números é {s}!')
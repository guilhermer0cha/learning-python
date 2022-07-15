nums = [[], []]
for c in range(1, 8):
    valores = (int(input(f'Digite o {c}º número: ')))
    if valores % 2 == 0:
        nums[0].append(valores)
        nums[0].sort()
    elif valores % 2 == 1:
        nums[1].append(valores)
        nums[1].sort()
print(f'Os valores pares digitados foram: {nums[0]}')
print(f'Os valores ímpares digitados foram: {nums[1]}')
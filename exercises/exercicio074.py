# from random import randint
# maior = 0
# menor = 10
# print(f'Os números sorteados foram: ', end='')
# for c in range (0, 5):
#     sorteio = randint(1,10)
#     print(f'{sorteio} ', end='')
#     if sorteio < menor:
#         menor = sorteio
#     elif sorteio > maior:
#         maior = sorteio
# print(f'\nO maior valor sorteado foi {maior}')
# print(f'O menor valor sorteado foi {menor}')
from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), 
           randint(1,10), randint(1,10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

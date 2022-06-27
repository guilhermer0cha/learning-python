from random import randint
palpite = int(input('Digite seu palpite: '))
tentativas = 1
sorteado = randint(0, 10)
while palpite != sorteado:
    palpite = int(input('Palpite errado. Tente novamente: '))
    tentativas += 1
print(f'Eu pensei no número {sorteado}!')
print(f'Você acertou na {tentativas}ª tentativa!')

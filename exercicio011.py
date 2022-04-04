largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
área = altura * largura
tinta = área / 2
print(f'A parade tem a dimensão de {largura}x{altura} e sua área é de {área}m², e para pintar essa parede será necessário {tinta:.2f}l de tinta.')
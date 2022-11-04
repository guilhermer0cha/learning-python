import sys

sys.path.append('..')
from utilidadescev.moeda import resumo
preço = float(input('Digite o preço: R$'))
resumo(preço)
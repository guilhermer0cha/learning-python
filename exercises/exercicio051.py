first_term = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
dez = first_term + (10 - 1) * reason
for x in range(first_term, dez + reason, reason):
    print('{} '.format(x), end=' → ')
print('ACABOU!')
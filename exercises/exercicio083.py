expressão = str(input('Digite a expressão: '))
pilha = []
for símbolo in expressão:
    if símbolo == '(':
        pilha.appned('(')
    elif símbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
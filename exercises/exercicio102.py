def fatorial(número, show=False):
    """
    -> Calcula o Fatorial de um número.
    : "número": O número a ser calculado.
    : "show": (opcional) Mostrar ou não a conta.
    : "return": O valor do Fatorial de um número.
    """
    fatorial = 1
    for c in range(número, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        fatorial *= c
    return fatorial

print(fatorial(5, show=True))
help(fatorial)
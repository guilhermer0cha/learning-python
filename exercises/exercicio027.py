nome = str(input('Digite o seu nome: ')).strip()
separado = nome.split(" ")
print(f'O primeiro nome é: {separado[0]}.')
print(f'O último nome é: {separado[-1]}')
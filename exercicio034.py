salary = float(input('Digite o seu salário: '))
if salary > 1250:
    print(f'Seu novo salário é de R${(salary*0.10) + salary:.2f}.')
if salary <= 1250:
    print(f'Seu novo salário é de R${(salary*0.15) + salary:.2f}.')

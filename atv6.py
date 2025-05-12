# Faça um programa que solicite o salário de um funcionário e calcule o aumento. Se o salário for maior que R$2000, o aumento é de 12,5%; caso contrário, o aumento é de 17,75%.
print('Digite o salário do funcionario: ')
salario = float(input('salario: '))

if salario > 2000:
    aumento = salario * 0.125
    novo_salario = salario + aumento
    print('O novo salário é:', novo_salario)

else:
    aumento = salario * 0.1775
    novo_salario = salario + aumento
    print('O nov salário é:', novo_salario)
    
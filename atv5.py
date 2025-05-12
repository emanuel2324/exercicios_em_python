# Crie um programa que peça dois números ao usuário e qual das quatro operações básicas (soma, subtração, multiplicação e divisão) deseja.
print('Digite um número')
n1 = int(input('n1: '))

print('Digite outro número')
n2 = int(input('n2: '))
print('Escolha uma operação:')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
op = int(input('Escolha a operação: '))
if op == 1:
    result = n1 + n2
    print('A soma de', n1, 'e', n2, 'é:', result)

elif op == 2:
    result = n1 - n2
    print('A sutração de', n1, 'e',n2, 'é:', result)
elif op == 3:
    result = n1 * n2
    print('A multiplicação de', n1, 'e', n2, 'é:', result)
elif op == 4:
    if n2 == 0:
        print('Divisão por zero não é permitida')
    else:
        result = n1 / n2
        print('A divisão de', n1, 'e', n2, 'é:', result)
else:
    print('Operação inválida')
    
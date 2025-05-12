#Escreva um programa que peça um número ao usuário e calcule o seu fatorial.
print('Digite um número')
n = int(input('n:'))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
    print('O fatorial de', n, 'é:', fatorial)

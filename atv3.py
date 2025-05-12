# Crie um programa que peça dois números e mostre qual deles é o maior
print('Digite um número')
n1 = int(input('n1: '))
print('Digite outro número')
n2 = int(input('n2: '))

if n1 >n2:
    print('o maior número é:', n1)
elif n2 > n1:
    print('o maior número é:', n2)
else:
    print('os números são iguais')
    

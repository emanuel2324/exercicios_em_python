# Escreva um programa que peça três notas de um aluno e calcule a média.
# Em seguida, diga se o aluno foi aprovado (média >= 7), ficou em recuperação
# (média entre 5 e 6.9) ou foi reprovado (média < 5).
 
print('Digite a primeira nota')
n1 = float(input('n1: '))

print('Digite a segunda nota')
n2 = float(input('n2: '))

print('Digite a terceira nota')
n3 = float(input('n3: '))
media = (n1 + n2 + n3) / 3 
print('A média é:', media)
if media >= 7:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')

           
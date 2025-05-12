# Crie um programa que peça um número e imprima todos os números pares
# de 0 até esse número (inclusive).

# Solicita um número ao usuário
numero = int(input("Digite um número: "))

# Imprime os números pares de 0 até o número informado
print(f"Números pares de 0 até {numero}:")
for i in range(0, numero + 1, 2):
    print(i)

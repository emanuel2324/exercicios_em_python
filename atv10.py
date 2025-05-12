# Faça um programa que peça um número e calcule a soma de todos os
# números ímpares de 1 até esse número (inclusive).

numero = int(input("Digite um número: "))

soma_impares = 0

for i in range(1, numero + 1):
    if i % 2 != 0:
        soma_impares += i

print(f"A soma dos números ímpares de 1 até {numero} é: {soma_impares}")

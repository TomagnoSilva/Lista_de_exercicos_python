"""
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

O produto do dobro do primeiro com metade do segundo .
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo.
"""

# Solicitando os dados ao usuário
int_1 = int(input("Digite um número inteiro: "))
int_2 = int(input("Digite outro número inteiro: "))
real = float(input("Digite um número real: "))

# Realizando os cálculos
# 1. O produto do dobro do primeiro com metade do segundo
resutado1 = (int_1 * 2) * (int_2 / 2)

# 2. A soma do triplo do primeiro com o terceiro
resutado2 = (int_1 * 3) + real

# 3. O terceiro elevado ao cubo
resutado3 = real ** 3

# Exibindo os resultado ao usuário
print("\n--- Resultados ---")
print(f"O produto do dobro do primeiro com metade do seundo: {resutado1}")
print(f"A soma do triplo do primeiro com o terceiro: {resutado2}")
print(f"O terceiro elevado ao cubo: {resutado3:.2f}")

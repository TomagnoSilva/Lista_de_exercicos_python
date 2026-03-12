"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

import math

# Entrada de dados do usuários
area = float(input("Digite o tamanho da área a ser pintada (m²): "))

# Premissas do problema
cobertura_por_litro = 3
capacidade_lata = 18
preco_lata = 80.00

# 1. Calcular a quantidade de litros necessária
litros_necessarios = area / cobertura_por_litro
# 2. Calcular a quantidade de latas (arredondando para cima)
quantidade_latas = math.ceil(litros_necessarios / capacidade_lata)
# 3. Calcular o custo total
custo_total = quantidade_latas * preco_lata

# Exibição dos resultados
print("-" * 25)
print(f"Quantidade de latas: {quantidade_latas}")
print(f"Preço total: R$ {custo_total:.2f}")
print("-" * 25)

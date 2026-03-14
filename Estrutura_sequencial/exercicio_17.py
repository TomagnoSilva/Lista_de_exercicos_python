"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

- Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga
e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

import math


# Entrada de dados
area = float(input("Digite o tamanho da área a ser pintada (m²): "))

# Cálculos base
# 1 litro para cada 6 metros quadrados
litros_necessarios = area / 6

# Adição de 10% de folga (apenas para a terceira situação, mas aplicada aqui para precisão)
litros_com_folga = litros_necessarios * 1.1

# Configurações de venda
LATA_LITROS = 18
LATA_PRECO = 80.00
GALAO_LITROS = 3.6
GALAO_PRECO = 25.00

# --- SITUAÇÃO 1: Apenas Latas de 18L ---
quantidade_latas = math.ceil(litros_necessarios / LATA_LITROS)
preco_latas = quantidade_latas * LATA_PRECO

# --- SITUAÇÃO 2: Apenas Galões de 3,6L ---
quantidade_galoes = math.ceil(litros_necessarios / GALAO_LITROS)
preco_galoes = quantidade_galoes * GALAO_PRECO

# --- SITUAÇÃO 3: Mistura Otimizada (com 10% de folga) ---
# 1. Calculamos quantas latas inteiras cabem no total com folga
latas_mistas = int(litros_com_folga // LATA_LITROS)

# 2. O que sobrar das latas, calculamos em galões
litros_restantes = litros_com_folga % LATA_LITROS
galoes_mistos = math.ceil(litros_restantes / GALAO_LITROS)

# Verificação de segurança: 
# Se o preço dos galões for maior que o preço de uma lata inteira,
# compensa comprar mais uma lata e zero galões.
if (galoes_mistos * GALAO_PRECO) > LATA_PRECO:
    latas_mistas += 1
    galoes_mistos = 0

# 3. Preço total da mistura
preco_misto = (latas_mistas * LATA_PRECO) + (galoes_mistos * GALAO_PRECO)

# Exibição dos resultados
print("-" * 46)
print(f"Área a pintar: {area:.2f} m²")
print(f"Litros necessários (com 10% de folga): {litros_com_folga:.2f} L")
print("-" * 46)

print(f"1) Comprar apenas latas de 18L:")
print(f"   Quantidade: {quantidade_latas}")
print(f"   Preço total: R$ {preco_latas:.2f}")

print(f"\n2) Comprar apenas galões de 3,6L:")
print(f"   Quantidade: {quantidade_galoes}")
print(f"   Preço total: R$ {preco_galoes:.2f}")

print(f"\n3) Mistura de latas e galões (Otimizado):")
print(f"   Latas: {latas_mistas}")
print(f"   Galões: {galoes_mistos}")
print(f"   Preço total: R$ {preco_misto:.2f}")

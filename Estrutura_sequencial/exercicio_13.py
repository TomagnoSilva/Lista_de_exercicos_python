"""
Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo
que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

Para Megabytes: Gigabytes * 1024
Para Kilobytes: Gigabytes * 1024 * 1024
Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.
"""

# Passo 1: Entrada de dados
# O usuário informa o tamanho em Gigabytes (ex: 1.5)
tamanho_gb = float(input("Digite o tamanho do arquivo em GBs: "))

# Passo 2: Cálculos de conversão
# Convertendo para Megabytes (1 degrau abaixo)
tamanho_mb = tamanho_gb * 1024

# Convertendo para Kilobytes (2 degraus abaixo)
tamanho_kb = tamanho_gb * 1024 * 1024

# Passo 3: Exibição dos resultados
print(f"\n--- Resultado da Converção ---")
print(f"O tamanho em Megabytes é {tamanho_mb:.2f}MBs, e o tamanho em Kilobytes é {tamanho_kb:.2f}KBs ")
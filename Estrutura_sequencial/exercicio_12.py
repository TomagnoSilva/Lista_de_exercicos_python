"""
Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:
Formula: Gigabytes * 1024
"""
# 1 KB (Kilobyte) = 1024 Bytes
# 1 MB (Megabyte) = 1024 KB
# 1 GB (Gigabyte) = 1024 MB

# Entrada de dados (Tamanho em Gigabytes)
tamanho_gb = float(input("Digite o tamanho do arquivo em GBs: "))

# O cálculo de conversão 1 GB possui 1024 Megabytes
tamanho_mb = tamanho_gb * 1024

# Exibição do resultado
print(f"\n--- Resultado da Converção ---")
print(f"{tamanho_gb} GB equivale a {tamanho_mb:.2f} MB.")

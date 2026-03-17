"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e
a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).
"""

# Solicita o tamanho do arquivo em MB
tamanho_arquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))

# Solicita a velocidade do link em Mbps
velocidade_link = float(input("Digite a velocidade do link de Internet (em Mbps): "))

# Calcula o tempo de download em segundos
tempo_segundos = (tamanho_arquivo * 8) / velocidade_link

# Converte para minutos
tempo_minutos = tempo_segundos / 60

# Informa o tempo aproximado
print(f"O tempo aproximado de download é de {tempo_minutos:.2f} minutos.")

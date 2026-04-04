"""
Faça um programa que leia três números e mostre o maior deles:
"""

# Passo 1: Solicita três números do usuário
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o terceiro número: "))

maior = numero_1 # Assume que o primeiro número é o maior inicialmente

# Passo 2: Compara o segundo número com o maior atual
if numero_2 > maior:
    maior = numero_2

# Passo 3: Compara o terceiro número com o maior atual
if numero_3 > maior:
    maior = numero_3
    
# Passo 4: Exibe o maior número encontrado
print(f"O maior número é: {maior}")

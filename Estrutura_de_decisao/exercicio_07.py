"""
Faça um programa que leia três números e mostre o maior e o menor deles:
"""

# Passo 1: Solicita três números do usuário
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o terceiro número: "))

maior = numero_1 # Assume que o primeiro número é o maior inicialmente
menor = numero_1 # Assume que o primeiro número é o menor inicialmente

# Passo 2: Compara o segundo número com o maior e menor atuais
if numero_2 > maior:
    maior = numero_2
if numero_2 < menor:
    menor = numero_2

# Passo 3: Compara o terceiro número com o maior e menor atuais
if numero_3 > maior:
    maior = numero_3
if numero_3 < menor:
    menor = numero_3
    
# Passo 4: Exibe o maior e o menor número encontrados
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

"""
Faça um programa que leia três números e mostre-os em ordem decrescente:
"""
# Solicitar ao usuário que digite três números
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o terceiro número: "))

# Criar uma lista com os números e ordená-la em ordem decrescente
numeros = [numero_1, numero_2, numero_3]

# Ordenar a lista em ordem decrescente
numeros.sort(reverse=True)

# Imprimir os números em ordem decrescente
print("Os números em ordem decrescente são:")

# Iterar sobre a lista ordenada e imprimir cada número
for numero in numeros:
    print(numero)

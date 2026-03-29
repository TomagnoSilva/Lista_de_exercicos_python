"""
Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

# Passo 1: Solicita um valor do usuário
numero = float(input("Digite um número: "))

# Passo 2: Verifica se o número é positivo e exibe a mensagem correspondente
if numero > 0:
    print(f"O valor {numero} é positivo.")
# Passo 3: Verifica se o número é negativo ou zero e exibe a mensagem correspondente
elif numero < 0:
    print(f"O valor {numero} é negativo.")
# Passo 4: Se o número for zero, exibe a mensagem correspondente
else:
    print(f"O valor {numero} é zero (neutro).")

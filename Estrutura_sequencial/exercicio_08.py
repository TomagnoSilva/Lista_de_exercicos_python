"""
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

# Perguntando os valores ao usuário
valor_hora = float(input("Quanto você ganha por hora: "))
horas_mes = float(input("Quantas horas trabalhou esse mês: "))

# Calculando o salário total
salario = valor_hora * horas_mes

# Exibindo o resultado formatado
print(f"O salário deste mês será: {salario:.2f}")




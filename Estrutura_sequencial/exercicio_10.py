"""
Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
formula: F = (C * 9/5) + 32
"""

# Solicita a temperatura em Celsius ao usuário
c_temp = float(input("Digite a temperatura em celsius: "))

# Aplica a fórmula de conversão
f_temp = (c_temp * 9 / 5) + 32

# Exibe o resultado formatado com duas casas decimais
print(f"{c_temp}°C em Fahrenheit é: {f_temp:.2f}°F")
"""
Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
formula: C = 5 * ((F-32) / 9).
"""

# Solicita a temperatura em Fahrenheit ao usuário
f_temp = float(input("Digite a temperatura em Fahrenheit: "))

# Aplica a fórmula de conversão
c_temp = 5 * ((f_temp - 32) / 9)

# Exibe o resultado formatado com duas casas decimais
print(f'{f_temp}°F em celsius é: {c_temp:.2f}°C')

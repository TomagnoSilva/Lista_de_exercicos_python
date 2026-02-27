"""
Faça um programa que peça as 4 notas bimestrais e mostre a média.
"""

# Solicita as notas ao usuário
# Ultizar float() para permitir números decimais (ex: 7.9)
nota_1 = float(input("Digite a nota 1° bimestre: "))
nota_2 = float(input("Digite a nota 2° bimestre: "))
nota_3 = float(input("Digite a nota 3° bimestre: "))
nota_4 = float(input("Digite a nota 4° bimestre: "))

# Calcula a média aritmética
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# Exibe o resultado formatado com duas casas decimais
print(f"\nA média final das notas é: {media:.2f}")

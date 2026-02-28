"""
Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""
# Passo 1: Solicita a medida do lado do quadrado
lado = float(input("Entre com a medida do lado: "))

# Passo 2: Calcula a área (Lado * Lado)
area = lado ** 2

# Passo 3: Calcula o dobro da área
dobro_area = area * 2

# Passo 4: Exibe os resultados para o usuário
print(f"A área de um quadrado de lado {lado} é: {area}")
print(f"O dobro da área é: {dobro_area}")

# Foi Importada essa biblioteca para usar o valor de 'r' com alta precisão (math.pi).
import math

# É Solicitado o raio ao usuário
raio = float(input("Entre com o raio: "))

# Calcula a área usando a constante pi da biblioteca math
area = (raio ** 2) * math.pi

# Exibe o resultado com duas casas decimais
print(f"A área de círculo com ario {raio} é: {area:.2f}")

"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um
programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:

salários até R$ 1300,00 (incluindo) : aumento de 20%
salários entre R$ 1300,00 e R$ 1800,00 : aumento de 15%
salários entre R$ 1800,00 e R$ 2500,00 : aumento de 10%
salários de R$ 2500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

# Solicitar ao usuário que digite o salário do colaborador
salario = float(input("Digite o salário do colaborador: R$ "))

# Verificar o salário e calcular o reajuste
if salario <= 1300.00:
    percentual_aumento = 20
elif salario <= 1800.00:
    percentual_aumento = 15
elif salario <= 2500.00:
    percentual_aumento = 10
else:
    percentual_aumento = 5

# Calcular o valor do aumento com base no percentual
valor_aumento = salario * (percentual_aumento / 100) 

# Calcular o novo salário após o aumento
novo_salario = salario + valor_aumento 

# Imprimir as informações sobre o reajuste
print("\n--- Resultado do Reajuste Tabajara ---")
print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")
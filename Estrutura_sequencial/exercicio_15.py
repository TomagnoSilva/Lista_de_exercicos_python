"""
Faça um programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

# Solicita os dados ao usuário
valor_hora = float(input("Quanto você ganha por hora? R$ "))
horas_mes = float(input("Números de horas trabalhadas no mês: "))

# Cálculo do salário bruto
salario_bruto = valor_hora * horas_mes

# Cálculo dos descontos
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
total_descontos = ir + inss + sindicato

# Cálculo do salário líquido
salario_liquido = salario_bruto - total_descontos

# Exibição dos resultados formatados
print("\n" + "=" * 33)
print(f"+ Salário Bruto   : R$ {salario_bruto:10.2f}")
print(f"- IR (11%)        : R$ {ir:10.2f}")
print(f"- INSS (8%)       : R$ {inss:10.2f}")
print(f"- Sindicato (5%)  : R$ {sindicato:10.2f}")
print("-" * 33)
print(f"= Salário Líquido : R$ {salario_liquido:10.2f}")
print("=" * 33)

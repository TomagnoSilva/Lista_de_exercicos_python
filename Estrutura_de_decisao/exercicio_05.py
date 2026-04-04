"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado com Distinção", se a média for igual a dez.
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
"""

# Passo 1: Solicita as duas notas do usuário
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

# Passo 2: Calcula a média das notas
media = (nota_1 + nota_2) / 2

# Passo 3: Verifica se a média é igual a 10 e exibe a mensagem correspondente
if media == 10:
    print(f"Média: {media:.2f} - Aprovado com Distinção")

# Passo 4: Verifica se a média é maior ou igual a 7 e exibe a mensagem correspondente
elif media >= 7:
    print(f"Média: {media:.2f} - Aprovado")

# Passo 5: Se a média for menor do que 7, exibe a mensagem de reprovado
else:
    print(f"Média: {media:.2f} - Reprovado")

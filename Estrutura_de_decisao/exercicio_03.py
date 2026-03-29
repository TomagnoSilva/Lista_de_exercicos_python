"""
Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
"""

# Passo 1: Solicita uma letra do usuário
letra = input("Digite uma letra (F para Feminino, M para Masculino): ").upper() # Converte a letra para maiúscula para facilitar a comparação

# Passo 2: Verifica se a letra é "F" ou "M" e exibe a mensagem correspondente
if letra == "F":
    print(f"{letra} - Sexo Feminino")
# Passo 3: Verifica se a letra é "M" e exibe a mensagem correspondente
elif letra == "M":
    print(f"{letra} - Sexo Masculino")
# Passo 4: Se a letra for diferente de "F" ou "M", exibe uma mensagem de erro
else:
    print(f"{letra} - Letra inválida. Por favor, digite 'F' para Feminino ou 'M' para Masculino.")

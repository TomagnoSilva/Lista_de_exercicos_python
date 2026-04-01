"""
Faça um programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = input("Digite uma letra: ").lower() # Converte a letra para minúscula para facilitar a comparação

if len(letra) != 1: # Verifica se o usuário digitou mais de uma letra
    print("Por favor, digite apenas uma letra.")
elif letra in "aeiou": # Verifica se a letra é uma vogal
    print(f"{letra} - Vogal")
elif letra.isalpha(): # Verifica se a letra é uma consoante (ou seja, é uma letra do alfabeto, mas não é uma vogal)
    print(f"{letra} - Consoante")
else:
    print(f"{letra} - Não é uma letra do alfabeto")

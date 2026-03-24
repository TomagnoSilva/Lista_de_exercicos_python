"""
Faça um programa que peça dois números e imprima o maior deles.
"""

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

if numero_1 > numero_2:
    print(f"O número {numero_1} é o maior!")
elif numero_1 < numero_2:
    print(f"O número {numero_2} é o maior!")

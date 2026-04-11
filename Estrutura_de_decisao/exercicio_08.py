"""
Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato:
"""

# Passo 1: Solicita os preços dos três produtos do usuário
preco_1 = float(input("Digite o preço do primeiro produto: "))
preco_2 = float(input("Digite o preço do segundo produto: "))
preco_3 = float(input("Digite o preço do terceiro produto: "))

# Passo 2: Assume que o primeiro produto é o mais barato inicialmente
mais_barato = preco_1
item_mais_barato = "primeiro produto"

# Passo 3: Compara o segundo produto com o mais barato atual
if preco_2 < mais_barato:
    mais_barato = preco_2
    item_mais_barato = "segundo produto"

# Passo 4: Compara o terceiro produto com o mais barato atual
if preco_3 < mais_barato:
    mais_barato = preco_3
    item_mais_barato = "terceiro produto"

# Passo 5: Exibe qual produto é o mais barato e seu preço
print(f"O {item_mais_barato} é o mais barato e custa: R${mais_barato:.2f}")

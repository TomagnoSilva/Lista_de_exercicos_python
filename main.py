nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
data_atual = "23/2/2026"

indice_massa_corporal = peso / (altura ** 2)

print(f"O {nome} tem {idade} anos e seu IMC é {indice_massa_corporal}")
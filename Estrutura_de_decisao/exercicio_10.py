"""
Faça um programa que pergunte em que turno você estuda. Peça para digitar:

M - Matutino
V - Vespertino
N - Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

# Solicitar ao usuário que digite o turno em que estuda
turno = input("Em que turno você estuda? (M - Matutino, V - Vespertino, N - Noturno): ").upper().strip() # Converter a entrada para maiúscula e remover espaços em branco

# Verificar o turno e imprimir a mensagem correspondente
if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")

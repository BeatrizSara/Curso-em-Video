""" 
Aluguel de carros
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e 0,15 por km rodado.
"""

distancia = float(input("Quantos Km rodados? "))
dias_aluguel = int(input("Quantos dias alugados? "))

total_distancia = distancia * 0.15
total_alugado = dias_aluguel * 60
valor_total = total_distancia + total_alugado

print(f"O valor a pagar é de R$ {valor_total:.2f}")
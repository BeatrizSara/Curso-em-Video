""" 
Desafio 06
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere: US: $ 1,00 = 4,91 (Atualizado*)
"""
carteira = float(input("Quanto de dinheiro tem guardado na carteira: "))

reais = 4.91

compraDolares = carteira / reais

print(f"Com o valor de R$ {carteira:.2f}, pode comprar $ {compraDolares:.2f}")
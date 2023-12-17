""" 
Faça um algorítimo que leia o preço de um produto e mostre seu novo preço , com 5% de desconto 
"""
produto = float(input("Informe o preço de um produto: "))

desconto = 0.05 * produto

valor_final = produto - desconto

print(f"O valor do produto com desconto de 5% será de R$ {valor_final:.2f}")
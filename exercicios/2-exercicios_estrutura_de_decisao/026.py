""" 
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro 
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""
print("Informe A para Álcool ou G para Gasolina, nas informações a seguir: ")

tipo_combustivel = input("Qual o tipo de combustível? ").upper()
litros_vendidos = float(input("Quantos litros ? "))

preco_gasolina = 2.50
preco_alcool = 1.90
desconto = 0.0
valor_total = 0.0

if tipo_combustivel == "A":
    
    if litros_vendidos <= 20:
        desconto = litros_vendidos * 0.03
    else:
        desconto = litros_vendidos * 0.05

    valor_total = (litros_vendidos * preco_alcool) - desconto

if tipo_combustivel == "G":
    
    if litros_vendidos <= 20:
        desconto = litros_vendidos * 0.04
    else:
        desconto = litros_vendidos * 0.06
    
    valor_total = (litros_vendidos * preco_gasolina) - desconto        

print(f" O valor total a ser pago é: R$ {valor_total:.2f}")
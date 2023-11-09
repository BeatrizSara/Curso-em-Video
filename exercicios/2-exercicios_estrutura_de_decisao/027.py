"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""
quantidade_morango = float(input("Informe a quantidade de morango em Kg: "))
quantidade_maca = float(input("Informe a quantidade de maçãs em Kg: "))

total_morango = 0.0
total_maca = 0.0
total_frutas = 0.0
desconto = 0.0
total_compra = 0.0

if quantidade_morango <= 5:
    total_morango = quantidade_morango * 2.50
else:
    total_morango = quantidade_morango * 2.20

if quantidade_maca <= 5:
    total_maca = quantidade_maca * 1.80
else:
    total_maca = quantidade_maca * 1.50

total_frutas = (total_morango + total_maca) 

if (quantidade_morango + quantidade_maca) > 8 or (total_frutas) > 25.00:
    desconto = total_frutas * 0.1

total_compra = total_frutas - desconto

print(f"Total da compra: R$ {total_compra:.2f}")
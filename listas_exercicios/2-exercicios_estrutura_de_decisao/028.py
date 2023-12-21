""" 
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
Se a compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

tipo_de_carne = int(input("1 - Filé Duplo\n2 - Alcatra \n3 - Picanha\nInforme qual tipo de carne: "))
quantidade_carne = float(input("Informe a quantidade da carne: "))
cartao_tabajara = input("Pagamento pelo cartão Tabajara? \nS - sim ou N - não: ").upper()
tipo_pagamento = input("Forma de pagamento será: \nCartão Tabajara ou Dinheiro: ").upper()

desconto = 0.0
preco_total = 0.0
total_compra = 0.0

if tipo_de_carne == 1:
    if quantidade_carne <= 5:
        preco_total = quantidade_carne * 4.90
            
    else:
        preco_total = quantidade_carne * 5.80
            
            
elif tipo_de_carne == 2:
    if quantidade_carne <= 5:
        preco_total = quantidade_carne * 5.90
            
    else:
        preco_total = quantidade_carne * 6.80
            
elif tipo_de_carne == 3:
    if quantidade_carne <= 5:
        preco_total = quantidade_carne * 6.90
    else:
        preco_total = quantidade_carne * 7.80
        
else: 
    print("Valor Inválido. Informe apenas o que se pede acima.")


if cartao_tabajara == "S":
    desconto = 0.05
    desconto = 0.05 * preco_total

total_compra = preco_total - desconto

print(f"{"=" * 4} NOTA FISCAL {"=" * 4} \nEscolha da carne: {tipo_de_carne} \nQuantidade da carne: {quantidade_carne:.1f}Kg \nPreço Total: R$ {preco_total:.2f} \nTipo de pagamento: {tipo_pagamento} \nValor do desconto: {desconto:.2f} \nO total da compra será: R$ {total_compra:.2f}")
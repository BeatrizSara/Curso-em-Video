"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
"""
# Controlar o Rendimento Diário do trabalho do João
# Peso de peixes MAIOR que o estabelecido pelo regulamento - 50kg - não pode passarr de 50
# Multa de R$ 4,00 por Kg Excedente !!
# Criar variável (Excesso) com a quantidade de kilos alem do limite
# Criar variável (Multa) que João deverá pagar


peixesPeso = float(input("Informe o peso do peixe: "))

if peixesPeso > 50:
    excesso = peixesPeso - 50
    multa = excesso * 4
    print(f" O peso de peixes é maior que 50Kg, com isso, João deve pagar uma multa de: R${
          multa: .2f}. O excesso foi de {excesso: .2f} Kg")
else:
    print("O peso de peixes é menor que 50Kg. João não precisa pagar nenhuma multa!")

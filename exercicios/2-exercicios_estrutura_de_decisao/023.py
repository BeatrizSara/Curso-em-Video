""" 
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento.
"""

numero = float(input("Digite um número: "))

arredondado = round(numero)

if arredondado == numero:
    print("O número é inteiro! ")

else:
    print("O número é decimal! ")
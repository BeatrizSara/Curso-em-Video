""" 
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão, %).
"""

numInt = int(input("Informe um número inteiro: "))

restoDivisao = numInt % 2

if restoDivisao == 0:
    print(f"O número {numInt} é par!")
else:
    print(f"O número {numInt} é ímpar!")
    
""" 
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
Exemplo:
Digite um número: 6.127
O numero 6.127 tem a parte inteira 6.
"""
from math import trunc

num_real = float(input("Informe um número Real: "))
num_inteiro = trunc(num_real)

print(f"O valor digitado foi {num_real}, e a sua porção inteira é {num_inteiro} ")
""" 
Faça um Programa que leia três números e mostre o maior deles.
"""
numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
numero3 = float(input("Informe o teceiro número: "))

# Utilização da função embutida max
maiorNumero = max(numero1, numero2, numero3)

print(" O maior número é:", maiorNumero, "!")

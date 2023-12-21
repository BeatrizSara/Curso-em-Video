""" 
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
numero3 = float(input("Informe o teceiro número: "))

# Utilização da função max e min
maiorNumero = max(numero1, numero2, numero3)
menorNumero = min(numero1, numero2, numero3)

print(f"O maior número é: {
      maiorNumero: .2f}, e o menor número é: {menorNumero: .2f}!")

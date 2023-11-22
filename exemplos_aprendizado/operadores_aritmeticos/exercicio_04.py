""" 
Desafio 04
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
"""
metros = float(input("Informe um valor em metros: "))

centimetros = metros * 100
milimetros = metros * 1000

print(f"Seu valor em centímetros é: {centimetros} cm")
print(f"Seu valor em milímetros é: {milimetros} mm")
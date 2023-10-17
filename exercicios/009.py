""" 
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
"""
F = float(input("Informe uma temperartura em graus Fahrenheit: "))
C = 5 * ((F-32) / 9)

print(f"A temperatura em graus Celsius é de:{C: .2f}°C")

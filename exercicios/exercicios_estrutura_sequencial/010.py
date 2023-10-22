"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""
C = float(input("Informe uma temperatura em graus Celsius: "))

F = ((C * 9) / 5) + 32

print(f"A temperatura em graus Fahrenheit é: {F: .2f}°F")

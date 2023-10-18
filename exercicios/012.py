"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
altura = float(input("Informe a altura de uma pessoa em metros: "))

pesoIdeal = (72.7 * altura) - 58

print(f"O Peso Ideal para sua altura é: {pesoIdeal: .2f} Kg")

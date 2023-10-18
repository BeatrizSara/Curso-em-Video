"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""

altura = float(input("Informe sua altura em metros: "))

mulheres = (72.7 * altura) - 58
homens = (62.1 * altura) - 44.7

print(f" O peso ideal para mulheres é: {
      mulheres: .2f} Kg. E o peso Ideal para homens é: {homens: .2f} Kg")

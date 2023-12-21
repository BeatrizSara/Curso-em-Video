"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""
valorHora = float(input("Quanto você ganha por hora? R$: "))
horaMensal = float(input("Qual o número de horas trabalhadas no mês? "))

salario = valorHora*horaMensal
print(f"O total do salário no referido mês foi de R${salario: .2f}")

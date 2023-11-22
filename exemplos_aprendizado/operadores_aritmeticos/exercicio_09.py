""" 
Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
"""
salario = float(input("Informe o salário: "))

aumento = 0.15 * salario

novo_salario = salario + aumento

print(f"Novo salário com 15% de aumento: {novo_salario}")
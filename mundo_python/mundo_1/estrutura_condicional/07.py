""" 
Aumentos múltiplos
Cálculo de porcentagens múltiplas
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Pra os inferiores ou iguais, o aumento é de 15%.
"""
salario = float(input("Informe qual o salário do funcionário: "))

if salario <= 1250:
    novo_valor  = salario + (salario * 0.15)
    
else:
    novo_valor  = salario + (salario * 0.10)

print(f"O salário de R${salario} com aumento vai passar a ganhar R${novo_valor}")
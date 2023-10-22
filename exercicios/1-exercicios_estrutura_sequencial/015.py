"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
"""
# Perguntas - Quanto ganha por hora? e Qual o número de horas trabalhadas? ( duas variáveis )

valorHora = float(input("Informe quanto ganha por hora: "))
horasTrabalhadas = float(
    input("Informe o número de horas trabalhadas no mês: "))

# Calculo do salário no referido mês
salarioBruto = valorHora * horasTrabalhadas

# Calculo com descontos

impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05

# Calculo do Salário Líquido
salarioLiquido = salarioBruto - (impostoRenda+inss+sindicato)

# Resultado dos calculos
print(f" Valor do Salário Bruto foi de: R${salarioBruto: .2f} ")
print(f" Desconto do IR de 11% foi de: R${impostoRenda: .2f}")
print(f" Desconto do INSS de 8% foi de: R${inss: .2f}")
print(f" Desconto do Sindicato de 5% foi de: R${sindicato: .2f}")
print(f" Salário Líquido foi de: R${salarioLiquido: .2f}")

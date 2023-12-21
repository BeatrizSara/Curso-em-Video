"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 
3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""
valorHora = float(input("Informe o valor de sua hora de trabalho: R$ "))
horasTrabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

# INSS = 10% e fgts = 11% e IR - % de acordo com cada salário Bruto acima.

inss = 0.1
fgts = 0.11

salarioBruto = valorHora * horasTrabalhadas
descontoInss = salarioBruto * inss
descontoFgts = salarioBruto * fgts

if salarioBruto < 900:
    totalDescontos =  descontoFgts + descontoInss
    salarioLiquido = salarioBruto - totalDescontos
    print(f"""         
Salário Bruto:                  : R$  {salarioBruto:.2f}
(-) IR (0%)                     : R$  {0} 
(-) INSS ( 10%)                 : R$  {descontoInss:.2f}
(-) FGTS (11%)                  : R$  {descontoFgts:.2f}
Total de descontos              : R$  {totalDescontos:.2f}
Salário Liquido                 : R$  {salarioLiquido:.2f}\n""")
elif salarioBruto < 1500:
    descontoIr = salarioBruto * 0.05
    totalDescontos = descontoIr + descontoFgts + descontoInss
    salarioLiquido = salarioBruto - totalDescontos
    print(f"""         
Salário Bruto:                  : R$  {salarioBruto:.2f}
(-) IR (5%)                     : R$  {descontoIr:.2f} 
(-) INSS ( 10%)                 : R$  {descontoInss:.2f}
(-) FGTS (11%)                  : R$  {descontoFgts:.2f}
Total de descontos              : R$  {totalDescontos:.2f}
Salário Liquido                 : R$  {salarioLiquido:.2f}\n""")
elif salarioBruto < 2500:
    descontoIr = salarioBruto * 0.1
    totalDescontos = descontoIr + descontoFgts + descontoInss
    salarioLiquido = salarioBruto - totalDescontos
    print(f"""         
Salário Bruto:                  : R$  {salarioBruto:.2f}
(-) IR (10%)                    : R$  {descontoIr:.2f} 
(-) INSS ( 10%)                 : R$  {descontoInss:.2f}
(-) FGTS (11%)                  : R$  {descontoFgts:.2f}
Total de descontos              : R$  {totalDescontos:.2f}
Salário Liquido                 : R$  {salarioLiquido:.2f}\n""")
else:
    descontoIr = salarioBruto * 0.2
    totalDescontos = descontoIr + descontoFgts + descontoInss
    salarioLiquido = salarioBruto - totalDescontos
    print(f"""         
Salário Bruto:                  : R$  {salarioBruto:.2f}
(-) IR (20%)                    : R$  {descontoIr:.2f} 
(-) INSS ( 10%)                 : R$  {descontoInss:.2f}
(-) FGTS (11%)                  : R$  {descontoFgts:.2f}
Total de descontos              : R$  {totalDescontos:.2f}
Salário Liquido                 : R$  {salarioLiquido:.2f}\n""")
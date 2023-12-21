"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
salario = float(input("Qual o valor do seu salário? "))

if salario <= 280:
    print(f"O salário antes do reajuste: R$ {salario:.2f}")
    print(f"O percentual de aumento aplicado: 20%")
    aumento = salario * 0.2
    print(f"O valor do aumento é de: R$ {aumento:.2f}")
    novoSalario = aumento + salario
    print(f"O novo salário, após o aumento: R$ {novoSalario:.2f}")
elif salario < 700:
     print(f"O salário antes do reajuste: R$ {salario:.2f}")
     print(f"O percentual de aumento aplicado: 15%")
     aumento = salario * 0.15
     print(f"O valor do aumento é de: R$ {aumento:.2f}")
     novoSalario = aumento + salario
     print(f"O novo salário, após o aumento: R$ {novoSalario:.2f}")
elif salario < 1500:
    print(f"O salário antes do reajuste: R$ {salario:.2f}")
    print(f"O percentual de aumento aplicado: 10%")
    aumento = salario * 0.1
    print(f"O valor do aumento é de: R$ {aumento:.2f}")
    novoSalario = aumento + salario
    print(f"O novo salário, após o aumento: R$ {novoSalario:.2f}")
else :
    print(f"O salário antes do reajuste: R$ {salario:.2f}")
    print(f"O percentual de aumento aplicado: 5%")
    aumento = salario * 0.05
    print(f"O valor do aumento é de: R$ {aumento:.2f}")
    novoSalario = aumento + salario
    print(f"O novo salário, após o aumento: R$ {novoSalario:.2f}")
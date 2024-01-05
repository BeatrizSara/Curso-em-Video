""" 
Aprovando Emprestimo
Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou entao o emprestimo será negado.
"""

valor_casa = float(input("Qual o valor desejado da casa? R$ "))
salario = float(input("Qual o salario do comprador? R$"))
anos = int(input("Quantos anos de financiamento? "))

prestacao_mensal = valor_casa / (anos * 12) 
limite = salario * 0.3 

#O valor da prestação mensal do empréstimo não deve ser maior do que 30% do salário do comprador. Se não, será negado!
if prestacao_mensal <= limite:
    print("Empréstimo APROVADO!")
    print(f"Para pagar uma casa de R${valor_casa:.2f} \nA prestação será de R$ {prestacao_mensal:.2f}")
 

else:
    print("Empréstimo NEGADO!")
    
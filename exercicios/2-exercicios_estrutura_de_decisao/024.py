""" 
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a) par ou ímpar;
b) positivo ou negativo;
c) inteiro ou decimal.
"""
num1 = float(input("Informe um número: "))
num2 = float(input("Informe um segundo número: "))
operacao = input("Qual operação deseja realizar? (+, -, * ou /)")
valido = True

match operacao:
    
    case "+":
        resultado = num1 + num2
    case "-":
        resultado = num1 - num2
    case "*":
        resultado = num1 * num2
    case "/":
        resultado = num1 / num2
    case _:
        print("Operação inválida.")
        valido = False

if valido:

    print(f"O resultado da operação de {num1} {operacao} {num2} é {resultado}")
            
    restoDivisao = resultado % 2

    if restoDivisao == 0:
        print("O número é par!")
    else:
        print("O número é ímpar!")

    arredondado = round(resultado)

    if arredondado == resultado:
        print("O número é inteiro! ")
    else:
        print("O número é decimal! ")
        
    if resultado > 0:
        print("O número é positivo.")
    elif resultado < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")
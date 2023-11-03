"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""
saque = int(input("Informe o valor do saque: (min 10 reais / max 600 reais) "))

if saque >= 10 and saque <= 600:
    
    print("O saque possui: ")
    
    if saque >= 100:
        nota100 = int(saque / 100)
        saque = saque - (nota100*100)
        print(f"{nota100} nota(s) de 100 reais ")

    if saque >= 50: 
        nota50 = int(saque/50)
        saque = saque - (nota50*50)
        print(f"{nota50} nota(s) de 50 reais ")
        
    if saque >= 10:
        nota10 = int(saque/10)
        saque = saque - (nota10*10)
        print(f"{nota10} nota(s) de 10 reais ")
        
    if saque >= 5:
        nota5 = int(saque/5)
        saque = saque - (nota5*5)
        print(f"{nota5} nota(s) de 5 reais ")
        
    if saque >= 1:
        nota1 = int(saque)  
        print(f"{nota1} nota(s) de 1 real ")
        
else:
    print("Valor inválido. Não corresponde ao valor (min 10 reais / max 600 reais)!")
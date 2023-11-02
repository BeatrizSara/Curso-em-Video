"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
"""    
numero = int(input("Informe um número inteiro menor que 1000: "))

if numero < 0 or numero >= 1000:
    print(" O numero não corresponde o que foi solicitado!")
    
else:
    numero = str(numero)
    
    if len(numero) == 1:
        print("Centena: 0 ")
        print("Dezena: 0 ")
        print("Unidade: {}".format(numero[0]))
    elif len(numero) == 2:
        print("Centena: 0 ")
        print("Dezena: {}".format(numero[0]))
        print("Unidade: {}".format(numero[1]))
    else:
        print("Centena: {}".format(numero[0]))
        print("Dezena: {}".format(numero[1]))
        print("Unidade: {}".format(numero[2]))
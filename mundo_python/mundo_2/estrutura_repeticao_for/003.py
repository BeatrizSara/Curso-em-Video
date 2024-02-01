""" 
Faça um programa que calcule a soma entre todos os numeros impares ( nao é para somar todos), mas sim,
que são múltiplos de três e que 
se encontram no intervalo de 1 até 500.
Soma dos numeros
Contador de quantos numeros tem dentro de 1 a 500 que sao multiplos de 3
"""

numeros_impares = []
soma = 0
contador = 0

for numero in range(1,501,2):
    if numero % 3 == 0:
        numeros_impares.append(numero) 
        contador +=  1 #contador - soma com + 1
        soma += numero #acumulador - soma com o valor
        
print(f"A soma de todos os {contador} valores solicitados é: {soma}")
print("Os numeros dentro de 1 a 500 que são multiplos de 3 são:\n{}".format(numeros_impares))

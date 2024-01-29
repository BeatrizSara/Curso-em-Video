""" 
Faça um programa que calcule a soma entre todos os numeros impares ( nao é para somar todos), mas sim,
que são múltiplos de três e que 
se encontram no intervalo de 1 até 500.
"""

numeros_impares = []

for numero in range(1,501):
    if numero % 3 == 0:
        numeros_impares.append(numero)

print("Os numeros dentro de 1 a 500 que são multiplos de 3 são:\n{}".format(numeros_impares))
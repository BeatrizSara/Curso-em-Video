""" 
Exercicio 047
Contagem de Pares
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""
numeros_pares = []

for numero in range(1,51):
    if numero % 2 == 0:
        numeros_pares.append(numero)
    
print("Os numeros pares que estão entre 1 a 50 são:\n{}".format(numeros_pares))

#A lista numeros_pares armazena todos os números pares encontrados durante o loop. 
# O resultado será a lista de números pares entre 1 e 50.
#Importante o numero de interações e numero de laços

# for numero in range(2, 51, 2)
#     print(n, end=" ")
#print("Acabou")
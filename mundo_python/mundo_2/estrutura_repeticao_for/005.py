""" 
Exercicio 050 - Soma dos pares
Desenvolva um programa que leia seis numeros inteiros 
e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for impar, desconsidere-o.
"""
soma = 0 
contador = 0
lista = range(1, 7)

for item in lista:
        num = int(input("Informe o {} valor: ".format(item)))
        if num % 2 == 0:
            soma += num
            contador += 1
        
print("Foi informado {} numeros pares, e a soma foi: {}".format(contador, soma))
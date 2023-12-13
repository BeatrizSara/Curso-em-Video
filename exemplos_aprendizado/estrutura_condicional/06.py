""" 
Maior e menor valores
Faça um progrograma que leia três números mostre qual é o maior e qual é o menor
"""
valor1= int(input("Informe um número inteiro:"))
valor2 = int(input("Informe um segundo número inteiro: "))
valor3 = int(input("Informe um terceiro número inteiro: "))

lista = [valor1, valor2, valor3] 
lista.sort()

print(f'O maior número é {lista[2]} e o menor é {lista[0]}')

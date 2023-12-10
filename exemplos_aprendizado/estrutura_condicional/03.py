""" 
Par ou Ímpar?
Crie um programa que leia um número inteiro
"""
numero = int(input("Informe um número aleatório inteiro: "))

resultado = numero % 2

print(f"O resultado foi {resultado}")

if resultado == 1:
    print(f"O número {numero} é: Ímpar")
    
else:
    print(f"O número {numero} é: Par")
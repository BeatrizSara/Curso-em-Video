""" 
Par ou Ímpar?
Crie um programa que leia um número inteiro
"""
#Obs: Usou o operador de porcentagem para calcular o resto da divisão. 
#Todo número par é divisivel por 2 ou o resto da divisão por 2 é igual a zero

numero = int(input("Informe um número aleatório inteiro: "))

resultado = numero % 2

print(f"O resultado foi {resultado}")

if resultado == 1:
    print(f"O número {numero} é: Ímpar")
    
else:
    print(f"O número {numero} é: Par")
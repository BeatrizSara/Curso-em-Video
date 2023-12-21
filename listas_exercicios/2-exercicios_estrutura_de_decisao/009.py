"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
number1 = float(input("Informe um número: "))
number2 = float(input("Informe um segundo número: "))
number3 = float(input("Informe um terceiro número: "))

listaNumeros = [number1, number2, number3]

ordemDecrescente = sorted(listaNumeros, reverse=True)

print("Números em ordem decrescente:", ordemDecrescente)

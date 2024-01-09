""" 
Analisando Triângulo
(035 - mundo 1 de Pyhton)
Desenvolva um programa que leia o comprimento de três retas 
e diga ao usuário se elas podem ou não formar um triângulo.
"""

print("*" * 31)
print(" ▲  ANALISADOR DE TRIÂNGULOS ▲ ") 
print("*" * 31)

ladoA = float(input("Digite um valor para formar um triângulo: "))
ladoB = float(input("Digite um segundo valor para formar um triângulo: "))
ladoC = float(input("Digite um terceiro valor para formar um triângulo: "))

#Triangle is True if : a + b > c and a + c > b and b + c > a


if ladoA + ladoB > ladoC  and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    print("Os valores acima PODEM FORMAR UM TRIÂNGULO!")

else:
    print("Os valores acima NÃO PODEM FORMAR UM TRIÂNGULO!") 
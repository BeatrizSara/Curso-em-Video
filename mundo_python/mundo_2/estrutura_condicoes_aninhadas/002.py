""" 
Conversor de Bases Numéricas  - Sistema de Numeração - 037
Escreva um programa que leia um número inteiro qualquer e
peça para o usuário  escolher qual será a base de conversão:
- 1 para binário = 0b
- 2 para octal = 0o
- 3 para hexadecimal = 0x
"""

num = int(input("Informe um numero inteiro: "))
print("""Escolha a base para conversão:
    [1] converter para Binário
    [2] converter para Octal
    [3] converter para Hexadecimal """)

escolha = int(input("OPÇÃO: "))

if escolha == 1:
    print("{} convertido para BINÁRIO será igual a {}".format(num, bin(num)[2:]))
elif escolha == 2:
    print("{} convertido para OCTAL será igual a {}".format(num, oct(num)[2:]))
    
elif escolha == 3:
    print("{} convertido para HEXADECIMAL será igual a {}".format(num, hex(num)[2:]))
        
else:
    print("Opção Inválida. Deve-se informar apenas as opções solicitadas acima. Tente novamente")
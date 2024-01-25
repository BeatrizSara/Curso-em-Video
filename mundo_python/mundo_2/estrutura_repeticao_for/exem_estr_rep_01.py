""" 
EXEMPLOS
Estrutura de Repetição FOR
Laço de repetiçao parte 1
Cuidar com a identação
O ultimo ele ignora se for (1, 6)conta apenas até o 5
(6,0, -1) -1 contagem de cimma para baixo
(0, 7, 2) - 2 significa que vai pular de 2 em dois
range(0, n+1)  como parte de passagem para o FOR
Ex:
"Digite um número: 3
0 
1
2
3
FIM
"""
# Passo significa de quanto em quanto o numero informado vai pular.
# Se for: inicio 1, fim 100 e passo 10, vai contar de  10 em 10 - 1 11 21 31 41 51.. 100
#Pode-se utilizar da estrutura de repetição para fazer o que voce quiser
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in range (i, f+1, p):
    print(c)
print("FIM")

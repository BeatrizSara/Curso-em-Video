""" 
Exercicio 051
Progressao Aritimética
Desenvolva um programa que leia o primeiro termo e a razao de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
an = an-1 + r
formula do n - ésimo termo
""" 
primeiro_termo = int(input("Primeiro Termo: "))
razao = int(input("Razao entre eles: "))
decimo_termo = primeiro_termo + (10 -1) * razao

for c in range(primeiro_termo, decimo_termo + razao, razao):
    print("{}".format(c), end = " => ")
    
print("fim")
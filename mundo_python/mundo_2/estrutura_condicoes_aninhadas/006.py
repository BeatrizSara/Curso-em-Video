""" 
Classificando Atletas
A Confederação Nacional de Natação precisa de 
um programa que leia o ano de nascimento de um atleta 
e mostre sua categoria de acordo com a idade:
- Até 9 anos : MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos:JUNIOR
- Até 25 anos: Sênior
- Acima: MASTER
"""
from datetime import date
atual = date.today().year
data_nasc = int(input("Data de nascimento:"))
idade = atual - data_nasc

print(f"O atleta tem {idade} anos")

if idade <= 9:
    print("Categoria: MIRIM")

elif idade <= 14:
    print("Categoria: INFANTIL")

elif idade <= 19:
    print("Categorai: JUNIOR")

elif idade <= 25:
    print("Categoria: SÊNIOR")
    
else:
    print("Categoria: MASTER")
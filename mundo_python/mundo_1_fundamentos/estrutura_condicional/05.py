""" 
Ano Bissexto
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
Obs: A condição para ser bissexto é que o ano seja divisível por 4, 
mas não por 100, a menos que seja divisível por 400.
"""

from datetime import date
ano = int(input("Informe um ano para saber se é BISSEXTO. Coloque 0 para analisar o ano atual:   "))

if ano == 0:
    ano = date.today().year #Comando para pegar o ano atual que esta na máquina]

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO!")
    
else:
    print(F"O ano {ano} NÃO é BISSEXTO")
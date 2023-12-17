""" 
Faça um programa utilizando dois Whiles para execução da Tabuada do 1 ao 10.
"""
contador1 = 0

while contador1 <= 10:
    
    contador2 = 0
    
    print(f"Tabuada do número {contador1}")
    
    while contador2 <= 10:
        print(f"{contador1} x {contador2} = {contador2 * contador1}")
        contador2 += 1 
    
    contador1 += 1    
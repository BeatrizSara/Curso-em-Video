""" 
Analisando triangulos 
(042 - mundo 2 de Pyhton)
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
OBS: mundo 1 - estrutura condicional 08
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
print("Informe a seguir, números para formar um tipo de triângulo")
lado_a = float(input("\nInforme o primeiro número: "))
lado_b = float(input("Informe o segundo número: "))
lado_c = float(input("Informe o terceiro número: "))

if lado_b + lado_c > lado_a and lado_a + lado_c > lado_b and lado_a + lado_b > lado_c:
    print("Esses valores podem formar um triângulo ", end="")
    
    if lado_a == lado_b == lado_c:
        print(" => EQUILÁTERO")
        
    # elif lado_a != lado_b != lado_c: (obs: lado a pode ser igual a lado c)
    # Por isso lado a tem que ser != de lado b e c. Se não, o else não vai como ISOSCELES
    elif lado_a != lado_b != lado_c != lado_a:
        print("=> ESCALENO")
    
    else:
        print("=> ISÓSCELES")

else:
    print("Os valores acima não podem formar um triângulo")
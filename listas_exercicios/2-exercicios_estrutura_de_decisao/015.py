""" 
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

## Pede os 3 lados. Faz o calculo da primeira dica pra dizer se com os lados informados é possivel formar um triangulo, se sim calcular se ele é equilatero, isosceles ou escaleno

lado1 = float(input("informe o valor do lado de um triângulo: "))
lado2 = float(input("informe o valor do segundo lado de um triângulo: "))
lado3 = float(input("informe o valor do terceiro lado de um triângulo: "))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    if lado1 == lado2 == lado3:
        print("Triângulo é Equilátero!")
    elif lado1 != lado2 != lado3:
        print("Triângulo é Escaleno!")
    else:
        print("Triângulo é Isósceles!")
else:
    print("Os lados fornecidos não podem formar um triângulo.")
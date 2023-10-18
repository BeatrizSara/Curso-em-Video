"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
"""
numeroInteiro1 = int(input("Informe um número inteiro: "))
numeroInteiro2 = int(input("Informe um segundo número inteiro: "))

numeroReal = float(input("Informe um número real: "))

letraA = (numeroInteiro1 * 2) * (numeroInteiro2/2)
letraB = (numeroInteiro1 * 3) + numeroReal
letraC = numeroReal**3

print(f"a) O produto do dobro do primeiro com metade do segundo: {
      letraA: .2f}")
print(f"b) A soma do triplo do primeiro com o terceiro: {letraB: .2f}")
print(f"c) O terceiro elevado ao cubo: {letraC: .2f}")

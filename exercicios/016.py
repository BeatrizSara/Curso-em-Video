"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
tamanhoMetros = float(input("Informe o tamanho em m² da área a ser pintada: "))

latas = tamanhoMetros / (3 * 18)
latasInt = int(latas)

if latas != latasInt:
    latas = latasInt + 1

precoTotal = latas * 80

print(f" A quantidade de latas a ser comprado é de: {latas}")
print(f" O valor total a pagar será: R$ {precoTotal: .2f}")

# Realizar um somatorio desses números
# s += n é a mesma coisa que s = s + n
s = 0

for c in range(0, 4):
    n = int(input("Digite um valor: "))
    s += n
print("O somatório de todos os valores foi {}".format(s))

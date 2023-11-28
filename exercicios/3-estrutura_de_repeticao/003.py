""" 
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

while True:
    nome = input("Informe o nome: ")
    
    if len(nome) > 3:
        break
    else: 
        print("O nome deve possuir mais do que 3 caracteres")

while True:
    idade = int(input("Informe a idade: "))

    if idade > 0 and idade < 150:
        break
    else:
        print("Deve informar a idade entre 0 e 150.")

while True:
    salario = float(input("Informe o salário: R$"))

    if salario > 0:
        break
    else:
        print("O salário deve ser maior que zero.")

while True:
    sexo = input("Informe o sexo, F- Feminino ou M - Masculino: ").upper()

    if sexo == "F" or sexo == "M":
        break
    else:
        print("O sexo deve ser M para masculino ou F para Feminino.")
        
while True:
    estado_civil = input("Informe o estado civil, S - solteiro, C- casado, V - viúvo, D- Divorciado: ").upper()

    match estado_civil:
        case "S":
            break
        case "C":
            break
        case "V":
            break
        case "D":
            break
        case _:
            print("Informe o estado civil solicitado.")
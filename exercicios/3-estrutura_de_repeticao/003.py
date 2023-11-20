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
    idade = int("Informe a idade: ")
    salario = float(input("Informe o salário: R$"))
    sexo = input("Informe o sexo, F- Feminino ou M - Masculino: ").upper()
    estado_civil = input("Informe o estado civil, S - solteiro, C- casado, V - viúvo, D- Divorciado: ").upper()
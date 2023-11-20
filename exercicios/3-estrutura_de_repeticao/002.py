""" 
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
while True:
    
    usuario = input("Informe o nome de usuário: ")
    senha = input("Informe a senha: ")
    
    if senha == usuario:
        print("Não é possível a senha ser igual ao nome de usuário! \nTente novamente.")
    
    else:
        print("Cadastro realizado com sucesso!!")
        break
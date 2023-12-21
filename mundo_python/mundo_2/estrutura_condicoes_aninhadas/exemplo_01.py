""" 
Exemplos de aprendizado MUNDO 2  - Condições Aninhadas
"""
#Esse é um exemplo de uma estrutura condicional aninhada
nome = str(input("Qual é o seu nome?"))

if nome == "Beatriz":
    print("Que nome bonito!")

elif nome == "João" or nome  == "Maria" or nome == "Pedro":
    print("Seu nome é muito popular no Brasil")

elif nome in "Ana Cláudia Jessica Juliana":
    print("Belo nome feminino!")
    
else:
    print("Seu nome é bem normal.")

print(f"Tenha um ótimo dia, {nome}")
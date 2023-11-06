"""
Faça um programa que peça  para o cliente notas de 1 a 10 referente a 1) qualidade do atendimento, 2) da comida, 3)do local e do 4) preco do restaurante
Se a media de notas for maior  ou igual a 8 - Informe que o restaurante eh ótimo
Se a media for maior ou igual a 6 e menor que 8 - Informe que o restaurante é bom
Se a media for maior ou igual a 3 e menor que 6 - Informe que o restaurante é razoável
Se a media for menor que 3 - Informe que o restaurante é pessimo
"""
print("Digite a nota para o Restaurante de 1 a 10 para as seguintes informações a seguir: ")
resposta1 = int(input("Nota para qualidade do atendimento de 1 a 10): "))
resposta2 = int(input("Nota para comida de 1 a 10: "))
resposta3 = int(input("Nota para o local de 1 a 10: "))
resposta4 = int(input("Nota preço do restaurante de 1 a 10: "))

notaFinal = (resposta1 + resposta2 + resposta3 + resposta4) / 4

if notaFinal >= 8:
    print("Restaurante ótimo")
    
elif notaFinal >= 6:
    print("Restaurante bom")
    
elif notaFinal >= 3:
    print("Restaurante razoável")
    
else:
    print("Restaurante péssimo")
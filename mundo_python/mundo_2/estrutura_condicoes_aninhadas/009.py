""" 
Gerenciador de pagamentos - 044
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro / cheque:
10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
print("{:=^40}".format(" LOJAS MANIA DE PREÇOS "))

compras = float(input("Valor da compra: R$ "))
print("FORMA DE PAGAMENTO\n[1] À vista dinheiro/cheque \n[2] À vista no cartão \n[3] Parcela em 2x \n[4] Parcelamento em 3x ou mais ")
opcao = int(input("Qual opção de pagamento: "))

if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
    if opcao == 1:
        desconto = compras * 0.1
        total = compras - desconto
    
    elif opcao == 2:
        desconto = compras * 0.05
        total = compras - desconto

    elif opcao == 3:
        total = compras
        parcela = total / 2
        print("Compra parcelada em 2x de {:.2f}".format(parcela))

    else:
        num_parcelas = int(input("Parcelar em 3x ou mais? "))
        if num_parcelas > 3:
            juros = compras * 0.2
            total =  compras + juros
            parcela = total / num_parcelas
            print("Compra parcelada em {}x de R$ {:.2f} COM JUROS".format(num_parcelas,parcela))
        else:
            total = 0
            print("Opção INVÁLIDA. Tente novamente ")

    print("A compra de R$ {:.2f} vai custar R$ {:.2f} no final".format(compras, total))

else:
    print("Opção INVÁLIDA. Verifique as opções novamente")
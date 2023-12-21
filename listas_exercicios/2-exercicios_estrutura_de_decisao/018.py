"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""
def is_data_valida(data):
    try:
        # Tente criar um objeto de data a partir da entrada
        dia, mes, ano = map(int, data.split('/'))
        data_formatada = f'{ano:04d}-{mes:02d}-{dia:02d}'
        
        # Verifique se o objeto de data foi criado com sucesso
        from datetime import datetime
        datetime.strptime(data_formatada, '%Y-%m-%d')
        
        return True
    except ValueError:
        return False

data = input("Digite uma data no formato dd/mm/aaaa: ")

if is_data_valida(data):
    print("A data é válida.")
else:
    print("A data não é válida.")
    
    
   # FAZER EXERCICIO PARA DAR COMIT !! 
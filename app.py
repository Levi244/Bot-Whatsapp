
import openpyxl

workbook = openpyxl.load_workbook('Clientes.xlsx')
pagina_clientes = workbook['Contatos']

for linha in pagina_clientes.iter_rows(min_row=2):
    #nome, telefone
    nome = linha[0]
    telefone = linha[1].value
    
    link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}'
    
    
    
    print(nome)
    print(telefone)


import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/')
sleep(20)

workbook = openpyxl.load_workbook('Clientes.xlsx')
pagina_clientes = workbook['Contatos']

for linha in pagina_clientes.iter_rows(min_row=2):
    #nome, telefone
    nome = linha[0]
    telefone = linha[1].value

    mensagem = f'Olá! {nome}'
    
    link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
    webbrowser.open(link_mensagem_whatsapp)
    
    input('')
    

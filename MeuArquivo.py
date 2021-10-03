import pandas as pd
import smtplib
import email.message
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

tabela_vendas = pd.read_excel('Vendas.xlsx')

pd.set_option('display.max_columns', None)

faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})

email_from = os.environ.get("EMAIL_FROM")
email_to = "email@email.com.br"

smtp = "smtp.gmail.com"

corpo_email = f"""
    <h2>Prezados,</h2>

    <strong>Segue o relatório de vendas por cada loja.</strong>

    <strong>Faturamento:</strong>
    {faturamento.to_html(formatters={'Valor Final': 'R${:,.2F}'.format})}

    <strong>Quantidade vendida:</strong>
    {quantidade.to_html()}

    <strong>Ticket médio dos produtos em cada loja:</strong>
    {ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2F}'.format})}

    <strong>Qualquer dúvida estou à disposição.</strong>
    
    <hr/>
    
    <p>Att,</p>
    <p>Fulano de tal</p>
"""

server = smtplib.SMTP(smtp, 587)
server.starttls()
server.login(email_from, open('senha.txt').read().strip())

msg = email.message.Message()

msg.add_header('Content-Type', 'text/html')
msg['Subject'] = "Assunto do e-mail"

msg.set_payload(corpo_email)

server.sendmail(email_from, email_to, msg.as_string().encode('utf-8'))
server.quit()

print("E-mail enviado com sucesso")

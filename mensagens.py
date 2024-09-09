import pandas as pd
import pywhatkit as pwk
import time



# Carregar a planilha (substitua pelo caminho da sua planilha)
df = pd.read_excel('C:\\Users\\teste\\Desktop\\Pasta1.xlsx')


# Exemplo: assumindo que a planilha tem colunas chamadas 'nome', 'telefone', 'mensagem'
for index, row in df.iterrows():
    nome = row['nome']
    telefone = str(row['telefone'])  # Exemplo: +5511999999999 (com código do país)
    mensagem = f"Olá {nome}, {row['mensagem']}"
   
    # Adicionar o código do país se estiver faltando
    if not telefone.startswith('+'):
        telefone = '+55' + telefone  # Adiciona o código do Brasil, ajuste se necessário
   
    # Enviar a mensagem no WhatsApp (envia às 2 minutos a partir do tempo atual)
    pwk.sendwhatmsg(telefone, mensagem, time.localtime().tm_hour, time.localtime().tm_min + 2)
    
    # Esperar alguns segundos antes de enviar a próxima
    time.sleep(5)

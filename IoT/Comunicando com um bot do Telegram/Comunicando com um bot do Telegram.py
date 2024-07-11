# Código 15.8 - Comunicando com um bot do Telegram

# Bibliotecas necessárias para o código

# Importação das bibliotecas padrão
import urequests
import utime
import machine

# Importação das bibliotecas customizadas
from realiza_conexao import realiza_conexao

# Declaração das variáveis
global URL_da_requisicao
global OFFSET

OFFSET = 0

# Insere diretamente os tokens
bot_token = '6401229347:AAFrIuoP_QEaFhEDiCgYbVFf69HlnrKFSgE'
id_do_chat = '7374655417'

URL_da_requisicao = 'https://api.telegram.org/bot' + bot_token + '/getUpdates'
URL_de_envio = 'https://api.telegram.org/bot' + bot_token + '/sendMessage'

# Função que formata o retorno da mensagem do Telegram
def extrai_resultado(dict):
    array_da_resposta = dict['result']
    if array_da_resposta == []:
        return False
    else:
        array_resultante = array_da_resposta[0]
        return array_resultante

# Função que envia mensagem para o chat
def envia_mensagem(chatId, message):
    urequests.post(URL_de_envio + "?chat_id=" + str(chatId) + "&text=" + message)

# Função que recebe a mensagem do chat
def recebe_mensagem(url):
    global OFFSET
    try:  
        pacote_bruto = urequests.get(url + "?offset=" + str(OFFSET))
        pacote = pacote_bruto.json()
        resultado_final = extrai_resultado(pacote)
        if resultado_final != False:
            OFFSET = resultado_final['update_id'] + 1
            id_do_chat = resultado_final['message']['chat']['id']
            mensagem = resultado_final['message']['text']
            print('Mensagem recebida: {}'.format(resultado_final['message']['text']))
            print('ID do chat: {}'.format(resultado_final['message']['chat']['id']))
            envia_mensagem(id_do_chat, mensagem)
            return mensagem
    except:
        return None

# Realiza a conexão Wi-Fi
realiza_conexao()

# Laço de execução
while True:
    recebe_mensagem(URL_da_requisicao)
    utime.sleep(10)

# Código 15.9 - Controle um Anel de LED via Telegram

# Bibliotecas necessárias para o código

# Importação das bibliotecas padrão
import urequests  # Para realizar requisições HTTP
import utime  # Para manipular tempo e criar delays
import machine  # Para controle de hardware

# Importação das bibliotecas customizadas 
from realiza_conexao import *  # Função para realizar conexão Wi-Fi
from ws2812 import WS2812  # Biblioteca para controlar LEDs WS2812

# Declaração do Anel de LEDs
ws = WS2812(machine.Pin(28), 12)  # Inicializa o anel de LEDs no pino 28 com 12 LEDs

# Declaração das variáveis
global URL_da_requisicao  # URL para obter atualizações do bot
global OFFSET  # Offset para controle de mensagens processadas

OFFSET = 0  # Inicializa o offset com 0
bot_token = '6401229347:AAFrIuoP_QEaFhEDiCgYbVFf69HlnrKFSgE'  # Token do bot do Telegram
id_do_chat = '7374655417'  # ID do chat do Telegram
URL_da_requisicao = 'https://api.telegram.org/bot' + bot_token + '/getUpdates'  # Monta a URL para obter atualizações
URL_de_envio = 'https://api.telegram.org/bot' + bot_token + '/sendMessage'  # Monta a URL para enviar mensagens

# Função que formata o retorno da mensagem do telegram
def extrai_resultado(dict):
    array_da_resposta = dict['result']  # Obtém o array de resultados
    if array_da_resposta == []:
        return False  # Retorna False se o array estiver vazio
    else:
        array_resultante = array_da_resposta[0]  # Pega o primeiro resultado
        return array_resultante  # Retorna o resultado

# Função que envia mensagem para o chat
def envia_mensagem(chatId, message):
    urequests.post(URL_de_envio + "?chat_id=" + str(chatId) + "&text=" + message)  # Envia a mensagem

# Função que recebe a mensagem do chat
def recebe_mensagem(url):
    global OFFSET
    try:
        pacote_bruto = urequests.get(url + "?offset=" + str(OFFSET))  # Obtém as mensagens do Telegram
        pacote = pacote_bruto.json()  # Converte para JSON
        resultado_final = extrai_resultado(pacote)  # Extrai o resultado
        if resultado_final != False:
            OFFSET = resultado_final['update_id'] + 1  # Atualiza o offset
            id_do_chat = resultado_final['message']['chat']['id']  # Obtém o ID do chat
            mensagem = resultado_final['message']['text']  # Obtém a mensagem
            return (mensagem, id_do_chat)  # Retorna a mensagem e o ID do chat
    except:
        return None  # Retorna None em caso de erro

# Realiza a conexão Wi-Fi
realiza_conexao()

# Laço de execução
while True:
    mensagem = recebe_mensagem(URL_da_requisicao)  # Recebe mensagem do Telegram
    try:
        print(type(mensagem[1]))  # Imprime o tipo do ID do chat
    except:
        pass

    if mensagem is not None:
        if mensagem[0].lower() == 'liga':  # Se a mensagem for 'liga'
            ws.write_all(0xFFFFFF)  # Liga os LEDs
            envia_mensagem(mensagem[1], 'Ligado')  # Envia confirmação
            print("liga")
        elif mensagem[0].lower() == 'desliga':  # Se a mensagem for 'desliga'
            ws.write_all(0x000000)  # Desliga os LEDs
            envia_mensagem(mensagem[1], 'Desligado')  # Envia confirmação
            print("desliga")

        elif mensagem[0].lower() == 'azul':  # Se a mensagem for 'azul'
            ws.write_all(0x0000FF)  # Muda cor para azul
            envia_mensagem(mensagem[1], 'Mudada cor para Azul')  # Envia confirmação
            print("azul")

        elif mensagem[0].lower() == 'verde':  # Se a mensagem for 'verde'
            ws.write_all(0x00FF00)  # Muda cor para verde
            envia_mensagem(mensagem[1], 'Mudada cor para Verde')  # Envia confirmação
            print("verde")
            
        elif mensagem[0].lower() == 'vermelho':  # Se a mensagem for 'vermelho'
            ws.write_all(0xFF0000)  # Muda cor para vermelho
            envia_mensagem(mensagem[1], 'Mudada cor para Vermelho')  # Envia confirmação
            print("vermelho")
        else:
            try:
                ws.write_all(int(mensagem[0], 16))  # Tenta mudar cor usando o valor hexadecimal
                envia_mensagem(mensagem[1], 'Mudada cor para {}'.format(mensagem[0]))  # Envia confirmação
            except:
                envia_mensagem(mensagem[1], 'Comando não reconhecido')  # Envia mensagem de erro

    utime.sleep(1)  # Espera 10 segundos antes de verificar novamente

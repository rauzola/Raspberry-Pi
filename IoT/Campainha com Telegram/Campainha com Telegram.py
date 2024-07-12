# Código 15.10 - Campainha com Telegram

# Bibliotecas necessárias para o código

# Importação das bibliotecas padrão
import urequests
import utime
import machine
import _thread

# Importação das bibliotecas customizadas
from realiza_conexao import *

# Token do bot do Telegram e ID do chat
bot_token = '6401229347:AAFrIuoP_QEaFhEDiCgYbVFf69HlnrKFSgE'
id_do_chat = '7374655417'

# Declaração do buzzer
buzzer = machine.PWM(machine.Pin(14, machine.Pin.OUT))
buzzer.duty_u16(65535)

# Declaração dos botões
botao_1 = machine.Pin(18, machine.Pin.IN)
botao_2 = machine.Pin(19, machine.Pin.IN)
botao_3 = machine.Pin(20, machine.Pin.IN)
botao_4 = machine.Pin(21, machine.Pin.IN)

# Declaração das variáveis
global URL_da_requisicao
global OFFSET
global tempo_ultimo_toque
global campainha_apertada

campainha_apertada = False
tempo_ultimo_toque = 0
OFFSET = 0

URL_da_requisicao = 'https://api.telegram.org/bot' + bot_token + '/getUpdates'
URL_de_envio = 'https://api.telegram.org/bot' + bot_token + '/sendMessage'

# Função chamada ao apertar o botão 1
def button_1_isr(_):    
    global tempo_ultimo_toque
    if not utime.ticks_ms() - tempo_ultimo_toque < 200:
        global campainha_apertada
        campainha_apertada = True
        tempo_ultimo_toque = utime.ticks_ms()        

# Funções para os outros botões
def button_2_isr(_):    
    global tempo_ultimo_toque
    if not utime.ticks_ms() - tempo_ultimo_toque < 200:
        global campainha_apertada
        campainha_apertada = True
        tempo_ultimo_toque = utime.ticks_ms()    

def button_3_isr(_):  
    global tempo_ultimo_toque
    if not utime.ticks_ms() - tempo_ultimo_toque < 200:
        global campainha_apertada
        campainha_apertada = True
        tempo_ultimo_toque = utime.ticks_ms()

def button_4_isr(_):    
    global tempo_ultimo_toque
    if not utime.ticks_ms() - tempo_ultimo_toque < 200:
        global campainha_apertada
        campainha_apertada = True
        tempo_ultimo_toque = utime.ticks_ms()

# Declaração das interrupções que serão iniciadas ao toque dos botões
botao_1.irq(trigger=botao_1.IRQ_FALLING, handler=button_1_isr)
botao_2.irq(trigger=botao_2.IRQ_FALLING, handler=button_2_isr)
botao_3.irq(trigger=botao_3.IRQ_FALLING, handler=button_3_isr)
botao_4.irq(trigger=botao_4.IRQ_FALLING, handler=button_4_isr)

# Função que envia mensagem para o chat
def envia_mensagem(chatId, message):    
    urequests.post(URL_de_envio + "?chat_id=" + str(chatId) + "&text=" + message)

# Função que emite o som da campainha
def som_campainha():  
    buzzer.duty_u16(32767)
    buzzer.freq(500)
    utime.sleep(.5)
    buzzer.freq(300)
    utime.sleep(.5)
    buzzer.duty_u16(65535)

# Realiza a conexão Wi-Fi
realiza_conexao()

# Laço de execução
while True:
    if campainha_apertada:
        try:
            _thread.start_new_thread(som_campainha,())
        except:
            pass
        envia_mensagem(id_do_chat, 'Campainha acionada!')
        campainha_apertada = False
    utime.sleep(.3)

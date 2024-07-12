# Codigo 15.11 - Sistema de Segurança
 
# Bibliotecas necessarias para o codigo
 
# Importacao das bibliotecas padrao
 
import machine
 
import urequests
 
import utime
 
import _thread
 
# Importacao das bibliotecas customizadas 
 
from realiza_conexao import *
 
import credenciais
 
from ws2812 import WS2812
 
# Declaracao do Anel de LEDs
 
ws = WS2812(machine.Pin(28), 12)
 
ws.write_all(0x000000)

# Token do bot do Telegram e ID do chat
bot_token = '6401229347:AAFrIuoP_QEaFhEDiCgYbVFf69HlnrKFSgE'
id_do_chat = '7374655417'
 
# Declaracao do buzzer
 
buzzer = machine.PWM(machine.Pin(14, machine.Pin.OUT))
 
buzzer.duty_u16(65535)
 
# Declaracao do sensor PIR
 
pir_sensor = machine.Pin(16, machine.Pin.IN)
 
# Declaracao das variaveis
 
alarme_armado = False
 
alarme_disparado = False
 
movimento_detectado = False
 
global URL_da_requisicao
 
global OFFSET
 
global URL_de_envio
 
OFFSET = 0
 
URL_da_requisicao = 'https://api.telegram.org/bot' + bot_token +'/getUpdates'
 
URL_de_envio = 'https://api.telegram.org/bot' + bot_token +'/sendMessage'
 
# Funcao que formata o retorno da mensagem do telegram
 
def extrai_resultado (dict):    
 
    array_da_resposta = dict['result']
 
    if array_da_resposta == []:
 
        return False
 
    else:
 
        array_resultante = array_da_resposta[0]
 
        return array_resultante
 
# Funcao que envia mensagem para o chat
 
def envia_mensagem (chatId, message):    
 
    urequests.post(URL_de_envio + "?chat_id=" + str(chatId) + "&text=" + message)
 
# Funcao que executa as rotinas de disparo do alarme
 
def da_alarme ():    
 
    global alarme_disparado
 
    alarme_disparado = True
 
    _thread.start_new_thread(aciona_sirene,())
 
    envia_mensagem(id_do_chat,'Alarme disparou!')
 
# Funcao que recebe a mensagem do chat
 
def recebe_mensagem (url):    
 
    global OFFSET
 
    try:  
 
        pacote_bruto = urequests.get(url + "?offset=" + str(OFFSET))
 
        pacote = pacote_bruto.json()
 
        resultado_final = extrai_resultado(pacote)
 
        if resultado_final != False:
 
            OFFSET = resultado_final['update_id'] + 1
 
            id_do_chat = resultado_final['message']['chat']['id']
 
            mensagem = resultado_final['message']['text']
 
            return mensagem
 
    except:
 
        return None
 
# Funcao chamada ao haver uma deteccao de movimento
 
def detectou_movimento(_):    
 
    global movimento_detectado
 
    movimento_detectado = True    
 
# Declaracao da interrupcao que sera iniciada ao detectar movimento    
 
pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=detectou_movimento)
 
# Funcao que aciona o giroflex e a sirene
 
def aciona_sirene():   
 
    j=0
 
    buzzer.duty_u16(32767)
 
    timeSinceLastSwitch = utime.ticks_ms()
 
    buzzer.freq(500)
 
    proximoMultiplicador = 3
 
    while j<700 and alarme_armado:
 
        for i in range(12):
 
            if ((i+j)%12)//6 < 1:
 
                ws.write(i,0xFF0000)
 
            elif ((i+j)%12)//6 == 1:
 
                ws.write(i,0X0000FF)
 
        if ((utime.ticks_ms() - timeSinceLastSwitch > 300)):       
 
            buzzer.freq(500*proximoMultiplicador)
 
            if proximoMultiplicador == 3:
 
                proximoMultiplicador = 1
 
            else:
 
                proximoMultiplicador = 3
 
            timeSinceLastSwitch = utime.ticks_ms()
 
         
 
        # Inicio das luzes estroboscopicas, remova essa parte do codigo para que elas nao acontecam
 
        if j%59 == 0:
 
            ws.write_all(0xFFFFFF)
 
            buzzer.freq(500)
 
            utime.sleep_ms(40)
 
            ws.write_all(0xFF0000)
 
            buzzer.freq(100)
 
            utime.sleep_ms(40)
 
            ws.write_all(0xFFFFFF)
 
            buzzer.freq(500)
 
            utime.sleep_ms(40)
 
            ws.write_all(0x0000FF)
 
            buzzer.freq(100)
 
            utime.sleep_ms(40)
 
            ws.write_all(0xFFFFFF)
 
            buzzer.freq(500)
 
            utime.sleep_ms(40)
 
            ws.write_all(0xFF0000)
 
            buzzer.freq(100)
 
            utime.sleep_ms(40)
 
            ws.write_all(0xFFFFFF)
 
            buzzer.freq(500)
 
            utime.sleep_ms(40)
 
            ws.write_all(0x0000FF)
 
            buzzer.freq(100)
 
            utime.sleep_ms(40)
 
            buzzer.freq(500*proximoMultiplicador)
 
        # Fim das luzes estroboscopicas
 
             
 
        j+=1
 
        utime.sleep_ms(20)
 
    ws.write_all(0x000000)
 
    buzzer.duty_u16(65535)
 
    global alarme_disparado
 
    alarme_disparado = False
 
# Realiza a conexao Wi-Fi
 
realiza_conexao()
 
# Laco de execucao
 
while True:    
 
    mensagem = recebe_mensagem(URL_da_requisicao)
 
    if mensagem is not None:
 
        if mensagem == 'armar' or mensagem == 'Armar' or mensagem == 'ARMAR':
 
            alarme_armado = True
 
            envia_mensagem(id_do_chat, 'Alarme armado!')
 
        elif mensagem == 'desarmar' or mensagem == 'Desarmar' or mensagem == 'DESARMAR':
 
            alarme_armado = False
 
            envia_mensagem(id_do_chat, 'Alarme desarmado!')
 
    if alarme_armado and movimento_detectado and not alarme_disparado:   
 
        da_alarme()
 
        movimento_detectado = False
 
    elif alarme_armado and movimento_detectado and alarme_disparado:
 
        movimento_detectado = False
 
    elif not alarme_armado and movimento_detectado:
 
        movimento_detectado = False
 
    utime.sleep(.3)
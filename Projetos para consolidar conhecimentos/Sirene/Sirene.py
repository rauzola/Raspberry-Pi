# Codigo 14.2 - Sirene
 
# Bibliotecas necessarias para o codigo
 
# Importacao das bibliotecas padrao
 
import machine
 
import utime
 
import _thread
 
# Importacao das bibliotecas customizadas 
 
from ws2812 import WS2812
 
from colour import *
 
# Declaracao do anel de LEDs
 
ws = WS2812(machine.Pin(28), 12)
 
# Declaracao do buzzer
 
buzzer = machine.PWM(machine.Pin(14, machine.Pin.OUT))
 
# Declaracao dos botoes
 
botao_1 = machine.Pin(18, machine.Pin.IN)
 
botao_2 = machine.Pin(19, machine.Pin.IN)
 
botao_3 = machine.Pin(20, machine.Pin.IN)
 
botao_4 = machine.Pin(21, machine.Pin.IN)
 
# Declaracao das variaveis
 
estado_botao_1 = 0
 
estado_botao_2 = 0
 
estado_botao_3 = 0
 
estado_botao_4 = 0
 
giroflex_simples_ligado = False
 
giroflex_com_estrobo_ligado = False
 
sirene_ligada = False
 
# Funcao que comanda o anel de LEDs em animacao de giroflex simples
 
# e o buzzer (se estiver ativa a sirene) 
 
def giroflex_simples():
 
    global giroflex_simples_ligado
 
    j=0
 
    tempo_desde_ultima_mudanca = utime.ticks_ms()
 
    buzzer.freq(500)
 
    proximoMultiplicador = 3
 
    while(giroflex_simples_ligado):
 
        if sirene_ligada:
 
            duty = 32767
 
        else:
 
            duty = 65535
 
        buzzer.duty_u16(duty)
 
        for i in range(12):
 
            if ((i+j)%12)//6 < 1:
 
                ws.write(i,0xFF0000)
 
            elif ((i+j)%12)//6 == 1:
 
                ws.write(i,0X0000FF)
 
        if ((utime.ticks_ms() - tempo_desde_ultima_mudanca > 300)):       
 
            buzzer.freq(500*proximoMultiplicador)
 
            if proximoMultiplicador == 3:
 
                proximoMultiplicador = 1
 
            else:
 
                proximoMultiplicador = 3
 
            tempo_desde_ultima_mudanca = utime.ticks_ms()
 
        if j == 2000000000:
 
            j=0
 
        j+=1
 
        utime.sleep_ms(20)
 
    ws.write_all(0x000000)
 
    buzzer.duty_u16(65535)
 
# Funcao que comanda o anel de LEDs em animacao de giroflex com efeito estroboscopico
 
# e o buzzer (se estiver ativa a sirene)
 
def giroflex_com_estrobo():
 
    global giroflex_com_estrobo_ligado
 
    j=0
 
    tempo_desde_ultima_mudanca = utime.ticks_ms()
 
    buzzer.freq(500)
 
    proximoMultiplicador = 3
 
    while(giroflex_com_estrobo_ligado):
 
        if sirene_ligada:
 
            duty = 32767
 
        else:
 
            duty = 65535
 
        buzzer.duty_u16(duty)
 
        for i in range(12):
 
            if ((i+j)%12)//6 < 1:
 
                ws.write(i,0xFF0000)
 
            elif ((i+j)%12)//6 == 1:
 
                ws.write(i,0X0000FF)
 
        if ((utime.ticks_ms() - tempo_desde_ultima_mudanca > 300)):       
 
            buzzer.freq(500*proximoMultiplicador)
 
            if proximoMultiplicador == 3:
 
                proximoMultiplicador = 1
 
            else:
 
                proximoMultiplicador = 3
 
            tempo_desde_ultima_mudanca = utime.ticks_ms()            
 
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
 
        if j == 2000000000:
 
            j=0
 
        j+=1
 
        utime.sleep_ms(20)
 
    ws.write_all(0x000000)
 
    buzzer.duty_u16(65535)
 
     
 
# Funcao que comanda o buzzer caso os giroflex nao estejam ligados em simultaneo
 
def sirene():
 
    if sirene_ligada:
 
        duty = 32767
 
    else:
 
        duty = 65535
 
    buzzer.duty_u16(duty)
 
    while sirene_ligada and not giroflex_com_estrobo_ligado and not giroflex_simples_ligado:
 
            buzzer.freq(500)
 
            utime.sleep_ms(40)
 
            buzzer.freq(100)
 
            utime.sleep_ms(40)
 
            buzzer.freq(500)
 
            utime.sleep_ms(40)
 
            buzzer.freq(100)
 
            utime.sleep_ms(40)
 
            buzzer.freq(500)
 
            utime.sleep_ms(40)
 
            buzzer.freq(100)
 
            utime.sleep_ms(40)
 
            buzzer.freq(500)
 
            utime.sleep_ms(40)
 
            buzzer.freq(100)
 
            utime.sleep_ms(40)
 
    buzzer.duty_u16(65535)
 
# Funcao que sera executada no segundo nucleo da pico W em paralelo a do nucelo principal 
 
def nucleo_secundario():
 
    # Laco de execucao do nucleo secundario    
 
    while True:        
 
        giroflex_simples()
 
        giroflex_com_estrobo()
 
        sirene()
 
# Inicializacao da nova rotina no nucelo secundario e espera para que ela inicie com sucesso    
 
_thread.start_new_thread(nucleo_secundario,())
 
utime.sleep(0.25)
 
# Laco de execucao
 
while True:    
 
    estado_botao_1 = botao_1.value()
 
    estado_botao_2 = botao_2.value()
 
    estado_botao_3 = botao_3.value()
 
    estado_botao_4 = botao_4.value()
 
    if estado_botao_1 == 1:
 
        if giroflex_simples_ligado:
 
            giroflex_simples_ligado = False
 
        elif giroflex_com_estrobo_ligado:
 
            giroflex_com_estrobo_ligado = False
 
            giroflex_simples_ligado = True
 
        else:
 
            giroflex_simples_ligado = True
 
    elif estado_botao_2 == 1:
 
        if giroflex_com_estrobo_ligado:
 
            giroflex_com_estrobo_ligado = False
 
        elif giroflex_simples_ligado:
 
            giroflex_com_estrobo_ligado = True
 
            giroflex_simples_ligado = False
 
        else:
 
            giroflex_com_estrobo_ligado = True
 
    elif estado_botao_3 == 1:
 
        sirene_ligada = not sirene_ligada
 
    elif estado_botao_4 == 1:
 
        giroflex_com_estrobo_ligado = False
 
        giroflex_simples_ligado = False
 
        sirene_ligada = False
 
    utime.sleep(0.2)
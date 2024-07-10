# Codigo 10.3 - Fazendo musica
 
# Bibliotecas necessarias para o codigo
 
# Importacao das bibliotecas padrao
 
import machine
 
import utime
 
# Declaracao do buzzer
 
buzzer = machine.PWM(machine.Pin(14, machine.Pin.OUT))
 
# Declaracao dos botoes
 
botao_1 = machine.Pin(21, machine.Pin.IN)
 
botao_2 = machine.Pin(20, machine.Pin.IN)
 
botao_3 = machine.Pin(19, machine.Pin.IN)
 
botao_4 = machine.Pin(18, machine.Pin.IN)
 
# Definicao das variaveis do codigo
 
NOTA_C4 =  262
 
NOTA_D4 =  294
 
NOTA_E4 =  330
 
NOTA_F4 =  349
 
estado_botao_1 = 0
 
estado_botao_2 = 0
 
estado_botao_3 = 0
 
estado_botao_4 = 0
 
# Laco de execucao
 
while True:
 
    estado_botao_1 = botao_1.value()
 
    estado_botao_2 = botao_2.value()
 
    estado_botao_3 = botao_3.value()
 
    estado_botao_4 = botao_4.value()
 
    valor = (estado_botao_1 << 3) + (estado_botao_2 << 2) + (estado_botao_3 << 1) + estado_botao_4   
 
    if valor == 0:
 
        buzzer.freq(100)
 
        buzzer.duty_u16(65535)
 
    elif valor == 1:
 
        buzzer.freq(NOTA_C4)
 
        buzzer.duty_u16(32767)
 
        utime.sleep_ms(100)
 
    elif valor == 2:
 
        buzzer.freq(NOTA_D4)
 
        buzzer.duty_u16(32767)
 
        utime.sleep_ms(100)
 
    elif valor == 4:
 
        buzzer.freq(NOTA_E4)
 
        buzzer.duty_u16(32767)
 
        utime.sleep_ms(100)
 
    elif valor == 8:
 
        buzzer.freq(NOTA_F4)
 
        buzzer.duty_u16(32767)
 
        utime.sleep_ms(100)
 
    else:
 
        buzzer.duty_u16(65535)
 
    utime.sleep(0.01)
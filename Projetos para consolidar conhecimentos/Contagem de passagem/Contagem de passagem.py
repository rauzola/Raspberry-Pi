# Codigo 14.3 - Contagem de passagem
 
# Bibliotecas necessarias para o codigo
 
# Importacao das bibliotecas padrao
 
import machine
 
import utime
 
# Importacao das bibliotecas customizadas 
 
import LCD
 
from colour import colour
 
# Declaracao do LCD
 
display = LCD.LCD_1inch3()
 
# Declaracao do sensor de movimento PIR
 
pir_sensor = machine.Pin(19, machine.Pin.IN)
 
# Declaracao das variaveis
 
numero_de_movimentacoes = 0
 
atualiza_display = False
 
# Funcao chamada ao concluir a deteccao de uma movimentacao pelo sensor
 
def movimento_detectado(_):
 
    global numero_de_movimentacoes
 
    global atualiza_display
 
    numero_de_movimentacoes += 1
 
    atualiza_display = True
 
# Declaracao da interrupcao que sera iniciadas ao encerrar a deteccao de uma movimentacao
 
# pelo sensor
 
pir_sensor.irq(trigger=machine.Pin.IRQ_FALLING, handler=movimento_detectado)
 
# Exibicao das informacoes que permanecerao fixas no display
 
display.fill(colour(0,0,0))
 
display.printstring('Contagem de',22,30,3,0,0,colour(244,255,113))
 
display.printstring('pessoas',60,70,3,0,0,colour(244,255,113))
 
display.show()
 
atualiza_display = True
 
# Laco de execucao
 
while True:
 
    if atualiza_display:
 
        display.fill_rect(100,120,240,40,colour(0,0,0))
 
        if numero_de_movimentacoes < 10:
 
            display.printstring('{}'.format(numero_de_movimentacoes),112,120,3,1,0,colour(244,255,113))
 
        elif numero_de_movimentacoes >= 10 and numero_de_movimentacoes < 100:
 
            display.printstring('{}'.format(numero_de_movimentacoes),105,120,3,1,0,colour(244,255,113))
 
        elif numero_de_movimentacoes > 10 and numero_de_movimentacoes < 1000:
 
            display.printstring('{}'.format(numero_de_movimentacoes),95,120,3,1,0,colour(244,255,113))
 
        else:
 
            display.printstring('{}'.format(numero_de_movimentacoes),85,120,3,1,0,colour(244,255,113))
 
        atualiza_display = False
 
    utime.sleep(0.1)
# Codigo 13.3 - Reagindo a sons
 
# Bibliotecas necessarias para o codigo
 
# Importacao das bibliotecas padrao
 
import machine
 
import utime
 
# Importacao das bibliotecas customizadas 
 
from ws2812 import WS2812
 
from colour import *
 
# Declaracao do microfone
 
mic = machine.ADC(26)
 
# Declaracao da fita de LEDs
 
ws = WS2812(machine.Pin(28), 12)
 
# Captacao do ruido ambiente
 
ruido_ambiente = []
 
for i in range(100):
 
    ruido_ambiente.append(mic.read_u16())
 
    utime.sleep(0.001)
 
# Laco de execucao
 
while True:
 
    leitura = mic.read_u16()
 
    if leitura > max(ruido_ambiente) or leitura < min(ruido_ambiente):
 
        leitura = leitura*(4096)/((65535)+4096)
 
        leitura = round(leitura)
 
        brilho = abs((leitura-2048)/2048)
 
        brilho = round(brilho,2)
 
        if brilho < 0.33:
 
            ws.write_all([0,0,round(255*brilho)])
 
        elif brilho >= 0.33 and brilho < 0.66:
 
            ws.write_all([0,round(255*brilho),0])  
 
        else:
 
            ws.write_all([round(255*brilho),0,0])
 
    else:
 
        ws.write_all([0,0,0])
 
    utime.sleep(.05)
# Codigo 13.2 - Acendendo uma luminaria com sons

# Bibliotecas necessarias para o codigo

# Importacao das bibliotecas padrao
import machine
import utime

# Importacao das bibliotecas customizadas 
from ws2812 import WS2812

# Declaracao do Anel de LEDs
ws = WS2812(machine.Pin(28), 12)

# Declaracao do microfone
mic = machine.ADC(26)

# Declaracao das variaveis
ultima_palma = 0
uma_palma = False
duas_palmas = False
leds_ligados = False

# Le uma media de 100 amostras do ruido ambiente e faz uma media
ambient_noise = sum(mic.read_u16() for _ in range(100)) / 100

# Laco de execucao
while True:
    if ultima_palma == 0:
        ultima_palma = utime.ticks_ms()

    # Verifica se o som detectado é uma palma
    if mic.read_u16() > ambient_noise * 1.8:
        print('uma palma')
        # Verifica se a segunda palma foi dentro do intervalo de 400 ms
        if (utime.ticks_ms() - ultima_palma < 400):
            duas_palmas = True
            print('duas palmas')
        else:
            uma_palma = True
        ultima_palma = utime.ticks_ms()

    if duas_palmas:
        # Desliga os LEDs ao detectar duas palmas
        ws.write_all(0x000000)
        leds_ligados = False
        duas_palmas = False
        uma_palma = False
    elif uma_palma:
        # Liga os LEDs ao detectar uma palma
        ws.write_all(0xFFFFFF)
        leds_ligados = True
        uma_palma = False

    utime.sleep(0.1)

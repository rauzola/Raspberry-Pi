# Codigo 9.2 - Higrometro Luminoso
 
# Bibliotecas necessarias para o codigo
 
# Importacao das bibliotecas padrao
 
from machine import Pin, I2C
 
import utime
 
# Importacao das bibliotecas customizadas 
 
from dht import DHT11
 
from ws2812 import WS2812
 
# Declaracao do Anel de LEDs
 
ws = WS2812(machine.Pin(28), 12)
 
# Declaracao do Sensor de temperatura e umidade
 
pin = Pin(13, Pin.IN, Pin.PULL_UP)
 
sensor = DHT11(pin)
 
# Atraso inicial para inicializacao do sensor
 
utime.sleep(5)  
 
# Saida que nao sofrera alteracao no console
 
print('Dados do sensor:')
 
# Laco de execucao
 
while True:
 
    try:
 
        sensor.measure()
        temperatura = sensor.temperature()
        umidade = sensor.humidity()
 
    except:
 
        temperatura = 'err'
 
        umidade = 'err'
 
    string = "Temperatura:{}°C Umidade: {}%".format(temperatura, umidade)
 
    print("\r",string,end='')
 
    if umidade <= 10:
 
        ws.write(0,0xFF0000)
 
        for i in range(1,12):
 
            ws.write(i,0x000000)
 
    elif umidade <= 18:
 
        for i in range(2):
 
            ws.write(i, 0xFF0000)
 
        for i in range(2,12):
 
            ws.write(i,0x000000)
 
    elif umidade <= 26:
 
        for i in range(3):
 
            ws.write(i, 0xFF0000)
 
        for i in range(3,12):
 
            ws.write(i,0x000000)
 
    elif umidade <= 34:
 
        for i in range(4):
 
            ws.write(i, 0xFF3300)
 
        for i in range(4,12):
 
            ws.write(i,0x000000)
 
    elif umidade <= 42:
 
        for i in range(5):
 
            ws.write(i, 0xFFAA00)
 
        for i in range(5,12):
 
            ws.write(i,0x000000)
 
    elif umidade <= 50:
 
        for i in range(6):
 
            ws.write(i, 0xBBBB00)
 
        for i in range(6,12):
 
            ws.write(i,0x000000)
 
    elif umidade <= 58:
 
        for i in range(7):
 
            ws.write(i, 0x00FF00)
 
        for i in range(7,12):
 
            ws.write(i,0x000000)
 
    elif umidade <= 66:
 
        for i in range(8):
 
            ws.write(i, 0x00FF00)
 
        for i in range(8,12):
 
            ws.write(i,0x000000)
 
    elif umidade <= 72:
 
        for i in range(9):
 
            ws.write(i, 0x00FFFF)
 
        for i in range(9,12):
 
            ws.write(i,0x000000)
 
    elif umidade <= 80:
 
        for i in range(10):
 
            ws.write(i, 0x0055FF)
 
        for i in range(10,12):
 
            ws.write(i,0x000000)
 
    elif umidade <= 88:
 
        for i in range(11):
 
            ws.write(i, 0x0000FF)
 
        for i in range(11,12):
 
            ws.write(i, 0x000000)
 
    elif umidade <= 90:
 
            ws.write_all(0x0000FF)
 
    utime.sleep(4)
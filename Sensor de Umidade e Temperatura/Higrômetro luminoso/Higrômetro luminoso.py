from machine import Pin
import time
from dht import DHT11
from ws2812 import WS2812

# Inicializa o sensor DHT11, conectando-o ao pino 16 do microcontrolador.
sensor = DHT11(Pin(16, Pin.OUT, Pin.PULL_DOWN))

# Inicializa o anel de LEDs, conectando-o ao pino 28 do microcontrolador.
ws = WS2812(Pin(28), 12)

# Função para atualizar o anel de LEDs com base na umidade.
def atualizar_leds(umidade):
    if umidade <= 10:
        ws.write(0, 0xFF0000)
        for i in range(1, 12):
            ws.write(i, 0x000000)
    elif umidade <= 18:
        for i in range(2):
            ws.write(i, 0xFF0000)
        for i in range(2, 12):
            ws.write(i, 0x000000)
    elif umidade <= 26:
        for i in range(3):
            ws.write(i, 0xFF0000)
        for i in range(3, 12):
            ws.write(i, 0x000000)
    elif umidade <= 34:
        for i in range(4):
            ws.write(i, 0xFF3300)
        for i in range(4, 12):
            ws.write(i, 0x000000)
    elif umidade <= 42:
        for i in range(5):
            ws.write(i, 0xFFAA00)
        for i in range(5, 12):
            ws.write(i, 0x000000)
    elif umidade <= 50:
        for i in range(6):
            ws.write(i, 0xBBBB00)
        for i in range(6, 12):
            ws.write(i, 0x000000)
    elif umidade <= 58:
        for i in range(7):
            ws.write(i, 0x00FF00)
        for i in range(7, 12):
            ws.write(i, 0x000000)
    elif umidade <= 66:
        for i in range(8):
            ws.write(i, 0x00FF00)
        for i in range(8, 12):
            ws.write(i, 0x000000)
    elif umidade <= 72:
        for i in range(9):
            ws.write(i, 0x00FFFF)
        for i in range(9, 12):
            ws.write(i, 0x000000)
    elif umidade <= 80:
        for i in range(10):
            ws.write(i, 0x0055FF)
        for i in range(10, 12):
            ws.write(i, 0x000000)
    elif umidade <= 88:
        for i in range(11):
            ws.write(i, 0x0000FF)
        for i in range(11, 12):
            ws.write(i, 0x000000)
    elif umidade <= 90:
        ws.write_all(0x0000FF)
    else:
        ws.write_all(0x0000FF)

# Loop infinito para ler os valores do sensor continuamente.
while True:
    try:
        # Tenta ler a temperatura e a umidade do sensor.
        temp = sensor.temperature
        humidity = sensor.humidity
        # Imprime os valores de temperatura e umidade lidos do sensor.
        print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, humidity))
        # Atualiza o anel de LEDs com base na umidade lida.
        atualizar_leds(humidity)
    except Exception as e:
        # Captura qualquer exceção que ocorra durante a leitura dos valores do sensor.
        print("Error reading sensor:", e)
        # Reinicia o loop em caso de erro, ignorando o restante do código no bloco while.
        continue
        
    # Aguarda 2 segundos antes de fazer a próxima leitura.
    time.sleep(2)

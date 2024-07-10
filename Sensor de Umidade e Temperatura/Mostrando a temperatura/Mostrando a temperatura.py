from machine import Pin
import time
from dht import DHT11

# Inicializa o sensor DHT11, conectando-o ao pino 16 do microcontrolador.
sensor = DHT11(Pin(16, Pin.OUT, Pin.PULL_DOWN))

# Loop infinito para ler os valores do sensor continuamente.
while True:
    try:
        # Tenta ler a temperatura do sensor.
        temp = sensor.temperature
        # Tenta ler a umidade do sensor.
        humidity = sensor.humidity
        # Imprime os valores de temperatura e umidade lidos do sensor.
        print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, humidity))
    except Exception as e:
        # Captura qualquer exceção que ocorra durante a leitura dos valores do sensor.
        print("Error reading sensor:", e)
        # Reinicia o loop em caso de erro, ignorando o restante do código no bloco while.
        continue
        
    # Aguarda 2 segundos antes de fazer a próxima leitura.
    time.sleep(2)

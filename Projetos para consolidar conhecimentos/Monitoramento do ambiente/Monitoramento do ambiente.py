# Bibliotecas necessárias para o código
from machine import Pin, ADC
import utime
import LCD
from colour import colour
from dht import DHT11

# Declaração do LCD
LCD = LCD.LCD_1inch3()

# Declaração do sensor de temperatura e umidade
sensor = DHT11(Pin(16, Pin.OUT, Pin.PULL_DOWN))

# Declaração do foto resistor
foto_resistor = ADC(26)
valor_de_baixa_luminosidade = 65535
valor_de_alta_luminosidade = 0

utime.sleep(5)  # Atraso para a inicialização correta do sensor

# Laço de execução
while True:
    valor_luminosidade = foto_resistor.read_u16()
    porcentagem_iluminacao = ((valor_de_baixa_luminosidade - valor_luminosidade) / valor_de_baixa_luminosidade) * 100
    
    try:
        # Tenta ler a temperatura do sensor.
        temp = sensor.temperature
        # Tenta ler a umidade do sensor.
        humidity = sensor.humidity
        # Imprime os valores de temperatura, umidade e luminosidade lidos do sensor.
        print("Temperatura: {}°C  Umidade: {:.0f}%  Luminosidade: {:.1f}%".format(temp, humidity, porcentagem_iluminacao))
    except Exception as e:
        # Captura qualquer exceção que ocorra durante a leitura dos valores do sensor.
        print("Erro ao ler o sensor:", e)
        # Reinicia o loop em caso de erro, ignorando o restante do código no bloco while.
        continue
    
    string_temp = "Temp: {}C".format(temp)
    string_umid = "Umi : {}%".format(humidity)
    string_lumi = "Luz : {}%".format(round(porcentagem_iluminacao, 1))
    
    # Limpa as áreas onde o texto será atualizado
    LCD.fill_rect(17, 30, 200, 40, colour(40, 40, 40))  # Limpa a área da temperatura
    LCD.fill_rect(17, 80, 200, 40, colour(40, 40, 40))  # Limpa a área da umidade
    LCD.fill_rect(17, 120, 200, 40, colour(40, 40, 40))  # Limpa a área da luminosidade
    
    # Desenha o texto nas áreas limpas
    LCD.printstring(string_temp, 17, 30, 3, 0, 0, colour(244, 255, 113))
    LCD.printstring(string_umid, 17, 80, 3, 0, 0, colour(244, 255, 113))
    LCD.printstring(string_lumi, 17, 120, 3, 0, 0, colour(244, 255, 133))
    LCD.show()
    
    utime.sleep(1)  # Aguarda 1 segundo antes de fazer a próxima leitura

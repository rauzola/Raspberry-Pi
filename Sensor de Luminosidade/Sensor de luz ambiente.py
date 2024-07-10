# Codigo 8.2 - Sensor de luz ambiente

# Bibliotecas necessarias para o codigo

# Importacao das bibliotecas padrao
import machine  # Biblioteca para controle do hardware
import utime  # Biblioteca para funções de tempo

# Declaracao do LDR (Light Dependent Resistor)
ldr = machine.ADC(28)  # Define o pino 28 como entrada para o LDR

# Declaracao do LED
led = machine.Pin(15, machine.Pin.OUT)  # Define o pino 15 como saída para o LED

# Definição dos limites de histerese
limite_superior = 21000  # Limite superior para ligar o LED
limite_inferior = 19000  # Limite inferior para desligar o LED

# Estado inicial do LED
led_ligado = False

# Laco de execucao
while True:
    # Lê o valor de luminosidade do LDR
    valor_de_luminosidade = ldr.read_u16()  # Lê o valor analógico (0 a 65535)

    # Verifica se o valor de luminosidade está acima do limite superior
    if valor_de_luminosidade > limite_superior and not led_ligado:
        led.value(1)  # Liga o LED
        led_ligado = True  # Atualiza o estado do LED

    # Verifica se o valor de luminosidade está abaixo do limite inferior
    elif valor_de_luminosidade < limite_inferior and led_ligado:
        led.value(0)  # Desliga o LED
        led_ligado = False  # Atualiza o estado do LED

    utime.sleep_ms(10)  # Espera por 10 milissegundos antes de repetir o loop

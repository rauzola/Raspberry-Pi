# Codigo 7.2 - Detector de movimento

# Bibliotecas necessarias para o codigo

# Importacao das bibliotecas padrao
import machine  # Biblioteca para controle do hardware
import utime  # Biblioteca para funções de tempo

# Declaracao do sensor PIR
sensor_pir = machine.Pin(19, machine.Pin.IN)  # Define o pino 19 como entrada para o sensor PIR

# Declaracao do LED
led = machine.Pin(15, machine.Pin.OUT)  # Define o pino 15 como saída para o LED

# Declaracao das variaveis do codigo
movimento = False  # Inicializa a variável para armazenar o estado do movimento

# Funcao a ser chamada quando houver uma borda positiva no pino do sensor PIR
def movimento_detectado(_):
    global movimento  # Declara a variável movimento como global para poder modificá-la
    movimento = True  # Define movimento como True quando uma interrupção é detectada

# Declaracao da interrupcao no pino do sensor PIR
sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=movimento_detectado)  # Configura uma interrupção na borda de subida

# Laco de execucao
while True:
    if movimento:  # Verifica se foi detectado movimento
        led.value(1)  # Liga o LED
        print("Alguem passou aqui!")  # Imprime uma mensagem no console
        utime.sleep(3)  # Aguarda 3 segundos
        led.value(0)  # Desliga o LED
        movimento = False  # Reseta a variável movimento para False
    utime.sleep(0.01)  # Reduz o tempo de espera no loop principal para 10 milissegundos

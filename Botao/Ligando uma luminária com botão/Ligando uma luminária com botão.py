# Codigo 6.2 - Ligando luminaria com botao

# Bibliotecas necessarias para o codigo

# Importacao das bibliotecas padrao

import machine  # Biblioteca para controle do hardware
import utime  # Biblioteca para funções de tempo

# Importacao das bibliotecas customizadas

from ws2812 import WS2812  # Biblioteca para controle dos LEDs WS2812

# Declaracao do Anel de LEDs

ws = WS2812(machine.Pin(28), 12)  # Cria objeto 'ws' para controlar 12 LEDs no pino 28

# Declaracao dos botoes

botao_1 = machine.Pin(18, machine.Pin.IN)  # Define o pino 18 como entrada para o botão 1
botao_2 = machine.Pin(19, machine.Pin.IN)  # Define o pino 19 como entrada para o botão 2
botao_3 = machine.Pin(20, machine.Pin.IN)  # Define o pino 20 como entrada para o botão 3
botao_4 = machine.Pin(21, machine.Pin.IN)  # Define o pino 21 como entrada para o botão 4

# Declaracao das variaveis do codigo

estado_botao_1 = 0  # Inicializa a variável para armazenar o estado do botão 1
estado_botao_2 = 0  # Inicializa a variável para armazenar o estado do botão 2
estado_botao_3 = 0  # Inicializa a variável para armazenar o estado do botão 3
estado_botao_4 = 0  # Inicializa a variável para armazenar o estado do botão 4

# Laco de execucao

while True:
    # Lê o estado de cada botão
    estado_botao_1 = botao_1.value()  # Lê o estado do botão 1
    estado_botao_2 = botao_2.value()  # Lê o estado do botão 2
    estado_botao_3 = botao_3.value()  # Lê o estado do botão 3
    estado_botao_4 = botao_4.value()  # Lê o estado do botão 4

    # Verifica qual botão está pressionado e define a cor dos LEDs
    if estado_botao_1 == 1:
        ws.write_all(0x444444)  # Define uma cor cinza escura para todos os LEDs
    elif estado_botao_2 == 1:
        ws.write_all(0x888888)  # Define uma cor cinza média para todos os LEDs
    elif estado_botao_3 == 1:
        ws.write_all(0xFFFFFF)  # Define a cor branca para todos os LEDs
    elif estado_botao_4 == 1:
        ws.write_all(0x000000)  # Desliga todos os LEDs

    ws.send()  # Envia a nova configuração de cor para o anel de LEDs

    utime.sleep(0.01)  # Espera por 10 milissegundos antes de repetir o loop

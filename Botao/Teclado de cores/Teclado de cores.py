# Codigo 6.3 - Teclado de Cores

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

# Declaracao das variaveis

estado_botao_1 = 0  # Inicializa a variável para armazenar o estado do botão 1
estado_botao_2 = 0  # Inicializa a variável para armazenar o estado do botão 2
estado_botao_3 = 0  # Inicializa a variável para armazenar o estado do botão 3
estado_botao_4 = 0  # Inicializa a variável para armazenar o estado do botão 4

azul_ligado = False  # Variável para controlar se a cor azul está ligada
branco_ligado = False  # Variável para controlar se a cor branca está ligada
verde_ligado = False  # Variável para controlar se a cor verde está ligada
vermelho_ligado = False  # Variável para controlar se a cor vermelha está ligada

# Laco de execucao

while True:
    # Lê o estado de cada botão
    estado_botao_1 = botao_1.value()  # Lê o estado do botão 1
    estado_botao_2 = botao_2.value()  # Lê o estado do botão 2
    estado_botao_3 = botao_3.value()  # Lê o estado do botão 3
    estado_botao_4 = botao_4.value()  # Lê o estado do botão 4

    # Verifica qual botão está pressionado e altera a cor dos LEDs
    if estado_botao_1 == 1:
        if not vermelho_ligado:
            ws.write_all(0xFF0000)  # Define a cor vermelha para todos os LEDs
            azul_ligado = False
            branco_ligado = False
            verde_ligado = False
            vermelho_ligado = True
        else:
            ws.write_all(0x000000)  # Desliga todos os LEDs
            azul_ligado = False
            branco_ligado = False
            verde_ligado = False
            vermelho_ligado = False

    elif estado_botao_2 == 1:
        if not verde_ligado:
            ws.write_all(0x00FF00)  # Define a cor verde para todos os LEDs
            azul_ligado = False
            branco_ligado = False
            verde_ligado = True
            vermelho_ligado = False
        else:
            ws.write_all(0x000000)  # Desliga todos os LEDs
            azul_ligado = False
            branco_ligado = False
            verde_ligado = False
            vermelho_ligado = False

    elif estado_botao_3 == 1:
        if not azul_ligado:
            ws.write_all(0x0000FF)  # Define a cor azul para todos os LEDs
            azul_ligado = True
            branco_ligado = False
            verde_ligado = False
            vermelho_ligado = False
        else:
            ws.write_all(0x000000)  # Desliga todos os LEDs
            azul_ligado = False
            branco_ligado = False
            verde_ligado = False
            vermelho_ligado = False

    elif estado_botao_4 == 1:
        if not branco_ligado:
            ws.write_all(0xFFFFFF)  # Define a cor branca para todos os LEDs
            azul_ligado = False
            branco_ligado = True
            verde_ligado = False
            vermelho_ligado = False
        else:
            ws.write_all(0x000000)  # Desliga todos os LEDs
            azul_ligado = False
            branco_ligado = False
            verde_ligado = False
            vermelho_ligado = False

    ws.send()  # Envia a nova configuração de cor para o anel de LEDs
    utime.sleep(0.2)  # Espera por 200 milissegundos antes de repetir o loop

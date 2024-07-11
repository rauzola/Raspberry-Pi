# Código 14.4 - Jukebox

# Bibliotecas necessárias para o código

# Importação das bibliotecas padrão
from machine import Pin, PWM  # Bibliotecas para controle de pinos e PWM (Pulse Width Modulation)
import utime  # Biblioteca para controle de tempo

# Importação das bibliotecas customizadas
from melodias import *  # Biblioteca que contém as melodias

# Declaração do buzzer
buzzer = PWM(Pin(14))  # Inicializa o buzzer no pino 14 com controle PWM
buzzer.freq(1000)  # Define a frequência inicial do buzzer
buzzer.duty_u16(65535)  # Define a intensidade do som do buzzer

# Declaração dos botões
botao_1 = machine.Pin(18, machine.Pin.IN)  # Inicializa o botão 1 no pino 18 como entrada
botao_2 = machine.Pin(19, machine.Pin.IN)  # Inicializa o botão 2 no pino 19 como entrada
botao_3 = machine.Pin(20, machine.Pin.IN)  # Inicializa o botão 3 no pino 20 como entrada
botao_4 = machine.Pin(21, machine.Pin.IN)  # Inicializa o botão 4 no pino 21 como entrada

# Declaração das variáveis
tocar_musica = False  # Flag para indicar se uma música está sendo tocada
estado_botao_1 = 0  # Estado inicial do botão 1
estado_botao_2 = 0  # Estado inicial do botão 2
estado_botao_3 = 0  # Estado inicial do botão 3
estado_botao_4 = 0  # Estado inicial do botão 4

# Laço de execução
while True:
    # Leitura do estado dos botões
    estado_botao_1 = botao_1.value()  # Atualiza o estado do botão 1
    estado_botao_2 = botao_2.value()  # Atualiza o estado do botão 2
    estado_botao_3 = botao_3.value()  # Atualiza o estado do botão 3
    estado_botao_4 = botao_4.value()  # Atualiza o estado do botão 4

    # Verifica se o botão 1 foi pressionado
    if estado_botao_1 == 1:
        play(buzzer, musicas["pinkpanther"])  # Toca a música "Pink Panther"

    # Verifica se o botão 2 foi pressionado
    elif estado_botao_2 == 1:
        play(buzzer, musicas["nevergonnagiveyouup"])  # Toca a música "Never Gonna Give You Up"

    # Verifica se o botão 3 foi pressionado
    elif estado_botao_3 == 1:
        play(buzzer, musicas["starwars"])  # Toca a música "Star Wars"

    # Verifica se o botão 4 foi pressionado
    elif estado_botao_4 == 1:
        play(buzzer, musicas["thelionesleepstonight"])  # Toca a música "The Lion Sleeps Tonight"

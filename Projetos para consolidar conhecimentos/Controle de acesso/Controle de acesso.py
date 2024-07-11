# Código 14.5 - Controle de acesso

# Bibliotecas necessárias para o código

# Importação das bibliotecas padrão
import machine
import utime
import _thread

# Importação das bibliotecas customizadas
from mfrc522 import SimpleMFRC522  # Biblioteca para leitura RFID
import LCD  # Biblioteca para controle do LCD
from colour import colour  # Biblioteca para manipulação de cores no LCD

# Declaração do LCD
display = LCD.LCD_1inch3()  # Inicializa o display LCD

# Declaração do leitor RFID
reader = SimpleMFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=5, rst=0)  # Inicializa o leitor RFID com os pinos especificados

# Declaração dos botões
botao_1 = machine.Pin(18, machine.Pin.IN)  # Inicializa o botão 1 no pino 18 como entrada
botao_2 = machine.Pin(19, machine.Pin.IN)  # Inicializa o botão 2 no pino 19 como entrada
botao_3 = machine.Pin(20, machine.Pin.IN)  # Inicializa o botão 3 no pino 20 como entrada
botao_4 = machine.Pin(21, machine.Pin.IN)  # Inicializa o botão 4 no pino 21 como entrada

# Declaração das variáveis
entrando_senha = False  # Flag para indicar se o usuário está inserindo a senha
contador_digitos_inseridos = 0  # Contador de dígitos inseridos
contador_digitos_anterior = 0  # Contador de dígitos inseridos anteriormente
tecla_pressionada = 0  # Armazena a última tecla pressionada
tempo_ultimo_toque = 0  # Armazena o tempo do último toque
tempo_ultima_liberacao = 0  # Armazena o tempo da última liberação de acesso
tempo_ultima_leitura = 0  # Armazena o tempo da última leitura do cartão
tempo_ultima_atualizacao_display = 0  # Armazena o tempo da última atualização do display
inicia_cadastro = False  # Flag para indicar se o cadastro de um novo cartão foi iniciado
cartao_liberado = [-1]  # Armazena o ID do cartão liberado
cartao_lido = [-1]  # Armazena o ID do cartão lido
senha_cadastro = [1, 2, 3, 4]  # Senha de cadastro padrão
senha_acesso = [4, 3, 2, 1]  # Senha de acesso padrão
senha_digitada = ['', '', '', '']  # Armazena os dígitos da senha digitada

# Função chamada ao apertar o botão 1
def button_1_isr(pin):
    global tempo_ultimo_toque  # Usa a variável global
    if not utime.ticks_ms() - tempo_ultimo_toque < 200:  # Evita múltiplos toques rápidos
        global entrando_senha
        if entrando_senha:  # Se está inserindo a senha
            global tecla_pressionada
            tecla_pressionada = 1  # Armazena o valor da tecla pressionada
            global contador_digitos_inseridos
            contador_digitos_inseridos += 1  # Incrementa o contador de dígitos
        else:
            entrando_senha = True  # Inicia a inserção da senha
            tecla_pressionada = 1
            contador_digitos_inseridos += 1
        tempo_ultimo_toque = utime.ticks_ms()  # Atualiza o tempo do último toque

# Função chamada ao apertar o botão 2
def button_2_isr(pin):
    global tempo_ultimo_toque
    if not utime.ticks_ms() - tempo_ultimo_toque < 200:
        global entrando_senha
        if entrando_senha:
            global tecla_pressionada
            tecla_pressionada = 2
            global contador_digitos_inseridos
            contador_digitos_inseridos += 1
        else:
            entrando_senha = True
            tecla_pressionada = 2
            contador_digitos_inseridos += 1
        tempo_ultimo_toque = utime.ticks_ms()

# Função chamada ao apertar o botão 3
def button_3_isr(pin):
    global tempo_ultimo_toque
    if not utime.ticks_ms() - tempo_ultimo_toque < 200:
        global entrando_senha
        if entrando_senha:
            global tecla_pressionada
            tecla_pressionada = 3
            global contador_digitos_inseridos
            contador_digitos_inseridos += 1
        else:
            entrando_senha = True
            tecla_pressionada = 3
            contador_digitos_inseridos += 1
        tempo_ultimo_toque = utime.ticks_ms()

# Função chamada ao apertar o botão 4
def button_4_isr(pin):
    global tempo_ultimo_toque
    if not utime.ticks_ms() - tempo_ultimo_toque < 200:
        global entrando_senha
        if entrando_senha:
            global tecla_pressionada
            tecla_pressionada = 4
            global contador_digitos_inseridos
            contador_digitos_inseridos += 1
        else:
            entrando_senha = True
            tecla_pressionada = 4
            contador_digitos_inseridos += 1
        tempo_ultimo_toque = utime.ticks_ms()

# Declaração das interrupções que serão iniciadas ao toque dos botões
botao_1.irq(trigger=botao_1.IRQ_FALLING, handler=button_1_isr)  # Interrupção para o botão 1
botao_2.irq(trigger=botao_2.IRQ_FALLING, handler=button_2_isr)  # Interrupção para o botão 2
botao_3.irq(trigger=botao_3.IRQ_FALLING, handler=button_3_isr)  # Interrupção para o botão 3
botao_4.irq(trigger=botao_4.IRQ_FALLING, handler=button_4_isr)  # Interrupção para o botão 4

# Função que realiza o cadastro do cartão
def cadastra_cartao(cartao_lido):
    global cartao_liberado
    global inicia_cadastro
    global tempo_ultima_atualizacao_display
    if cartao_lido[0] != -1:  # Se um cartão foi lido
        print(cartao_lido[0])
        cartao_liberado[0] = cartao_lido[0]  # Armazena o ID do cartão liberado
        cartao_lido[0] = -1  # Reseta o ID do cartão lido
        display.fill(colour(0, 255, 0))  # Preenche o display com cor verde
        display.printstring('Cartao', 45, 30, 3, 0, 0, colour(0, 0, 0))  # Imprime "Cartao" no display
        display.printstring('Cadastrado!', 20, 90, 3, 0, 0, colour(0, 0, 0))  # Imprime "Cadastrado!" no display
        display.show()
        print("Cartão cadastrado!")
        inicia_cadastro = False  # Finaliza o cadastro
        tempo_ultima_atualizacao_display = utime.ticks_ms()  # Atualiza o tempo da última atualização do display

# Função que nega o acesso a cartões ou senhas não autorizadas
def barra_acesso():
    global tempo_ultima_atualizacao_display
    display.fill(colour(255, 0, 0))  # Preenche o display com cor vermelha
    display.printstring("Acesso", 60, 60, 3, 0, 0, colour(0, 0, 0))  # Imprime "Acesso" no display
    display.printstring("negado!", 57, 120, 3, 0, 0, colour(0, 0, 0))  # Imprime "negado!" no display
    display.show()
    print("Acesso negado!")
    tempo_ultima_atualizacao_display = utime.ticks_ms()  # Atualiza o tempo da última atualização do display

# Função que libera o acesso a cartões ou senhas autorizados
def libera_acesso():
    global cartao_lido
    global tempo_ultima_liberacao
    global tempo_ultima_atualizacao_display
    cartao_lido[0] = -1  # Reseta o ID do cartão lido
    display.fill(colour(0, 255, 0))  # Preenche o display com cor verde
    display.printstring("Acesso", 60, 60, 3, 0, 0, colour(128, 128, 128))  # Imprime "Acesso" no display
    display.printstring("liberado!", 47, 120, 3, 0, 0, colour(128, 128, 128))  # Imprime "liberado!" no display
    display.show()
    print("Acesso liberado!")
    tempo_ultima_liberacao = tempo_ultima_atualizacao_display = utime.ticks_ms()  # Atualiza os tempos de última liberação e atualização do display

# Função que será executada no segundo núcleo da pico W em paralelo ao do núcleo principal
def nucleo_secundario():
    global cartao_lido
    global contador_digitos_inseridos
    global contador_digitos_anterior
    global senha_cadastro
    global senha_acesso
    global senha_digitada
    global entrando_senha
    global cartao_liberado
    global inicia_cadastro
    global tempo_ultima_atualizacao_display

    # Laço de execução do núcleo secundário
    while True:
        if not inicia_cadastro and utime.ticks_ms() - tempo_ultima_atualizacao_display > 1000:
            display.fill(colour(244, 255, 113))  # Preenche o display com cor amarela
            display.printstring('Controle', 45, 30, 3, 0, 0, colour(0, 0, 0))  # Imprime "Controle" no display
            display.printstring('de', 100, 90, 3, 0, 0, colour(0, 0, 0))  # Imprime "de" no display
            display.printstring('Acesso', 65, 150, 3, 0, 0, colour(0, 0, 0))  # Imprime "Acesso" no display
            display.show()

        if entrando_senha and utime.ticks_ms() - tempo_ultimo_toque < 10000:
            if contador_digitos_inseridos < 4 and contador_digitos_inseridos > contador_digitos_anterior:
                senha_digitada[contador_digitos_inseridos - 1] = tecla_pressionada  # Armazena a tecla pressionada na posição correta da senha
                contador_digitos_anterior = contador_digitos_inseridos
            elif contador_digitos_inseridos == 4:
                senha_digitada[contador_digitos_inseridos - 1] = tecla_pressionada
                if senha_digitada == senha_cadastro:
                    print("Aproxime o cartão")
                    display.fill(colour(0, 133, 220))  # Preenche o display com cor azul
                    display.printstring('Aproxime', 45, 30, 3, 0, 0, colour(255, 255, 255))  # Imprime "Aproxime" no display
                    display.printstring('o', 105, 90, 3, 0, 0, colour(255, 255, 255))  # Imprime "o" no display
                    display.printstring('cartao', 60, 150, 3, 0, 0, colour(255, 255, 255))  # Imprime "cartao" no display
                    display.show()
                    tempo_ultima_atualizacao_display = utime.ticks_ms()
                    inicia_cadastro = True
                    contador_digitos_inseridos = 0
                    contador_digitos_anterior = 0
                    entrando_senha = False
                    senha_digitada = ['', '', '', '']
                elif senha_digitada == senha_acesso:
                    libera_acesso()
                    contador_digitos_inseridos = 0
                    contador_digitos_anterior = 0
                    entrando_senha = False
                    senha_digitada = ['', '', '', '']
                else:
                    barra_acesso()
                    contador_digitos_inseridos = 0
                    contador_digitos_anterior = 0
                    entrando_senha = False
                    senha_digitada = ['', '', '', '']

        elif entrando_senha:
            contador_digitos_inseridos = 0
            contador_digitos_anterior = 0
            entrando_senha = False
            senha_digitada = ['', '', '', '']

        if not inicia_cadastro and (cartao_lido[0] == cartao_liberado[0] and cartao_liberado[0] != -1 and utime.ticks_ms() - tempo_ultima_liberacao > 1000):
            libera_acesso()
        elif not inicia_cadastro and cartao_lido[0] != cartao_liberado[0] and cartao_lido[0] != -1:
            barra_acesso()
            cartao_lido[0] = -1

        utime.sleep(0.1)

# Inicialização da nova rotina no núcleo secundário e espera para que ela inicie com sucesso
_thread.start_new_thread(nucleo_secundario, ())
utime.sleep(0.25)

# Laço de execução
while True:
    if inicia_cadastro:
        cartao_lido[0] = reader.read_id()
        tempo_ultima_leitura = utime.ticks_ms()
        cadastra_cartao(cartao_lido)
    elif utime.ticks_ms() - tempo_ultima_leitura > 1000:
        cartao_lido[0] = reader.read_id()
        tempo_ultima_leitura = utime.ticks_ms()
    utime.sleep(0.1)

# Codigo 15.6 - Comunicando por MQTT
 
# Bibliotecas necessarias para o codigo
 
# Importacao das bibliotecas padrao
 
import time
 
from machine import Pin
 
import mip
 
import os
 
# Importacao das bibliotecas customizadas 
 
from realiza_conexao import realiza_conexao

# Realiza a conexao Wi-Fi
 
# Precisamos fazer ela logo no comeco pois a biblioteca mip utiliza a internet
 
# para buscar repositorios e instalar outras bibliotecas
 
realiza_conexao()
 
# Verifica se a biblioteca umqtt esta instalada
 
# se nao estiver, realiza a instalacao atraves do gerenciador de pacotes
 
try:
 
    os.stat('/lib/umqtt')
 
except:
 
    mip.install('umqtt.simple')
 
     
 
# Importa o MQTTClient da biblioteca umqtt.simple
 
from umqtt.simple import MQTTClient
 
# Declaracao dos botoes
 
botao1 = Pin(18, Pin.IN)
 
botao2 = Pin(19, Pin.IN)
 
botao3 = Pin(20, Pin.IN)
 
botao4 = Pin(21, Pin.IN)
 
# Declaracao das variaveis
 
servidor_mqtt = 'broker.hivemq.com'
 
id_de_cliente = 'teste'
 
meu_topico = 'Kit Maker Raspberry Pi Exemplo MQTT'
 
topico = b'' + meu_topico 
 
# Tenta realizar a conexao com o Broker MQTT, caso nao consiga
 
# aguarda 5 segundos e reseta o microcontrolador para tentar novamente
 
try:
 
    client = MQTTClient(id_de_cliente, servidor_mqtt, keepalive=3600)
 
    client.connect()
 
    print('Conectado ao Broker MQTT %s'%(servidor_mqtt))
 
except OSError as e:
 
    print('Erro ao conectar ao Broker MQTT. Reconectando...')
 
    time.sleep(5)
 
    machine.reset()
 
# Define uma funcao para tratar a interrupcao do aperto de cada botao
 
# e declara a respectiva interrupcao logo abaixo
 
def apertou1(pin):
 
    mensagem = b'O botao 1 foi apertado'
 
    client.publish(topico, mensagem)
 
    print(mensagem)
 
botao1.irq(trigger=machine.Pin.IRQ_RISING, handler=apertou1)
 
def apertou2(pin):
 
    mensagem = b'O botao 2 foi apertado'
 
    client.publish(topico, mensagem)
 
    print(mensagem)
 
botao2.irq(trigger=machine.Pin.IRQ_RISING, handler=apertou2)
 
def apertou3(pin):
 
    mensagem = b'O botao 3 foi apertado'
 
    client.publish(topico, mensagem)
 
    print(mensagem)
 
botao3.irq(trigger=machine.Pin.IRQ_RISING, handler=apertou3)
 
def apertou4(pin):
 
    mensagem = b'O botao 4 foi apertado'
 
    client.publish(topico, mensagem)
 
    print(mensagem)
 
botao4.irq(trigger=machine.Pin.IRQ_RISING, handler=apertou4)
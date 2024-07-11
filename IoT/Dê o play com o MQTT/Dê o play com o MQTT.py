# Codigo 15.7 - De o Play com MQTT
 
# Bibliotecas necessarias para o codigo
 
# Importacao das bibliotecas padrao
 
import time
 
from machine import Pin,PWM
 
import mip
 
import os
 
# Importacao das bibliotecas customizadas 
 
from realiza_conexao import *
 
from melodias import *
 
# Realiza a conexao Wi-Fi
 
# Precisamos fazer ela logo no comeco pois a biblioteca mip utiliza a internet
 
# para buscar repositorios e instalar outras bibliotecas
 
realiza_conexao()
 
# Verifica se a biblioteca umqtt esta instalada
 
# se nao estiver, realiza a instalacao
 
try:
 
    os.stat('/lib/umqtt')
 
except:
 
    mip.install('umqtt.simple')
 
 
# Importa o MQTTClient da biblioteca umqtt.simple
 
from umqtt.simple import MQTTClient
 
# Declaracao do Buzzer
 
buzzer = PWM(Pin(14))
 
buzzer.duty_u16(65535)
 
# Declaracao das variaveis
 
tocar_musica = False
 
servidor_mqtt = 'broker.hivemq.com'
 
id_de_cliente = 'teste'
 
meu_topico = 'Kit Maker Raspberry Pi Exemplo MQTT'
 
topico = b'' + meu_topico 
 
# Funcao que recebe e decodifica as mensagens enviadas por MQTT
 
# e toca a musica correspondente, se existir na biblioteca de melodias
 
def callback(topico, message):
 
    print("Nova mensagem no topico {}:".format(topico.decode('utf-8')))
 
    message = message.decode('utf-8')
 
    print(message)
 
    if message in musicas.keys():
 
        global melodia,tocar_musica
 
        melodia = musicas[message]
 
        tocar_musica = True
 
# Tenta realizar a conexao com o Broker MQTT, caso nao consiga
 
# aguarda 5 segundos e reseta o microcontrolador para tentar novamente
 
try:
 
    client = MQTTClient(id_de_cliente, servidor_mqtt, keepalive=60)
 
    client.set_callback(callback)
 
    client.connect()
 
    print('Conectado ao broker MQTT %s'%(servidor_mqtt))
 
    client.subscribe(topico)
 
except OSError as e:
 
    print('Erro ao conectar ao broker MQTT. Reconectando...')
 
    time.sleep(5)
 
    machine.reset()
 
# Laco de execucao
 
while True:
 
    try:
 
        client.check_msg()
 
    except:
 
        client.disconnect()
 
        client.connect()
 
        client.subscribe(topico)
 
    time.sleep(1)
 
    if tocar_musica is True:
 
        play(buzzer,melodia)
 
        tocar_musica = False
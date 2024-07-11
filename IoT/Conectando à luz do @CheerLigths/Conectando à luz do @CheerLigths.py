import urequests  # Importa o módulo urequests para fazer requisições HTTP
import json       # Importa o módulo json para lidar com dados JSON
import time       # Importa o módulo time para manipular tempo e pausas
import machine    # Importa o módulo machine para acessar funções do hardware
from ws2812 import WS2812  # Importa a classe WS2812 do módulo ws2812
from realiza_conexao import realiza_conexao  # Importa a função realiza_conexao do arquivo realiza_conexao.py

ip = realiza_conexao()  # Chama a função realiza_conexao para obter o endereço IP do dispositivo

print('IP: ', ip)  # Imprime o endereço IP obtido na linha anterior

ws = WS2812(machine.Pin(28), 12)  # Inicializa o objeto WS2812 para controlar LEDs conectados ao pino 28 (GPIO28) com 12 LEDs

def get_colour():
    url = "http://api.thingspeak.com/channels/1417/field/2/last.json"
    # Define a URL da qual os dados serão obtidos
    
    try:
        r = urequests.get(url)  # Realiza uma requisição GET para obter os dados da URL
        
        if r.status_code > 199 and r.status_code < 300:
            # Verifica se a resposta HTTP está dentro da faixa de sucesso (200-299)
            
            cheerlights = json.loads(r.content.decode('utf-8'))
            # Converte o conteúdo da resposta (JSON) em um objeto Python
            
            print(cheerlights['field2'])  # Imprime o valor do campo 'field2' dos dados recebidos
            
            colour = int('0x' + cheerlights['field2'][1:7])
            # Extrai o valor da cor (hexadecimal) do campo 'field2' e converte para um número inteiro
            
            r.close()  # Fecha a conexão após receber os dados
            
            return colour  # Retorna o valor da cor obtida
            
        else:
            print('Erro HTTP:', r.status_code)  # Imprime o código de erro HTTP, se houver
            
            return None  # Retorna None se ocorrer um erro HTTP
        
    except Exception as e:
        print(e)  # Imprime qualquer exceção capturada durante a execução do bloco try-except
        
        return None  # Retorna None se ocorrer uma exceção

while True:
    colour = get_colour()  # Chama a função get_colour para obter a cor atual
    
    if colour is not None:
        ws.write_all(colour)  # Define a cor dos LEDs para a cor obtida
    
    time.sleep(60)  # Aguarda 60 segundos antes de obter a cor novamente

# Código 15.5 - Criando um servidor WEB

# Bibliotecas necessárias para o código

# Importação das bibliotecas padrão
from machine import ADC, Pin  # Importa as classes ADC e Pin do módulo machine
import socket  # Importa o módulo socket para comunicação de rede

# Importação das bibliotecas customizadas
from realiza_conexao import realiza_conexao  # Importa a função realiza_conexao do arquivo realiza_conexao.py

led = machine.Pin("LED", machine.Pin.OUT)  # Define o pino "LED" como saída para controle do LED

sensor_de_temperatura = ADC(4)  # Inicializa o sensor de temperatura no pino ADC 4

def le_temperatura_interna():
    # Função para ler a temperatura interna do sensor

    valor_adc = sensor_de_temperatura.read_u16()  # Lê o valor bruto do ADC
    tensao = valor_adc * (3.3 / 65535.0)  # Converte o valor do ADC em tensão
    temperatura_celsius = 27 - (tensao - 0.706) / 0.001721  # Calcula a temperatura em graus Celsius

    return temperatura_celsius  # Retorna a temperatura medida em graus Celsius

def abre_socket(ip):
    # Função para abrir um socket de rede
    
    endereco = (ip, 80)  # Define o endereço IP e a porta 80
    conexao = socket.socket()  # Cria um objeto de socket
    
    conexao.bind(endereco)  # Associa o socket ao endereço IP e porta especificados
    conexao.listen(1)  # Coloca o socket em modo de escuta para aceitar conexões
    
    return conexao  # Retorna o objeto de conexão do socket

def pagina_web(temperatura, estado):
    # Função para gerar a página HTML dinâmica com base nos parâmetros temperatura e estado
    
    # Estrutura HTML
    html = f"""
        <!DOCTYPE html>
        <html>
            <body>
                <form action="./ligaled">
                    <input type="submit" value="Liga LED" />
                </form>
                <form action="./desligaled">
                    <input type="submit" value="Desliga LED" />
                </form>
                <p>O LED está {estado}</p>
                <p>A temperatura é {temperatura}</p>
            </body>
        </html>
        """
    
    return str(html)  # Retorna o HTML como uma string

def roda_servidor(conexao):
    # Função para rodar o servidor WEB
    
    estado = 'Desligado'  # Define o estado inicial do LED como desligado
    led.off()  # Garante que o LED esteja desligado inicialmente
    temperatura = 0  # Inicializa a temperatura como zero
    
    while True:
        # Aceita a conexão do cliente
        cliente = conexao.accept()[0]
        
        # Recebe a requisição em bytes
        requisicao = cliente.recv(1024)
        
        # Converte a requisição em string para processamento
        requisicao = str(requisicao)
        
        try:
            # Divide a string usando espaço como separador e pega o elemento 1 do array
            requisicao = requisicao.split()[1]
        except IndexError:
            pass
        
        if requisicao == '/ligaled?':
            led.on()  # Liga o LED
            estado = 'Ligado'  # Atualiza o estado do LED
        elif requisicao == '/desligaled?':
            led.off()  # Desliga o LED
            estado = 'Desligado'  # Atualiza o estado do LED
        
        temperatura = le_temperatura_interna()  # Atualiza a temperatura lendo o sensor
        
        html = pagina_web(temperatura, estado)  # Gera a página HTML dinâmica
        
        cliente.send(html)  # Envia a página HTML como resposta ao cliente
        
        cliente.close()  # Fecha a conexão com o cliente

# Executa as funções para conectar à rede, abrir o socket e rodar o servidor
try:
    ip = realiza_conexao()  # Obtém o endereço IP após conectar à rede
    conexao = abre_socket(ip)  # Abre o socket de rede com o endereço IP obtido
    roda_servidor(conexao)  # Inicia o servidor WEB utilizando o socket aberto
    
except:
    machine.reset()  # Reinicia o dispositivo em caso de erro

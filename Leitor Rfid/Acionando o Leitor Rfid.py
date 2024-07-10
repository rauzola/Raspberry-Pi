# Codigo 12.2 - Acionando o leitor RFID

# Bibliotecas necessarias para o codigo

# Importacao das bibliotecas padrao
import utime  # Biblioteca padrão para funções relacionadas ao tempo

# Importacao das bibliotecas customizadas
from mfrc522 import SimpleMFRC522  # Biblioteca customizada para controle do leitor RFID MFRC522

# Declaracao do leitor RFID
reader = SimpleMFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=5, rst=0)  # Inicializa uma instância do leitor RFID MFRC522 com a configuração dos pinos SPI

# Funcao que realiza a leitura do cartao e printa o ID no terminal
def realiza_leitura():    
    print("Lendo... Aproxime o cartao...")  # Mensagem para o usuário
    id, text = reader.read()  # Realiza a leitura do cartão RFID e armazena o ID e texto lido
    print("ID do cartao: %s\nText: %s" % (id, text))  # Imprime o ID e o texto lido no terminal

# Laco de execucao
while True:
    realiza_leitura()  # Chama a função de leitura do cartão RFID
    utime.sleep(1)  # Espera por 1 segundo antes de realizar a próxima leitura

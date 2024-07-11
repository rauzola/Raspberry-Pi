import network
import time

def realiza_conexao():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("MGP-EDIMAR", "edimar2990")

    # Espera por até 10 segundos pela conexão Wi-Fi
    wait = 10
    while wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        wait -= 1
        print('Aguardando conexao...')
        time.sleep(1)

    # Verifica o status da conexão após a espera
    if wlan.status() != 3:
        raise RuntimeError('A conexao falhou')
    else:
        print('Conectado')
        ip = wlan.ifconfig()[0]
        print('IP:', ip)
        return ip

# Chama a função para realizar a conexão
wlan_ip = realiza_conexao()



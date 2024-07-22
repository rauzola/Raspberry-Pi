from hcsr04 import HCSR04
from time import sleep

# Função para inicializar o sensor ultrassônico
def init_ultrasonic(trigger_pin, echo_pin, echo_timeout_us=10000):
    return HCSR04(trigger_pin=trigger_pin, echo_pin=echo_pin, echo_timeout_us=echo_timeout_us)

# Função para ler a distância do sensor ultrassônico
def get_distance(sensor):
    try:
        distance = sensor.distance_cm()
        return distance
    except Exception as e:
        print('Erro ao ler a distância do sensor ultrassônico:', e)
        return None

# Função principal
def main():
    sensor = init_ultrasonic(trigger_pin=2, echo_pin=3)
    
    while True:
        distance = get_distance(sensor)
        if distance is not None:
            print('Distance:', distance, 'cm')
        else:
            print('Falha ao obter a distância.')
        sleep(1)

# Chamada da função principal
if __name__ == "__main__":
    main()

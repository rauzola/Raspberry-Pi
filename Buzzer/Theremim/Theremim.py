# Codigo 10.4 - Theremin
 
# Bibliotecas necessarias para o codigo
 
# Importacao das bibliotecas padrao
 
import machine
 
import utime
 
# Declaracao do LED
 
led = machine.Pin(16, machine.Pin.OUT)
 
# Declaracao do LDR
 
LDR = machine.ADC(28)
 
# Declaracao do buzzer
 
buzzer = machine.PWM(machine.Pin(14))
 
# Declaracao das variaveis do codigo
 
pouca_luz=3000
 
muita_luz=55000
 
# Funcao que mapeia um intervalo de valores para outro
 
def mapeamento_de_intervalo(x, in_min, in_max, out_min, out_max):    
 
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
# Definicao do ciclo de trabalho do PWM
 
buzzer.duty_u16(30000)
 
# Laco de execucao
 
while True:
 
    valor_de_luminosidade  = LDR.read_u16()
 
    frequencia = int(mapeamento_de_intervalo(valor_de_luminosidade,pouca_luz,muita_luz,50,6000))
 
    buzzer.freq(frequencia)
 
    utime.sleep_ms(10)
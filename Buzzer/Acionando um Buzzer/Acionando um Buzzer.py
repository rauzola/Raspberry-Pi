# Codigo 10.2 - Acionando um buzzer
 
# Bibliotecas necessarias para o codigo
 
# Importacao das bibliotecas padrao
 
import machine
 
import utime
 
# Declaracao do buzzer
 
buzzer = machine.PWM(machine.Pin(14))
 
# Definicao da frequencia do PWM e periodo que aciona o buzzer
 
buzzer.freq(6000)
 
buzzer.duty_u16(30000)
from machine import Pin
from machine import PWM
from time import sleep
 
# Classe para controle de servomotor
class Servo:
 
    # Iniciação
    def __init__(self, pino):
        self.FREQ = 50
        self.pwm = PWM (Pin(pino))
        self.pwm.freq(self.FREQ)
        self.ultpos = 0
        self.duty = 0
        self.pwm.duty_u16(0)
        self.min = 1
        self.max = 2
 
    # Envia n pulsos com tempo t em ms
    def enviaPulsos(self, t, nPulsos=20):
        self.duty = int(t*65.535*self.FREQ)
        self.pwm.duty_u16(self.duty)
        sleep (nPulsos/self.FREQ)
        self.pwm.duty_u16(0)
        #print ("-> "+str(t)+" "+str(self.duty))
         
    # Informa/Muda posição
    # angulo deve estar entre 0 e 180 graus
    def pos(self, ang = None):
        if ang is None:
            return self.ultpos
        elif (ang >= 0) or (ang <= 180):
                self.ultpos = ang
                t = self.min + (180 - ang)*(self.max-self.min)/180
                self.enviaPulsos(t)
                 
    # Informa/muda tempo (em ms) para colocar na posição 180 graus
    def tempoFim (self, val = None):
        if (val == None):
            return self.min
        else:
            self.min = val
 
    # Informa/muda tempo (em ms) para colocar na posição 0 graus
    def tempoInicio(self, val = None):
        if (val == None):
            return self.max
        else:
            self.max = val
             
print ('Demonstração do controle de servomotor')
print ('* Entre com um valor entre 0.5 e 2.5 para posicionar')
print ('* A para definir o tempo para 0 graus')
print ('* Z para definir o tempo para 180 graus')
print ('* G para mover automaticamente')
servo = Servo(0)
tempo = 0.0
while True:
    val = input('Comando: ')
    if ((val == 'A') or (val == 'a')) and (tempo != 0.0) and \
       (tempo > servo.tempoFim()):
        servo.tempoInicio(tempo)
        print ('Novo tempo para 0 graus: '+str(tempo))
    elif ((val == 'Z') or (val == 'z')) and (tempo != 0.0) and \
       (tempo < servo.tempoInicio()):
        servo.tempoFim(tempo)
        print ('Novo tempo para 180 graus: '+str(tempo))
    elif ((val == 'G') or (val == 'g')):
        break
    else:
        try:
            tempo = float(val)
            if (tempo >= 0.5) and (tempo <= 2.5):
                servo.enviaPulsos(tempo)
            else:
                print ('Tempo precisa estar entre 0.5 e 2.5')
        except:
            print('Valor inválido')
print ('Entrando em modo automático')
while True:
    for angulo in range(0, 180, 10):
        servo.pos(angulo)
    for angulo in range(180, 0, -10):
        servo.pos(angulo)
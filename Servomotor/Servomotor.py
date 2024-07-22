from machine import Pin, PWM
from time import sleep

# Classe para controle de servomotor
class Servo:
    def __init__(self, pin):
        self.FREQ = 50
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(self.FREQ)
        self.ultpos = 0
        self.duty = 0
        self.pwm.duty_u16(0)
        self.min = 1
        self.max = 2

    # Envia n pulsos com tempo t em ms
    def enviaPulsos(self, t, nPulsos=20):
        self.duty = int(t * 65.535 * self.FREQ)
        self.pwm.duty_u16(self.duty)
        sleep(nPulsos / self.FREQ)
        self.pwm.duty_u16(0)

    # Informa/Muda posição (ângulo entre 0 e 180 graus)
    def pos(self, ang=None):
        if ang is None:
            return self.ultpos
        elif 0 <= ang <= 180:
            self.ultpos = ang
            t = self.min + (180 - ang) * (self.max - self.min) / 180
            self.enviaPulsos(t)

    # Informa/muda tempo (em ms) para colocar na posição 180 graus
    def tempoFim(self, val=None):
        if val is None:
            return self.min
        else:
            self.min = val

    # Informa/muda tempo (em ms) para colocar na posição 0 graus
    def tempoInicio(self, val=None):
        if val is None:
            return self.max
        else:
            self.max = val

# Função principal
def main():
    print('Demonstração do controle de servomotor')
    print('* Entre com um valor entre 0.5 e 2.5 para posicionar')
    print('* A para definir o tempo para 0 graus')
    print('* Z para definir o tempo para 180 graus')
    print('* G para mover automaticamente')
    
    servo = Servo(0)
    tempo = 0.0
    
    while True:
        val = input('Comando: ')
        
        if val.lower() == 'a' and tempo != 0.0 and tempo > servo.tempoFim():
            servo.tempoInicio(tempo)
            print('Novo tempo para 0 graus: ' + str(tempo))
        elif val.lower() == 'z' and tempo != 0.0 and tempo < servo.tempoInicio():
            servo.tempoFim(tempo)
            print('Novo tempo para 180 graus: ' + str(tempo))
        elif val.lower() == 'g':
            break
        else:
            try:
                tempo = float(val)
                if 0.5 <= tempo <= 2.5:
                    servo.enviaPulsos(tempo)
                else:
                    print('Tempo precisa estar entre 0.5 e 2.5')
            except ValueError:
                print('Valor inválido')
    
    print('Entrando em modo automático')
    while True:
        for angulo in range(0, 181, 10):
            servo.pos(angulo)
        for angulo in range(180, -1, -10):
            servo.pos(angulo)

# Chamada da função principal
if __name__ == "__main__":
    main()

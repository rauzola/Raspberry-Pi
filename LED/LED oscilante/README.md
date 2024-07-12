# LED oscilante

## Kit Maker Raspberry Pi

### LED - LED oscilante

Até agora, usamos apenas dois sinais de saída: nível alto e nível baixo (também chamados de ON e OFF), que é chamado de saída digital. No entanto, na utilização real, muitos dispositivos não se limitam a LIGAR/DESLIGAR para funcionar, por exemplo, ajustando a velocidade do motor, ajustando o brilho da lâmpada de mesa, e assim por diante. Para atingir esse objetivo a modulação por largura de pulso (PWM) surgiu como uma solução viável para problemas tão complexos.

Um pulso é uma saída digital que contém um nível alto e um nível baixo. A largura de pulso desses pinos pode ser ajustada alterando a velocidade ON/OFF.

Quando estivermos em um curto período de tempo (como 20ms, que é o período de retenção visual da maioria das pessoas), deixar o LED acender, desligar e ligar novamente, não veremos que ele foi desligado, mas sim o brilho da luz será ligeiramente mais fraca. Durante este período, quanto mais tempo o LED estiver aceso, mais brilhante ele se tornará. Em outras palavras, no ciclo, quanto mais amplo o pulso, maior será a “intensidade do sinal elétrico” emitida pelo microcontrolador. É assim que o PWM controla o brilho do LED (ou a velocidade do motor). 

![Pisca Pisca GIF](https://github.com/rauzola/Raspberry-Pi/blob/main/LED/LED%20oscilante/5.4LEDoscilante1920x1080-ezgif.com-video-to-gif-converter.gif)


Há alguns pontos a serem observados quando o Pico W usa PWM. Vamos dar uma olhada nesta imagem.

![raspberry-pi-pico-w-pinout](https://raw.githubusercontent.com/rauzola/Raspberry-Pi/main/LED/LED%20oscilante/raspberry-pi-pico-w-pinout-1024x671.png.webp)

A Pico W suporta PWM em cada pino GPIO, mas na verdade existem 16 saídas PWM independentes (em vez de 30), distribuídas entre GP0 a GP15 à esquerda, e a saída PWM do GPIO direito é idêntica à esquerda.

É importante evitar configurar o mesmo canal PWM para finalidades diferentes durante a programação. Por exemplo, GP0 e GP16 são ambos PWM_0A.

Vamos tentar obter o efeito de LED desbotado depois de compreender esse conhecimento.

## Materiais Necessários

Neste projeto, precisamos dos seguintes componentes:

- Placa Raspberry Pi Pico W
- Cabo USB
- Protoboard 400 pontos
- Jumper macho-macho
- LED Vermelho 5mm
- Resistor 220 ohm

## Circuito

Este projeto possui o mesmo circuito do primeiro projeto 5.3 Pisca-Pisca, mas o tipo de sinal é diferente. O primeiro projeto é emitir níveis altos e baixos digitais (0 e 1) diretamente do GP15 para fazer os LEDs acenderem ou desligarem. Este projeto é para emitir o sinal PWM do GP15 para controlar o brilho do LED.

![Circuito](https://raw.githubusercontent.com/rauzola/Raspberry-Pi/main/LED/LED%20oscilante/5-3-Pisca-Pisca_bb-1.png.webp)

## Programa

Vamos utilizar as mesmas bibliotecas do projeto anterior do 5.3 Pisca Pisca, que faz o controle do led.  Aqui, alteramos o brilho do LED alterando o ciclo de trabalho da saída PWM do GP15. 

O brilho do LED em PWM é controlado pelo controle da largura do pulso, que é a quantidade de tempo que o LED fica aceso a cada ciclo. Com uma frequência de temporizador de 100 Hz, cada ciclo leva 0,01 segundo, ou 10 ms.

Para obter o efeito de desbotamento mostrado no início deste tutorial, queremos definir a extensão do pulso para um valor pequeno, depois aumentar lentamente a extensão do pulso para iluminar o LED e recomeçar quando atingirmos o brilho máximo.

Vamos dar uma olhada no código completo abaixo:

```python
import machine
 
import utime
 
led = machine.PWM(machine.Pin(15))
 
led.freq(1000)
 
for brilho in range(0,65535,50):
 
   led.duty_u16(brilho)
 
   utime.sleep_ms(10)
 
led.duty_u16(0)
```

 - A linha led = machine.PWM(machine.Pin(15)) define o pino GP15 como saída PWM.
 - A linha led.freq(1000) é usada para definir a frequência PWM, aqui ela é configurada para 1000Hz, o que significa que 1ms (1/1000) é um ciclo.
 - a linha for brightness in range(0,65535,50): itera a variável brightness
 - A linha led.duty_u16() é usada para definir o ciclo de trabalho, que é um número inteiro de 16 bits (2 ^ 16 = 65536). Um 0 indica ciclo de trabalho de 0%, o que significa que cada ciclo tem 0% de tempo para gerar um nível alto, ou seja, o sinal fica desligado durante todo o ciclo. O valor 65535 indica um ciclo de trabalho de 100%, o que significa que o sinal está ativado durante todo o ciclo, e o resultado é ‘1’. Quando for 32768 (metade do valor) , ele ficará em nível alto durante metade do ciclo, então o LED terá metade do brilho quando estiver totalmente ligado.

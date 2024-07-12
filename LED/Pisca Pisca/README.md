# Pisca Pisca

## Kit Maker Raspberry Pi

### 5. LED 5.3 Pisca Pisca

Assim como imprimir “Olá, mundo!” é o primeiro passo para aprender a programar com uma IDE, usar um programa para acionar um LED é a introdução tradicional ao aprendizado de programação e eletrônica.

Agora que conhecemos o funcionamento do resistor e do LED, em nosso primeiro exemplo prático iremos fazer uma luz piscar. Parece um exercício simples demais, mas isso exemplifica a utilização da placa Raspberry Pi Pico W para controle de dispositivos externos. Os conceitos aprendidos neste exemplo servem para acionamento de outros dispositivos como ventilador, lâmpadas, motores e etc.

Esse é o primeiro projeto que será um pequeno grande passo para que você aprenda eletrônica e programação e possa fazer exercícios mais complexos.

## Materiais Necessários

Em todos os exercícios e projetos teremos uma seção que mostra os componentes que iremos utilizar. Se você tiver alguma dúvida sobre qual é o componente, você pode voltar na lista de materiais:

- Placa Raspberry Pi Pico W
- Cabo USB
- Protoboard 400 pontos
- Jumper macho-macho
- LED Vermelho 5mm
- Resistor 220 ohm

## Circuito

No esquema da montagem do circuito, as linhas coloridas são a representação gráfica dos jumpers. Utilize-os para ligar os componentes entre si conforme a ilustração abaixo: 

Nesse exemplo, após a programação da placa, o LED acende quando a fonte de energia (que nesse caso é o pino de saída da Pico W) é ligada e ao desligar a fonte de energia, o LED apagará. O resistor é colocado para reduzir a corrente que passa pelo circuito inteiro.

Para construir o circuito, vamos seguir o sentido da corrente!

- O LED é alimentado pelo pino GP15 da placa Pico W, e o circuito começa aqui.
- Para proteger o LED, a corrente deve passar por um resistor de 220 ohms. Um terminal do resistor deve ser inserido na mesma linha do pino Pico W GP15, e o outro terminal deve ser inserido na linha livre da protoboard.

**Observação:** Os anéis coloridos do resistor de 220 ohms são vermelho, vermelho, preto, preto e marrom.

Se você olhar o LED, verá que um de seus terminais é mais longo que o outro. Conecte o terminal mais longo à mesma fileira do resistor e o fio mais curto à mesma fileira no espaço intermediário da protoboard.

**Observação:** O terminal do LED mais longo é o ânodo, que representa o lado positivo do circuito; já o terminal curto é o cátodo, que representa o lado negativo.

O ânodo precisa ser conectado ao pino GPIO através de um resistor; o cátodo precisa ser conectado ao pino GND.

- Usando um fio jumper macho-macho, conecte o pino curto do LED ao barramento de alimentação negativo da protoboard.
- Conecte o pino GND da Pico W ao barramento de alimentação negativo usando um jumper.

Não é necessário conectar os componentes exatamente nos mesmos furos como indicado acima, basta apenas que os terminais de cada componente não estejam na mesma coluna. 

## Programa

Primeiramente vamos explicar o código em partes e logo mais abaixo você verá o programa completo. Ao fim da explicação você pode copiar o código completo e colar na sua IDE Thonny.

A biblioteca que será usada neste projeto é a `machine`, que será necessária para usar as portas GPIO. Essa biblioteca já faz parte do pacote de bibliotecas básicas do MicroPython que instalamos na IDE Thonny, portanto ao escrever o nome dela diretamente no código, ela já estará funcionando. 

```python
import machine
```
A biblioteca contém todas as instruções necessárias para a comunicação entre MicroPython e a Pico W. Na ausência desta linha de código, não poderemos controlar nenhum GPIO.

A próxima que temos que prestar atenção é esta linha:

```python
led = machine.Pin(15, machine.Pin.OUT)
```

O objeto led é definido aqui. Tecnicamente, pode ser qualquer nome, como x, y, banana, ou qualquer personagem. Para garantir que o programa seja fácil de ler, é melhor usar um nome que descreva a finalidade.

Na segunda parte desta linha (a parte após o sinal de igual), chamamos a função Pin, encontrada na biblioteca machine. É usada para informar aos pinos GPIO da Pico o que fazer.

A função Pin possui dois parâmetros:

O primeiro (15) representa o pino a ser configurado.
O segundo parâmetro (machine.Pin.OUT) especifica que o pino deve ser de saída em vez de entrada.
O código acima “configurou” o pino, mas não acenderá o LED. Para fazer isso, também precisamos “usar” o pino, ou seja, dizer qual função ele fará.

```python
led.value(1)
```

O pino GP15 foi configurado anteriormente e denominado led. A função desta instrução é definir o valor de led como 1 para acender o LED.

Resumindo, para usar o GPIO, estas etapas são necessárias:

Importar biblioteca da máquina: isso é necessário e só é executado uma vez.
Definir GPIO: Antes de usar, cada pino deve ser definido.
Uso: Altere o estado de funcionamento do pino atribuindo um valor a ele.
Se seguirmos as etapas acima para escrever um exemplo, você obterá um código como este:

```python
import machine

led = machine.Pin(15, machine.Pin.OUT)

led.value(1)
```

Execute-o e você poderá acender o LED.

A seguir, tentamos adicionar a declaração oposta, ou seja LED desligado:

```python
import machine

led = machine.Pin(15, machine.Pin.OUT)

led.value(1)

led.value(0)
```

Com base na linha de código, este programa acenderá primeiro o LED e depois o apagará. Mas ao usá-lo, você descobrirá que não é esse o caso, pois não vemos o LED aceso. Isto se deve à velocidade de execução muito rápida entre as duas linhas, muito mais rápida do que o olho humano pode reagir. Quando o LED acende, não percebemos a luz instantaneamente. Isso pode ser corrigido desacelerando o programa.

A segunda linha do programa deve conter a seguinte instrução:

```python
import utime
```

Da mesma forma que machine, a biblioteca utime é importada aqui, que trata de todas as coisas relacionadas ao tempo. Os atrasos que precisamos usar estão incluídos nisso. Adicione uma instrução de atraso entre led.value(1) e led.value(0) deixe-os separados por 2 segundos.

```python
utime.sleep(2)
```

É assim que o código deve ficar agora. Veremos que o LED acende primeiro e depois apaga quando o executamos:

```python
import machine
import utime

led = machine.Pin(15, machine.Pin.OUT)

led.value(1)
utime.sleep(2)
led.value(0)
```

Finalmente, devemos fazer o LED piscar. Vamos criar um laço para repetir infinitamente a parte que queremos do programa com o laço while. Coloque as linhas que você quer que repitam após adicionar a linha while True: Todas as linhas que serão repetidas devem ser identadas (espaçadas com tab). Esse espaçamento determina todas as linhas de código que serão englobadas pelo laço de repetição. Abaixo você terá o código completo para copiar e colar na IDE:


```python
import machine
import utime

led = machine.Pin(15, machine.Pin.OUT)

while True:
    led.value(1)
    utime.sleep(2)
    led.value(0)
    utime.sleep(2)
```
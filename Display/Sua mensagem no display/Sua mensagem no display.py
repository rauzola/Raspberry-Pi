# Codigo 11.2 - Sua mensagem no display

# Importacao das bibliotecas padrao
import utime  # Biblioteca padrão para funções relacionadas ao tempo

# Importacao das bibliotecas customizadas
import LCD  # Biblioteca customizada para controle do display LCD

from colour import colour  # Biblioteca customizada para manipulação de cores

# Declaracao do LCD
display = LCD.LCD_1inch3()  # Inicializa uma instância do display LCD de 1 polegada e 3

# Preenche o fundo do display com preto e escreve 'Oi, mundo!' em verde partindo das coordenadas 20 px e 10 px
display.fill(colour(0,0,0))  # Preenche o fundo do display com a cor preta (RGB: 0, 0, 0)

display.printstring('Oi, mundo!',24,30,3,0,0,colour(0,255,0))  # Escreve a string 'Oi, mundo!' no display com a cor verde (RGB: 0, 255, 0) nas coordenadas (24, 30) e com tamanho de fonte 3

display.show()  # Atualiza o display para mostrar as mudanças feitas


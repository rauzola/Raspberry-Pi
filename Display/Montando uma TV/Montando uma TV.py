# Codigo 11.3 - Montando uma TV
 
# Bibliotecas necessarias para o codigo
 
# Importacao das bibliotecas padrao
 
import utime
import array
import os
import sys
 
# Importacao das bibliotecas customizadas 
 
import LCD
from colour import colour
 
# Declaracao do LCD
 
display = LCD.LCD_1inch3()
 
# Declaracao dos arrays de coordenadas para o logo da MakerHero
 
logo_parte_externa = array.array('h', [40,53,55,40,185,40,200,53,200,187,185,200,55,200,40,187,40,53])
logo_parte_interna = array.array('h', [105,75,115,75,115,90,125,90,125,75,135,75,135,90,150,90,150,105,165,
                                       105,165,115,150,115,150,125,165,125,165,135,150,135,150,150,135,150,
                                       135,165,125,165,125,150,115,150,115,165,105,165,105,150,90,150,90,135,
                                       75,135,75,125,90,125,90,115,75,115,75,105,90,105,90,90,105,90,105,75])
 
# Preenche o fundo do display com preto
 
display.fill(colour(0,0,0))
display.show()
utime.sleep(3)
 
# Laco de execucao
 
while True:
     
    # Desenha as barras coloridas
     
    display.rect(0,0,35,240,colour(255,255,255),True)
    display.rect(35,0,35,240,colour(255,255,0),True)
    display.rect(70,0,35,240,colour(0,255,255),True)
    display.rect(105,0,35,240,colour(0,255,0),True)
    display.rect(140,0,35,240,colour(255,0,255),True)
    display.rect(175,0,35,240,colour(255,0,0),True)
    display.rect(210,0,35,240,colour(0,0,255),True)
    display.show()
    utime.sleep(3)
 
    # Desenha o circulo cinza de forma animada fazendo um setor de cada vez
 
    display.ellipse(120,120,120,120,colour(240,240,240),True,0b0001)
    display.show()
    utime.sleep(.1)
    display.ellipse(120,120,120,120,colour(240,240,240),True,0b1000)
    display.show()
    utime.sleep(.1)
    display.ellipse(120,120,120,120,colour(240,240,240),True,0b0100)
    display.show()
    utime.sleep(.1)
    display.ellipse(120,120,120,120,colour(240,240,240),True,0b0010)
    display.show()
    utime.sleep(.1)
     
    # Desenha o logo da MakerHero
 
    display.poly(0,0,logo_parte_externa,colour(0,0,0),True)
    display.poly(0,0,logo_parte_interna,colour(255,255,255),True)
    display.show()
    utime.sleep(5)
     
    # Desenha o smile
 
    display.fill(colour(255,255,255))
    display.ellipse(120,120,74,74,colour(245,245,0),True)
    display.ellipse(120,120,72,72,colour(250,250,0),True)
    display.ellipse(120,120,70,70,colour(255,255,0),True)
    display.rect(90,80,10,30,colour(0,0,0),True)
    display.rect(140,80,10,30,colour(0,0,0),True)
    display.ellipse(120,130,30,30,colour(0,0,0),True,0b1100)
    display.show()
    utime.sleep(.5)
     
    # Desenha o smile piscando e mostrando a lingua
     
    display.ellipse(120,120,74,74,colour(245,245,0),True)
    display.ellipse(120,120,72,72,colour(250,250,0),True)
    display.ellipse(120,120,70,70,colour(255,255,0),True)
    display.rect(90,80,10,30,colour(0,0,0),True)
    display.rect(140,90,10,10,colour(0,0,0),True)
    display.ellipse(120,130,30,30,colour(0,0,0),True,0b1100)
    display.rect(110,140,20,20,colour(255,120,120),True)
    display.ellipse(120,160,10,10,colour(255,120,120),True,0b1100)
    display.show()
    utime.sleep(.5)
     
    # Desenha o smile
     
    display.fill(colour(255,255,255))
    display.ellipse(120,120,74,74,colour(245,245,0),True)
    display.ellipse(120,120,72,72,colour(250,250,0),True)
    display.ellipse(120,120,70,70,colour(255,255,0),True)
    display.rect(90,80,10,30,colour(0,0,0),True)
    display.rect(140,80,10,30,colour(0,0,0),True)
    display.ellipse(120,130,30,30,colour(0,0,0),True,0b1100)
    display.show()
    utime.sleep(3)
     
    # Preenche o fundo do display com preto
     
    display.fill(colour(0,0,0))
    display.show()
    utime.sleep(1)
import RPi.GPIO as gpio
import time

cont=0
contador=0

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

sinal = 40

gpio.setup(22, gpio.OUT)
gpio.setup(24, gpio.OUT)
gpio.setup(26, gpio.OUT)
gpio.setup(sinal, gpio.IN)

def firstLed():
    for i in range(3):
        gpio.output(22, gpio.HIGH)
        gpio.output(24, gpio.HIGH)
        gpio.output(26, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(22, gpio.LOW)
        gpio.output(24, gpio.LOW)
        gpio.output(26, gpio.LOW)
        time.sleep(0.5)

def secondLed():
    for i in range(5):
        gpio.output(24, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(24, gpio.LOW)
        time.sleep(0.5)

def thirdLed():
    for i in range(10):
        gpio.output(22, gpio.HIGH)
        gpio.output(26, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(22, gpio.LOW)
        gpio.output(26, gpio.LOW)
        time.sleep(0.5)

verificador = False

while True:
    nivel_logico = gpio.input(sinal)

    time.sleep(0.2)
    contador = contador + 1

    if nivel_logico == 1:
        verificador = True
        #cont = cont + 1

    if nivel_logico == 0 and verificador == True:
        verificador = False
        cont = cont + 1
    
    if contador == 25:
        if cont == 1:
            firstLed()
            cont = 0
        elif cont == 2:
            secondLed()
            cont = 0
        elif cont == 3:
            thirdLed()
            cont = 0
        contador = 0
    if cont > 3:
        cont = 0
    print('contador de vezes:', cont)
    print('------')
    print('timer:', contador)
    print('------')
    
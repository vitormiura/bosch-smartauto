import RPi.GPIO as gpio
import time

cont = 0

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

sinal = 40

gpio.setup(22, gpio.OUT)
gpio.setup(24, gpio.OUT)
gpio.setup(26, gpio.OUT)
gpio.setup(sinal, gpio.IN)


while(True):
    nivel_logico = gpio.input(sinal)

    cont = cont + 1
    time.sleep(0.5)
    print(cont)

    if nivel_logico == gpio.LOW and cont == 6:
        for i in range(5):
            gpio.output(22, False)
            time.sleep(1)
            gpio.output(22, True)
            time.sleep(1)
    elif nivel_logico == gpio.LOW and cont == 11:
        for i in range(10):
            gpio.output(22, False)
            time.sleep(0.1)
            gpio.output(22, True)
            time.sleep(0.1)
    elif nivel_logico == gpio.LOW and cont == 16:
        for i in range(15):
            gpio.output(22, False)
            time.sleep(0.05)
            gpio.output(22, True)
            time.sleep(0.05)
    elif nivel_logico == gpio.LOW and cont == 21:
        gpio.output(22, False)

    elif nivel_logico == gpio.LOW:
        cont = 0


gpio.cleanup()
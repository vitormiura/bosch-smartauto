import RPi.GPIO as gpio
import time

cont = 0

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

gpio.setup(22, gpio.OUT)
gpio.setup(24, gpio.OUT)
gpio.setup(26, gpio.OUT)
gpio.setup(40, gpio.IN)

while True:
    botao = gpio.input(40)

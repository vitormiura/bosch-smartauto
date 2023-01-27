# cont = 0 

# if butao == 1:
#     if cont == 0:
#         botao.on 
#         cont++
#     elif cont == 1:
#         botao.off
#         cont--

import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

on = False
verificador = False

button = 38
gpio.setup(button, gpio.IN)

gpio.setup(40, gpio.OUT)

def on_connect(client, userdata, flags, rc):
    print(f"Conectado! {rc}")
    client.subscribe("miura")
    #client.publish("miura", payload = msg, qos = 0, retain = False)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    entrada = str(msg.payload)
    
    if entrada == "b'hello'":
        gpio.output(40, gpio.HIGH)
        print('acender')
    if entrada == "b'xau'":
        gpio.output(40, gpio.LOW)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("10.21.174.80", 1883, 60)

client.loop_start()

while True:
    butao = gpio.input(button)

    # time.sleep(0.5)
    # print('oiiiii')
    
    if butao == 1:
        verificador = True
        #cont = cont + 1

    if butao == 0 and verificador == True:
        verificador = False
        if on == True:
            on = False
        else:
            on = True
    
    if on == True:
        client.publish("miura", payload = 'oi', qos = 0, retain = False)
    else:
        client.publish("miura", payload = 'tchau', qos = 0, retain = False)

    #msg = input('INPUT: \n')
    #client.publish("miura", payload = msg, qos = 0, retain = False)


client.loop_forever()

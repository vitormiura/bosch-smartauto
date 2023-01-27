import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    #print(f"Conectado! {rc}")
    client.subscribe("miura")
    #client.publish("miura", payload = msg, qos = 0, retain = False)

def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    
    if str(msg.payload) == 'oi':
        print('ola mundo grande e maravilhoso!')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("10.21.174.80", 1883, 60)

client.loop_start()

while True:
    msg = input()
    client.publish("miura", payload = msg, qos = 0, retain = False)


client.loop_forever()

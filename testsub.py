import os, dotenv, time, paho.mqtt.client as mqtt

dotenv.load_dotenv()

mqttHost = str(os.getenv("mqttHost"))
mqttPort = int(os.getenv("mqttPort"))
mqttTopic = "Weather"
messageReceived = None

def on_message(client, userdata, msg ): # MQTT Function
    global messageReceived
    messageReceived = msg.payload.decode('utf-8')
    print(f"Message: [{msg.topic}]: {messageReceived}")
    
def on_connect(client, userdata, flags, rc): # MQTT Function
    print(f"Connected\nResult Code:{rc}")
    client.subscribe(mqttTopic)


client = mqtt.Client() 
client.on_connect = on_connect
client.on_message = on_message
client.connect(host=mqttHost, port=mqttPort)
client.loop_start()


while True:
    if messageReceived != messageReceived:
        print(messageReceived)
import time, dotenv, os, datetime, paho.mqtt.client as mqtt

dotenv.load_dotenv()
mqttHost = str(os.getenv("mqttHost"))
mqttPort = int(os.getenv("mqttPort"))
mqttTopic = "Test"

client=mqtt.Client()
client.connect(host=mqttHost, port=mqttPort)
while True:
    t=datetime.datetime.now()
    client.publish(mqttTopic,f"Hello World: {t.strftime('%c')}")
    print(f'pushed: Hello World: {t.strftime("%c")}\n')
    time.sleep(5)

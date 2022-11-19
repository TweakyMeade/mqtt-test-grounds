import os, dotenv, pygame, paho.mqtt.client as mqtt, json

dotenv.load_dotenv()

messageReceived = None
client = None
exitFlag = True

mqttHost = str(os.getenv("mqttHost"))
mqttPort = int(os.getenv("mqttPort"))
mqttTopic = "Test"

def on_message(client, userdata, msg ): # MQTT Function
    global messageReceived
    messageReceived = msg.payload.decode('utf-8')
    print(f"Message: [{msg.topic}]: {messageReceived}")
    
def on_connect(client, userdata, flags, rc): # MQTT Function
    print(f"Connected\nResult Code:{rc}")
    client.subscribe('Test')

def guiInit(title):
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(title)

def guiText(text):
    programFont=pygame.font.SysFont("Helvetica",20) 
    return programFont.render(text, True, "Red")

def guiTextBlit(text):
    
    array = json.loads(text)
    v = 0
    for i in array.keys():
        guiScreen.blit(guiText(f"{i}:{array[i]}"),(0,v))
        v += 20

    

def mqttInit(mqttHostInput,mqttPortInput):
    global client
    client = mqtt.Client() 
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host=mqttHostInput, port=mqttPortInput)
    client.loop_start()

mqttInit(mqttHost,mqttPort)
guiInit('test')


guiScreen = pygame.display.set_mode((640,480))

while exitFlag:

    guiScreen.fill((255,255,255))

    if messageReceived != messageReceived:
        print(messageReceived)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitFlag = False
    if messageReceived != None: 
        guiTextBlit(messageReceived)
    pygame.display.flip()
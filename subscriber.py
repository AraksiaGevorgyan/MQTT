import paho.mqtt.client as mqtt

# Callback function to handle incoming messages
def on_message(client, userdata, message):
    print(f"{str(message.payload.decode('utf-8'))}")

# MQTT broker settings
broker_address = "mqtt.eclipseprojects.io"
broker_port = 1883
topic = "group_chat"

client = mqtt.Client()

# Attach callback function to on_message event
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Subscribe to the group chat topic
client.subscribe(topic)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting...")
    client.disconnect()

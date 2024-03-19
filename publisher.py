import paho.mqtt.client as mqtt
import time

# MQTT broker settings
broker_address = "mqtt.eclipseprojects.io"
broker_port = 1883
topic = "group_chat"

client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

client.loop_start()

username = input("Enter your username: ")

while True:
    message = input("Enter message to publish (type 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    full_message = f"{username}: {message}"
    client.publish(topic, full_message)
    print(f"Message '{full_message}' published to topic '{topic}'")
    time.sleep(1)

client.loop_stop()
client.disconnect()

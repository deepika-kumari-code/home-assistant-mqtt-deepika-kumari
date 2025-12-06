# Author: Deepika Kumari
# Register Number: 42130115
# MQTT Sensor Publisher Script

import paho.mqtt.client as mqtt
import time
import random

BROKER = "test.mosquitto.org"
TOPIC = "deepika42130115/homeassistant/sensor"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    value = random.randint(20, 40)
    client.publish(TOPIC, value)
    print(f"Published: {value}")
    time.sleep(2)

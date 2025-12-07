# mqtt_sensor_pub.py
# Student: Deepika Kumari
# Register No: 42130115
# Topic: home/deepika-2025/sensor

import json
import time
import paho.mqtt.client as mqtt

student_name = "Deepika Kumari"
unique_id = "42130115"
topic = "home/deepika-2025/sensor"

MQTT_HOST = "localhost"   # use 'localhost' if broker on same machine
MQTT_PORT = 1883

client = mqtt.Client()

def publish_once():
    payload = {
        "student_name": student_name,
        "unique_id": unique_id,
        "temperature": 25,
        "humidity": 60,
        "light": 300            # extra sensor: light in lux
    }
    client.publish(topic, json.dumps(payload), qos=1, retain=False)
    print("Published:", payload)

if __name__ == "__main__":
    try:
        client.connect(MQTT_HOST, MQTT_PORT, 60)
    except Exception as e:
        print("Error connecting to MQTT broker:", e)
        raise

    try:
        while True:
            publish_once()
            time.sleep(2)   # publish every 2 seconds so values update during your video
    except KeyboardInterrupt:
        print("Stopping publisher")
        client.disconnect()


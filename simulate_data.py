import time
import json
import random
import paho.mqtt.client as mqtt
from datetime import datetime

# MQTT broker details
BROKER = "localhost"
PORT = 1883
TOPICS = ["env/temperature", "env/humidity", "env/airquality", "env/network"]

client = mqtt.Client()

def generate_payload(topic):
    timestamp = datetime.utcnow().isoformat()

    if topic == "env/temperature":
        return {
            "sensor_id": "temp_1",
            "timestamp": timestamp,
            "value": round(random.uniform(20.0, 30.0), 2)
        }
    elif topic == "env/humidity":
        return {
            "sensor_id": "hum_1",
            "timestamp": timestamp,
            "value": round(random.uniform(40.0, 70.0), 2)
        }
    elif topic == "env/airquality":
        return {
            "sensor_id": "aqi_1",
            "timestamp": timestamp,
            "AQI": random.randint(50, 200)
        }
    elif topic == "env/network":
        return {
            "source": f"device_{random.randint(1, 3)}",
            "target": f"gateway_{random.randint(1, 2)}",
            "type": "connected",
            "timestamp": timestamp
        }

def publish_loop():
    client.connect(BROKER, PORT)
    client.loop_start()
    try:
        while True:
            topic = random.choice(TOPICS)
            payload = generate_payload(topic)
            message = json.dumps(payload)
            print(f"[PUBLISH] Topic: {topic}, Payload: {message}")
            client.publish(topic, message)
            time.sleep(2)
    except KeyboardInterrupt:
        client.loop_stop()
        print("Publishing stopped.")

if __name__ == "__main__":
    publish_loop()

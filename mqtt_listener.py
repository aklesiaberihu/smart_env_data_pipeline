import json
import paho.mqtt.client as mqtt
from pymongo import MongoClient
from py2neo import Graph, Node, Relationship
from datetime import datetime
from db_sqlite import insert_temperature, insert_humidity

# MongoDB Setup
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["iot_data"]
airquality_collection = mongo_db["airquality"]

# Neo4j Setup
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

# MQTT Setup
BROKER = "localhost"
PORT = 1883
TOPICS = ["env/temperature", "env/humidity", "env/airquality", "env/network"]

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    for topic in TOPICS:
        client.subscribe(topic)

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = json.loads(msg.payload.decode())
    print(f"[RECEIVED] Topic: {topic}, Payload: {payload}")

    if topic == "env/airquality":
        airquality_collection.insert_one(payload)
        print("-> Stored in MongoDB")

    elif topic == "env/network":
        source = Node("Device", name=payload["source"])
        target = Node("Gateway", name=payload["target"])
        rel = Relationship(source, payload["type"], target, timestamp=payload["timestamp"])
        graph.merge(source, "Device", "name")
        graph.merge(target, "Gateway", "name")
        graph.create(rel)
        print("-> Stored in Neo4j")

    elif topic == "env/temperature":
        insert_temperature(payload)
        print("-> Stored in SQLite (temperature)")

    elif topic == "env/humidity":
        insert_humidity(payload)
        print("-> Stored in SQLite (humidity)")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()


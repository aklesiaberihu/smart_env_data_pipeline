Smart Environmental IoT Data Pipeline

This project simulates a real-time IoT data pipeline that collects environmental sensor readings and routes them to different databases using **MQTT**, **Python**, and **Docker Compose**. Each component is modular, containerized, and works together to emulate a smart data architecture with multiple database types: **SQLite**, **MongoDB**, and **Neo4j**.

---

## 1. Sensor Simulator

A Python script that:

- Simulates four sensor types:
  - Temperature
  - Humidity
  - Air Quality (AQI)
  - Device connectivity (for network graphing)
- Publishes JSON-formatted messages to specific MQTT topics:
  - `env/temperature`
  - `env/humidity`
  - `env/airquality`
  - `env/network`
- Uses `paho-mqtt` to send data to the MQTT broker.
- Runs continuously at 2-second intervals for each type.

**Key functions:**
- `simulate_temperature()` / `simulate_humidity()` / etc.
- `publish_data()` – handles MQTT publishing logic.

---

## 2. MQTT Listener (Data Router)

A Python service that:

- Subscribes to the above MQTT topics using `paho-mqtt`
- Parses each incoming message
- Routes the data to a database based on topic:
  - **env/temperature** → SQLite
  - **env/humidity** → SQLite
  - **env/airquality** → MongoDB
  - **env/network** → Neo4j

**Key functions:**
- `on_connect()` – subscribes to MQTT topics
- `on_message()` – routes data
- `store_in_sqlite()` / `store_in_mongo()` / `store_in_neo4j()`

---

## 3. MQTT Broker (Mosquitto)

- Eclipse Mosquitto runs in a Docker container
- Accepts messages from the Sensor Simulator
- Forwards them to the Listener

Configured to run anonymously on port **1883**, with a lightweight `.conf` file.

---

## 4. Databases

| Database   | Purpose                         | How It’s Used              |
|------------|----------------------------------|-----------------------------|
| **SQLite** | Structured numerical values      | Stores temperature & humidity |
| **MongoDB**| Semi-structured document storage | Stores AQI data (JSON)     |
| **Neo4j**  | Graph database                   | Stores network relationships |

All databases run in Docker containers with persistent volumes where needed.

---

## Integration & Data Flow

**Sensor Simulator**  
Publishes sensor readings to MQTT broker  
**MQTT Broker (Mosquitto)**  
Routes messages to the Listener  
**Listener (Data Router)**  
Analyzes topic and content  
Stores in the appropriate database (SQLite / MongoDB / Neo4j)

All services run inside Docker containers, communicating over a shared internal network.

---

## Dockerized Setup

All services are containerized and managed using Docker Compose.

### Key Docker Compose Features:
- One-command startup: `docker compose up -d`
- Runs:
  - `Mosquitto` on port 1883
  - `MongoDB` on 27017
  - `Neo4j` on 7474/7687
- Uses volume mounts for persistent data where required

---


 
## Folder Structure
```
smart_env_data_pipeline/
├── config/
│   └── mosquitto.conf           # MQTT broker configuration
├── data_router/
│   ├── mqtt_listener.py         # Subscribes to MQTT topics and routes data to databases
│   └── db_sqlite.py             # SQLite handler for temperature and humidity
├── sensor_simulator/
│   └── simulate_data.py         # Simulates and publishes sensor data via MQTT
├── docker-compose.yml           # Docker setup for MQTT, MongoDB, Neo4j
├── environment_data.db          # SQLite database (auto-generated)
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
```


## MQTT Topics and Database Routing

| Topic             | Destination DB |
|------------------|----------------|
| env/temperature   | SQLite         |
| env/humidity      | SQLite         |
| env/airquality    | MongoDB        |
| env/network       | Neo4j          |

## Important Commands 
''' bash

1. Start all services -
docker compose up -d

2. Run the listener -
python data_router/mqtt_listener.py

3. Run the simulator -
python sensor_simulator/simulate_data.py

4. Stop containers - 
docker compose down

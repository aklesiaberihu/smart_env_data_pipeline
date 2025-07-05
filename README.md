# Smart Environmental IoT Data Pipeline

A containerized pipeline that simulates real-time environmental sensor readings and routes them to appropriate databases using **Python**, **MQTT**, and **Docker Compose**. The system demonstrates how different types of IoT data can be stored in specialized databases:
- **SQLite** for structured data
- **MongoDB** for semi-structured documents
- **Neo4j** for graph-based device relationships

---

## System Overview

- **Sensor Simulator**: Generates temperature, humidity, air quality (AQI), and device network data.
- **MQTT Broker**: Receives data via topics (`env/temperature`, `env/humidity`, etc.).
- **MQTT Listener**: Subscribes to topics and routes data to the correct database.
- **Databases**: Each one stores a specific type of data for optimal structure and retrieval.

---

## Components

### Sensor Simulator (`simulate_data.py`)
- Simulates 4 types of sensors
- Publishes to:
  - `env/temperature`
  - `env/humidity`
  - `env/airquality`
  - `env/network`
- Publishes every 2 seconds using `paho-mqtt`

---

### MQTT Listener (`mqtt_listener.py`)
- Subscribes to all `env/*` topics
- Routes data:
  - ➤ **SQLite**: temperature & humidity
  - ➤ **MongoDB**: air quality
  - ➤ **Neo4j**: device connectivity graph

---

### MQTT Broker (Mosquitto)
- Lightweight MQTT broker (Dockerized)
- Listens on port `1883`
- Configured via `mosquitto.conf`

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

### Databases Used

| Database   | Data Stored                   |
|------------|-------------------------------|
| SQLite     | Temperature, Humidity         |
| MongoDB    | Air Quality (AQI JSON docs)   |
| Neo4j      | Device-to-device relationships|

## Important commands 

### 1. Start services
docker compose up -d

### 2. Start MQTT Listener
python data_router/mqtt_listener.py

### 3. Start Sensor Simulator
python sensor_simulator/simulate_data.py

### 4. Stop everything
docker compose down


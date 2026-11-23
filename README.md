# Smart Environmental IoT Data Pipeline

A containerized real-time IoT data pipeline that simulates environmental sensor streams and routes them across three specialized databases using **Python**, **MQTT (Eclipse Mosquitto)**, and **Docker Compose**. This project demonstrates **polyglot persistence**—matching each data type to the database architecture best suited for it.

## Architecture

```text
[ Sensor Simulator (simulate_data.py) ]
                  │  Publishes every 2s via paho-mqtt
                  ▼
[ Mosquitto MQTT Broker (Port 1883) ]
                  │  Subscribes to env/*
                  ▼
[ MQTT Listener / Router (mqtt_listener.py) ]
     ├──► env/temperature & env/humidity ──► SQLite (Relational)
     ├──► env/airquality                 ──► MongoDB (Document Store)
     └──► env/network                    ──► Neo4j (Graph Database)
```

## Polyglot Storage Strategy

| Database | Type | Data Stored | Why This Database? |
| :--- | :--- | :--- | :--- |
| **SQLite** | Relational | Temperature & Humidity | Lightweight, structured time-stamped numerical records |
| **MongoDB** | Document | Air Quality (AQI JSON) | Flexible schema for nested, semi-structured sensor payloads |
| **Neo4j** | Graph | Device Connectivity | Native storage and querying for device-to-device relationships |

## Components
- **`simulate_data.py`**: Generates synthetic readings for 4 sensor types (`env/temperature`, `env/humidity`, `env/airquality`, `env/network`) and publishes them every 2 seconds using `paho-mqtt`.
- **`mqtt_listener.py`**: Subscribes to `env/*` topics, parses incoming payloads, and routes each message to its designated database.
- **`db_sqlite.py`**: Handles SQLite schema initialization and writes for structured temperature and humidity readings.
- **`mosquitto.conf` & `docker-compose.yml`**: Containerizes and configures the Mosquitto MQTT broker (port `1883`), MongoDB, and Neo4j services.

## Repository Structure

```text
smart_env_data_pipeline/
├── docker-compose.yml       # Docker setup for Mosquitto, MongoDB, and Neo4j
├── mosquitto.conf           # MQTT broker configuration
├── simulate_data.py         # IoT sensor simulator (MQTT publisher)
├── mqtt_listener.py         # MQTT subscriber and multi-DB data router
├── db_sqlite.py             # SQLite database handler
├── requirements.txt         # Python dependencies
├── environment_data.db      # Sample/auto-generated SQLite database
└── README.md                # Project documentation
```

## How to Run Locally

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Dockerized services (Mosquitto, MongoDB, Neo4j):**
   ```bash
   docker compose up -d
   ```

3. **Start the MQTT Listener (Terminal 1):**
   ```bash
   python mqtt_listener.py
   ```

4. **Start the Sensor Simulator (Terminal 2):**
   ```bash
   python simulate_data.py
   ```

5. **Stop all services when finished:**
   ```bash
   docker compose down
   ```

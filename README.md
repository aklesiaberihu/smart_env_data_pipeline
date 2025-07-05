# Smart Environmental Data Pipeline

A real-time IoT data collection and storage system using MQTT, Python, and multi-database integration.

## Technologies Used

- **Python**: Sensor simulation, MQTT subscriber
- **Eclipse Mosquitto**: MQTT broker (via Docker)
- **MongoDB**: Stores air quality sensor data
- **Neo4j**: Stores IoT device network relationships
- **SQLite**: Stores temperature and humidity in structured form
- **Docker Compose**: Orchestrates services

## Folder Structure
smart_env_data_pipeline/
├── config/
│ └── mosquitto.conf
├── data_router/
│ ├── mqtt_listener.py
│ └── db_sqlite.py
├── sensor_simulator/
│ └── simulate_data.py
├── docker-compose.yml
├── environment_data.db
├── requirements.txt
├── README.md

## MQTT Topics and Database Routing

| Topic             | Destination DB |
|------------------|----------------|
| env/temperature   | SQLite         |
| env/humidity      | SQLite         |
| env/airquality    | MongoDB        |
| env/network       | Neo4j          |

## How to Run the Project

1. Start all containers:
```bash
docker compose up -d

2. Run the simulator:
```bash
python sensor_simulator/simulate_data.py

3. Run the subscriber:
```bash
python data_router/mqtt_listener.py



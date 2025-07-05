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
│ └── mosquitto.conf # MQTT broker configuration
├── data_router/
│ ├── mqtt_listener.py # Subscribes to MQTT topics and routes data to databases
│ └── db_sqlite.py # SQLite database handler for temperature and humidity
├── sensor_simulator/
│ └── simulate_data.py # Simulates sensor data and publishes it via MQTT
├── docker-compose.yml # Docker configuration to run MQTT, MongoDB, and Neo4j
├── environment_data.db # SQLite database file (auto-generated)
├── requirements.txt # Python dependencies
├── README.md # Project documentation

## MQTT Topics and Database Routing

| Topic             | Destination DB |
|------------------|----------------|
| env/temperature   | SQLite         |
| env/humidity      | SQLite         |
| env/airquality    | MongoDB        |
| env/network       | Neo4j          |

## How to Run the Project

1. Start all containers:

docker compose up -d

2. Run the simulator:

python sensor_simulator/simulate_data.py

3. Run the subscriber:

python data_router/mqtt_listener.py

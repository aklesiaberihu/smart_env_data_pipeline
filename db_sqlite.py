import sqlite3
from datetime import datetime

conn = sqlite3.connect("environment_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS temperature (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id TEXT,
    timestamp TEXT,
    value REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS humidity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id TEXT,
    timestamp TEXT,
    value REAL
)
""")

conn.commit()

def insert_temperature(data):
    cursor.execute("INSERT INTO temperature (sensor_id, timestamp, value) VALUES (?, ?, ?)",
                   (data["sensor_id"], data["timestamp"], data["value"]))
    conn.commit()

def insert_humidity(data):
    cursor.execute("INSERT INTO humidity (sensor_id, timestamp, value) VALUES (?, ?, ?)",
                   (data["sensor_id"], data["timestamp"], data["value"]))
    conn.commit()

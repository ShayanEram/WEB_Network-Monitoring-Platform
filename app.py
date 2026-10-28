from flask import Flask, render_template
from api.routes import api
import sqlite3
import os
import config

from models.device import DeviceLog
from models.traffic import TrafficLog

app = Flask(__name__)

# Load configuration
app.config.from_object("config")

# Register API routes
app.register_blueprint(api)

db_path = config.DATABASE_PATH
os.makedirs(os.path.dirname(db_path), exist_ok=True)

conn = sqlite3.connect(db_path)
with open("database/schema.sql", "r") as f:
    conn.executescript(f.read())
conn.commit()
conn.close()
print("Database initialized successfully!")


# Add test devices
DeviceLog.add_device("192.168.1.10", "Desktop-PC")
DeviceLog.add_device("192.168.1.15", "Laptop")

# Add test traffic packets
TrafficLog.insert_packet("192.168.1.10", "8.8.8.8", 512, "TCP")
TrafficLog.insert_packet("192.168.1.15", "1.1.1.1", 256, "UDP")
print("Test data inserted!")


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

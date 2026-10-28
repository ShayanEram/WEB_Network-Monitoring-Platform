from flask import Flask, render_template
from api.routes import api
import sqlite3
import os
import config

import subprocess
import sys

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


# # Add test devices
# DeviceLog.add_device("192.168.1.10", "Desktop-PC")
# DeviceLog.add_device("192.168.1.15", "Laptop")


# # Add test traffic packets
# TrafficLog.insert_packet("192.168.1.10", "8.8.8.8", 512, "TCP")
# TrafficLog.insert_packet("192.168.1.15", "1.1.1.1", 256, "UDP")
# print("Test data inserted!")
def compile_c_engine():
    """Directly compiles the C network engine using Zig from Python"""
    print("Compiling C network engine using Zig...")

    # Automatically handle Windows (.exe) vs Linux/Mac extensions
    output_name = (
        "network_engine/packet_sniffer.exe"
        if os.name == "nt"
        else "network_engine/packet_sniffer"
    )
    source_file = "network_engine/packet_sniffer.c"

    try:
        subprocess.run(
            ["zig", "cc", source_file, "-o", output_name],
            check=True,
            capture_output=True,
            text=True,
        )
        print("Compilation successful!")
    except subprocess.CalledProcessError as e:
        print("Compilation failed:\n", e.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(
            "Error: 'zig' command not found. Ensure Zig is installed and added to your system PATH."
        )
        sys.exit(1)


def listen_to_network_engine():
    # Path to your compiled C executable
    c_executable = "./network_engine/packet_sniffer"  # or packet_sniffer.exe on Windows

    try:
        process = subprocess.Popen(
            [c_executable], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        # Read output line by line as C prints it
        for line in process.stdout:
            line = line.strip()
            if not line:
                continue

            # Parse the CSV output from C: "192.168.1.50,142.250.190.46,512,TCP"
            parts = line.split(",")
            if len(parts) == 4:
                source_ip, dest_ip, size, protocol = parts

                # Use your existing Python model to save it to SQLite!
                TrafficLog.insert_packet(source_ip, dest_ip, int(size), protocol)
                print(f"Logged packet from C: {source_ip} -> {dest_ip}")

    except FileNotFoundError:
        print(
            f"C engine binary not found at {c_executable}. Make sure to compile it first!"
        )


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    # 1. Compile the C engine first
    compile_c_engine()
    listen_to_network_engine()

    app.run(debug=True)

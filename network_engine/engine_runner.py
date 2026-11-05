import os
import sys
import subprocess
import config
from models.traffic import TrafficLog
from models.device import DeviceLog

def compile_c_engine():
    print("Compiling C network engine using Zig...")

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
    c_executable = config.EXE_PATH

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

                # 1. Save packet into traffic_logs table
                TrafficLog.insert_packet(source_ip, dest_ip, int(size), protocol)

                # 2. Automatically register/update source device in devices table
                DeviceLog.add_device(source_ip, hostname=f"Device-{source_ip.split('.')[-1]}")

                print(f"Logged packet from C: {source_ip} -> {dest_ip}")

    except FileNotFoundError:
        print(f"C engine binary not found at {c_executable}. Make sure to compile it first!")
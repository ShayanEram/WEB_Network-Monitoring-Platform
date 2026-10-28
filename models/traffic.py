from database.databaseHelper import get_db_connection


class TrafficLog:
    def __init__(self):
        pass

    def insert_packet(source_ip, destination_ip, packet_size, protocol):
        conn = get_db_connection()
        conn.execute(
            """
            INSERT INTO traffic_logs (source_ip, destination_ip, packet_size, protocol) 
            VALUES (?, ?, ?, ?)
            """,
            (source_ip, destination_ip, packet_size, protocol),
        )
        conn.commit()
        conn.close()

    def get_protocol_counts():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT protocol, COUNT(*) as count FROM traffic_logs GROUP BY protocol"
        )
        rows = cursor.fetchall()
        conn.close()
        return {row["protocol"]: row["count"] for row in rows} if rows else {}

    def get_packet_total():
        pass

    def get_top_talkers():
        return [
            {"ip": "192.168.1.10", "packets": 4210},
            {"ip": "192.168.1.15", "packets": 3175},
            {"ip": "192.168.1.20", "packets": 1440},
        ]

    def get_dashboard_stats():
        conn = get_db_connection()
        cursor = conn.cursor()

        # Total packets and total packet size (bandwidth approximation)
        cursor.execute(
            "SELECT COUNT(*) as count, SUM(packet_size) as total_size FROM traffic_logs"
        )
        packet_res = cursor.fetchone()
        total_packets = packet_res["count"] if packet_res and packet_res["count"] else 0
        total_bytes = (
            packet_res["total_size"] if packet_res and packet_res["total_size"] else 0
        )

        # Total active devices
        cursor.execute("SELECT COUNT(*) as count FROM devices")
        device_res = cursor.fetchone()
        total_devices = device_res["count"] if device_res else 0

        # Top protocol
        cursor.execute(
            "SELECT protocol, COUNT(*) as cnt FROM traffic_logs GROUP BY protocol ORDER BY cnt DESC LIMIT 1"
        )
        proto_res = cursor.fetchone()
        top_protocol = (
            proto_res["protocol"] if proto_res and proto_res["protocol"] else "N/A"
        )

        conn.close()

        # Format bandwidth
        if total_bytes > 1024 * 1024:
            bandwidth = f"{total_bytes / (1024 * 1024):.2f} MB"
        elif total_bytes > 1024:
            bandwidth = f"{total_bytes / 1024:.2f} KB"
        else:
            bandwidth = f"{total_bytes} Bytes"

        return {
            "packets": total_packets,
            "devices": total_devices,
            "bandwidth": bandwidth,
            "top_protocol": top_protocol,
        }

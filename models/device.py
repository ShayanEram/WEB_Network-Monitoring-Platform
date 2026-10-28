from database.databaseHelper import get_db_connection


class DeviceLog:
    def __init__(self):
        pass

    def get_all_devices():
        conn = get_db_connection()
        devices = conn.execute(
            "SELECT ip_address as ip, hostname, last_seen FROM devices"
        ).fetchall()
        conn.close()
        return [dict(d) for d in devices]

    def add_device(ip, hostname):
        conn = get_db_connection()
        conn.execute(
            """
            INSERT INTO devices (ip_address, hostname, last_seen) 
            VALUES (?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(ip_address) DO UPDATE SET last_seen = CURRENT_TIMESTAMP
            """,
            (ip, hostname),
        )
        conn.commit()
        conn.close()

    def update_last_seen(ip):
        conn = get_db_connection()
        conn.execute(
            "UPDATE devices SET last_seen = CURRENT_TIMESTAMP WHERE ip_address = ?",
            (ip,),
        )
        conn.commit()
        conn.close()

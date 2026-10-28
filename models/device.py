class DeviceLog:
    def __init__(self):
        pass

    def get_all_devices():
        return [
            {
                "ip": "192.168.1.10",
                "hostname": "Desktop-PC",
                "last_seen": "12:30:15",
            },
            {
                "ip": "192.168.1.15",
                "hostname": "Laptop",
                "last_seen": "12:30:08",
            },
            {
                "ip": "192.168.1.20",
                "hostname": "Phone",
                "last_seen": "12:29:55",
            },
        ]

    def add_device(ip, hostname):
        pass

    def update_last_seen(ip):
        pass

CREATE TABLE devices (
    id INTEGER PRIMARY KEY,
    ip_address TEXT,
    hostname TEXT,
    last_seen DATETIME
);
CREATE TABLE traffic_logs (
    id INTEGER PRIMARY KEY,
    source_ip TEXT,
    destination_ip TEXT,
    protocol TEXT,
    packet_size INTEGER,
    timestamp DATETIME
);
CREATE TABLE alerts (
    id INTEGER PRIMARY KEY,
    title TEXT,
    message TEXT,
    created_at DATETIME
);
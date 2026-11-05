from database.databaseHelper import get_db_connection


class AlertLog:
    def __init__(self):
        pass

    def get_all_alerts(severity="all"):
        conn = get_db_connection()
        if severity and severity != "all":
            alerts = conn.execute(
                "SELECT id, title, message, severity, created_at FROM alerts WHERE severity = ? ORDER BY id DESC",
                (severity,),
            ).fetchall()
        else:
            alerts = conn.execute(
                "SELECT id, title, message, severity, created_at FROM alerts ORDER BY id DESC"
            ).fetchall()
        conn.close()
        return [dict(a) for a in alerts]

    def add_alert(title, message, severity="info"):
        conn = get_db_connection()
        conn.execute(
            """
            INSERT INTO alerts (title, message, severity, created_at) 
            VALUES (?, ?, ?, CURRENT_TIMESTAMP)
            """,
            (title, message, severity),
        )
        conn.commit()
        conn.close()

    def seed_dummy_alerts():
        conn = get_db_connection()
        dummy_alerts = [
            (
                "Port Scan Detected",
                "Multiple connection attempts from 192.168.1.101 across 45 ports.",
                "critical",
            ),
            (
                "High Bandwidth Usage",
                "Device 192.168.1.50 exceeded 50MB data threshold in 5 minutes.",
                "warning",
            ),
            (
                "Unknown External IP",
                "Traffic routed to blacklisted or unverified external endpoint.",
                "info",
            ),
            (
                "Unencrypted Protocol",
                "Plaintext HTTP traffic identified on port 80 from 192.168.1.15.",
                "warning",
            ),
        ]

        conn.executemany(
            """
                INSERT OR IGNORE INTO alerts (title, message, severity, created_at)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
            """,
            dummy_alerts,
        )
        conn.commit()
        conn.close()

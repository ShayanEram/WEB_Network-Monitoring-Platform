# Stores packet information.

class TrafficLog(db.Model):
    __tablename__ = "traffic_logs"

    source_ip = db.Column(db.String(45))
    destination_ip = db.Column(db.String(45))
    protocol = db.Column(db.String(20))
# Maps Python objects to SQL rows.

from flask_sqlalchemy import SQLAlchemy

class Device(db.Model):
    __tablename__ = "devices"

    id = db.Column(db.Integer,
                   primary_key=True)

    ip_address = db.Column(db.String(45))
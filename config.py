'''config.py

Purpose: Centralized configuration.
'''

import os

DB_HOST = os.getenv("DB_HOST")

DB_HOST = "localhost"
DB_NAME = "network_monitor"

PACKET_CAPTURE_INTERVAL = 5

SECRET_KEY = "secret"
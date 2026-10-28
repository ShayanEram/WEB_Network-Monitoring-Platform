from flask import Blueprint, jsonify

from models.device import DeviceLog
from models.traffic import TrafficLog

api = Blueprint("api", __name__)


@api.route("/api/stats")
def stats():
    return jsonify(TrafficLog.get_dashboard_stats())


@api.route("/api/devices")
def devices():
    return jsonify(DeviceLog.get_all_devices())


@api.route("/api/protocols")
def protocols():
    return jsonify(TrafficLog.get_protocol_counts())

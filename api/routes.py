from flask import Blueprint, jsonify, request

from models.device import DeviceLog
from models.traffic import TrafficLog
from models.alert import AlertLog

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


@api.route("/api/traffic")
def traffic_logs():
    limit = request.args.get("limit", 100, type=int)
    logs = (
        TrafficLog.get_recent_logs(limit=limit)
        if hasattr(TrafficLog, "get_recent_logs")
        else []
    )
    return jsonify(logs)


@api.route("/api/alerts")
def alerts():
    severity = request.args.get("severity", "all")
    alert_list = (
        AlertLog.get_all_alerts(severity=severity)
        if hasattr(AlertLog, "get_all_alerts")
        else []
    )
    return jsonify(alert_list)

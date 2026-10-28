from flask import Blueprint, jsonify

api = Blueprint("api", __name__)


@api.route("/api/stats")
def stats():
    return jsonify({})


@api.route("/api/devices")
def devices():
    return jsonify([])


@api.route("/api/protocols")
def protocols():
    return jsonify({})

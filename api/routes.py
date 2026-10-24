'''routes.py

Contains REST endpoints.
'''

@api.route("/api/stats")
def stats():
    return jsonify({...})
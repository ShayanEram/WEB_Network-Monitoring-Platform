'''app.py

Purpose: Main Flask application entry point.

Responsibilities:

Create Flask app
Initialize database connection
Register API routes
Configure logging
Start web server
'''

from flask import Flask
from api.routes import api

app = Flask(__name__)
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)
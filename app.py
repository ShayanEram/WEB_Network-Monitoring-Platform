from flask import Flask, render_template
from api.routes import api
import config
import threading

from models.alert import AlertLog
from database.databaseHelper import init_db
from network_engine.engine_runner import compile_c_engine, listen_to_network_engine

# Flask Init-----------------------------------------------------------------------------
app = Flask(__name__)

# Load configuration
app.config.from_object("config")

# Register API routes
app.register_blueprint(api)


# INTERFACE-PAGES ---------------------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/devices")
def devices_page():
    return render_template("devices.html")


@app.route("/traffic")
def traffic_page():
    return render_template("traffic.html")


@app.route("/alerts")
def alerts_page():
    return render_template("alerts.html")


@app.route("/about")
def about_page():
    return render_template("about.html", version=config.VERSION)


# MAIN ------------------------------------------------------------------------------------
if __name__ == "__main__":
    # 1. Initialize the database
    init_db()

    # 2. Compile the C engine
    compile_c_engine()

    # 3. Start the C packet sniffer in a background daemon thread
    sniffer_thread = threading.Thread(target=listen_to_network_engine, daemon=True)
    sniffer_thread.start()

    AlertLog.seed_dummy_alerts()

    # 4. Run the Flask web server
    app.run(debug=config.DEBUG)

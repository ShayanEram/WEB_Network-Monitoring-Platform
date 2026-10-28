from flask import Flask, render_template
from api.routes import api

app = Flask(__name__)

# Load configuration
app.config.from_object("config")

# Register API routes
app.register_blueprint(api)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

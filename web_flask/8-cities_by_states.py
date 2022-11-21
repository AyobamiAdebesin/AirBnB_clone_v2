#!/usr/bin/python3
from flask import Flask
from models import storage
from flask import render_template
from models.state import State
app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def get_cities_by_states():
    all_states = storage.all(State)
    return render_template(
            "8-cities_by_states.html",
            states=all_states)

@app.teardown_appcontext
def teardown(exc):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")

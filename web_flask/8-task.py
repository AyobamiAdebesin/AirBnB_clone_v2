#!/usr/bin/python3

from models import storage
from flask import Flask
from flask import render_template
from models.state import State

app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def get_cities_by_states():
    all_states = storage.all(State)
    return render_template("8-cities-by-states", states=all_states)

@app.teardown_appcontext
def close_db_session(exec):
    storage.close()

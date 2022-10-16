#!/usr/bin/python3
"""
A script that starts a Flask web application
Listening on 0.0.0.0 port 5000

Displays Hello HBNB on route "/"
Displays HBNB on route "/hbnb"
"""

from flask import Flask
from flask import escape0

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hello():
    """ Displas Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def say_hbnb():
    """ Displays HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c():
    """ Returns a custom message """
    return f"C {escape(text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")

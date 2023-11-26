#!/usr/bin/python3
"""renders html files"""
from models import storage
from flask import Flask, render_template

flask_app = Flask(__name__)


@flask_app.route("/states", strict_slashes=False)
def get_state():
    """gets the state"""
    s = storage.all("State")
    return render_template("9-states.html", state=s)


@flask_app.route("/states/<id>", strict_slashes=False)
def get_cities(id):
    """gets cities of a given id"""
    for s in storage.all("State").values():
        if s.id == id:
            return render_template("9-states.html", state=s)
    return render_template("9-states.html")


@flask_app.teardown_appcontext
def reloads(exep):
    """reloads all"""
    storage.close()


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0")

#!/usr/bin/python3
"""lists states in an html file"""
from flask import Flask, render_template
from models import storage

flask_app = Flask(__name__)


@flask_app.route("/states_list", strict_slashes=False)
def get_states():
    """lists all the states"""
    s = storage.all("State")
    return render_template("7-states_list.html", state=s)


@flask_app.teardown_appcontext
def reloads(exc):
    """reloads session"""
    storage.close()


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0")

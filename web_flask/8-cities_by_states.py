#!/usr/bin/python3
"""  lists cities in an html file """

from models import storage
from models.city import City
from models.state import State
from flask import Flask, render_template


flask_app = Flask(__name__)


@flask_app.teardown_appcontext
def reloads(exep):
    """reloads session"""
    storage.close()


@flask_app.route('/cities_by_states', strict_slashes=False)
def render_city():
    """ lists cities in an html file """
    s = list(storage.all(State).values())
    return render_template('8-cities_by_states.html', state=s)


if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""  starts a Flask web application """

from models import storage
from models.state import State
from flask import Flask, render_template


flask_app = Flask(__name__)


@flask_app.teardown_appcontext
def reloads(exep):
    """reloads the state"""
    storage.close()


@flask_app.route('/states', strict_slashes=False, defaults={'id': None})
@flask_app.route('/states/<id>')
def get_cities(id):
    """ shows cities by state id """
    s = list(storage.all(State).values())
    if id is None:
        return render_template('7-states_list.html', state=s)
    for val in s:
        if val.id == id:
            return render_template('9-states.html', state=val)
    return render_template('9-states.html', state=None)


if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port=5000)

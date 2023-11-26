#!/usr/bin/python3
"""Renders State values"""
from models import *
from models import storage
from flask import Flask, render_template


flask_app = Flask(__name__)


@flask_app.route('/states', strict_slashes=False)
@flask_app.route('/states/<state_id>', strict_slashes=False)
def get_state(id=None):
    """Renders available states"""
    s = storage.all("State")
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html', id=id, state=s)


@flask_app.teardown_appcontext
def reloads(exep):
    """reloads the state"""
    storage.close()

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port='5000')

#!/usr/bin/python3
""" initializes and configures a Flask web application"""

from flask import Flask, render_template
from models import storage

flask_app = Flask(__name__)

@flask_app.route('/states', strict_slashes=False)
@flask_app.route('/states/<id>', strict_slashes=False)
def get_states(id=None):
    """Display states and cities listed in alphabetical order."""
    s = storage.all("State")
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html', state=s, id=id)

@flask_app.teardown_appcontext
def close_db(exep):
    """Close the db"""
    storage.close()

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port='5000')

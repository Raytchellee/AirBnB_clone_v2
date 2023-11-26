#!/usr/bin/python3
"""  init flask application """

from models import storage
from models.city import City
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template


flask_app = Flask(__name__)


@flask_app.teardown_appcontext
def close_db(exep):
    """Close the database"""
    storage.close()


@flask_app.route('/hbnb_filters', strict_slashes=False)
def fet_filters():
    """gets filters by state"""
    s = list(storage.all(State).values())
    a = list(storage.all(Amenity).values())
    return render_template('10-hbnb_filters.html',
                           states=s,
                           amenities=a)


if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port=5000)

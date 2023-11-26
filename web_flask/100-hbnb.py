#!/usr/bin/python3
"""  starts a Flask web application """

from models import storage
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template


flask_app = Flask(__name__)


@flask_app.teardown_appcontext
def close_db(exep):
    """Close the database"""
    storage.close()


@flask_app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays places by state"""
    s = list(storage.all(State).values())
    a = list(storage.all(Amenity).values())
    p = list(storage.all(Place).values())
    return render_template('100-hbnb.html',
                           states=s,
                           amenities=a,
                           places=p)


if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""Starts Flask web application"""
from flask import Flask, render_template

flask_app = Flask(__name__)


@flask_app.route("/", strict_slashes=False)
def base():
    """Returns Hello HBNB to request"""
    return "Hello HBNB!"


@flask_app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB to /hbnb request"""
    return "HBNB"


@flask_app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Returns HBNB to /c/<text> request"""
    return "C %s" % str(text.replace("_", " "))


@flask_app.route("/python/<text>", strict_slashes=False)
@flask_app.route("/python/")
def python_text(text="is cool"):
    """Returns HBNB to /python/<text> request"""
    return "Python %s" % str(text.replace("_", " "))


@flask_app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """ confirms only numbers in /number/n """
    return "{} is a number".format(n)


@flask_app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    """ renders template on /number_template/n """
    return render_template('5-number.html', number=n)


@flask_app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """ renders template on /number_odd_or_even/n """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port="5000")

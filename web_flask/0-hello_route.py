#!/usr/bin/python3
"""Starts Flask web application"""
from flask import Flask, request

flask_app = Flask(__name__)


@flask_app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port="5000")

#!/usr/bin/python3
from flask import Flask
"""Flask web app"""

app = Flasik(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """starts a Flask web application"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

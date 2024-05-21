#!/usr/bin/python3
"""Flask web application:"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """landing page"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB route"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """displays 'C ' followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_route(text):
    """display 'Python ' followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """ displays 'n is a number' only if n is an integer"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

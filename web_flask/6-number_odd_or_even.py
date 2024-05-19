#!/usr/bin/python3
"""Flask web application:"""
from flask import Flask
from flask import render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    """display a HTML page only if n is an integer:"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """display a HTML page only if n is an integer"""
    num = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, num=num)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

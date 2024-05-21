#!/usr/bin/python3
"""python script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import state


app = Flask(__name__)

@app.teardown_appcontext
def shutdownself():
    """closes database session after each request"""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities(self):
    """displays a HTML page"""
    states = storage.all(state)
    return render_template('8-cities_by_state.html', states=states)


if __name__== "__main__":
    app.run(host="0.0.0.0", port="5000")

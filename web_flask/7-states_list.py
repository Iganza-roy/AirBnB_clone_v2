#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
# from models import storage
# from models.state import state

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_temp():
    """display a HTML page with a list of all states"""
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def shutdownself():
    """closes database session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

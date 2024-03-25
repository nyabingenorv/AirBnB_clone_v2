#!/usr/bin/python3
"""
This module starts a Flask web app listening on 0.0.0.0:5000.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models import type_of_storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_cities_by_states():
    """Displays an HTML page with lists of cities for each state."""

    states = storage.all(State)

    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def end_session(exc):
    """Ends the current SQLAlchemy session after each request"""

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

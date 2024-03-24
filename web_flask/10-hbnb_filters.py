#!/usr/bin/python3
"""
This module starts a Flask web app listening on 0.0.0.0:5000.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def display_filters():
    """Displays an HTML page with states and amenities filters."""

    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()

    return render_template(
        '10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def end_session(exc):
    """Ends the current SQLAlchemy session after each request"""

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

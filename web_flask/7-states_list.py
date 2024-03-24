#!/usr/bin/python3
"""
This module starts a Flask web app listening on 0.0.0.0:5000.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """Displays an HTML page with a list of states."""

    states = storage.all(State)

    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def end_session(exc):
    """Ends the current SQLAlchemy session after each request"""

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

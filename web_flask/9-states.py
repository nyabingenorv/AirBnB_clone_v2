#!/usr/bin/python3
"""
This module starts a Flask web app listening on 0.0.0.0:5000.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def list_cities_by_states(id=None):
    """Displays an HTML page with lists of cities for each state."""

    states = storage.all(State).values()
    selected_state = None

    if id:
        for state in states:
            if state.id == id:
                selected_state = state

    return render_template(
        '9-states.html', states=states, id=id, selected_state=selected_state)


@app.teardown_appcontext
def end_session(exc):
    """Ends the current SQLAlchemy session after each request"""

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

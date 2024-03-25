#!/usr/bin/python3
"""
This module starts a Flask web app listening on 0.0.0.0:5000.
"""

from typing import Literal
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns a welcome string"""

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb() -> Literal['HBNB']:
    """Returns HBNB"""

    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

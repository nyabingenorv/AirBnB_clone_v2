#!/usr/bin/python3
"""
This module starts a Flask web app listening on 0.0.0.0:5000.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns a welcome string"""

    return render_template()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

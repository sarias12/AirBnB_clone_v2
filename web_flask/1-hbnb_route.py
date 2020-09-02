#!/usr/bin/python3
"""
Modele For start a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display Text hello"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def text():
    """Display Text"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

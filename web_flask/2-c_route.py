#!/usr/bin/python3
"""
Modele For start a Flask web application
"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display Text hello"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def text():
    """Display Text"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_variable(text):
    """Display with value of text variable"""""
    return 'C %s' % escape(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

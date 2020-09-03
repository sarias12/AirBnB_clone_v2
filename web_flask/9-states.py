#!/usr/bin/python3
"""
Modele For start a Flask web application
"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id='noid'):
    list = []
    states = storage.all(State)
    if id != 'noid':
        for state in states.values():
            if state.id == id:
                state_display = state
                return render_template('9-states.html', state=state_display)
        return render_template('9-states.html')

@app.route('/states', strict_slashes=False)
def states():
    list = []
    states = storage.all(State)
    for key, value in states.items():
        list.append(value)
    return render_template('9-states.html', list=list)


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

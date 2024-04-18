#!/usr/bin/python3
"""a script that starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def hbnb_filters():
    """Returns html template using web static files"""
    states = storage.all('State').values()
    cities = storage.all('City').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', **locals())


@app.teardown_appcontext
def teardown(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')

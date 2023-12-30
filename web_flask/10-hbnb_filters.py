#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display a HTML page like 6-index.html with filters"""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()

    return render_template(
        '10-hbnb_filters.html',
        states=sorted(states, key=lambda x: x.name),
        cities=sorted(cities, key=lambda x: x.name),
        amenities=sorted(amenities, key=lambda x: x.name)
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


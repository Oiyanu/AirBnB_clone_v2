#!/usr/bin/python3
""" This script starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Returns message to be displayed """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Returns message to be displayed """
    return "HBNB"


@app.route("/c/<text>", strct_slashes=False)
def display_c(text):
    """ Returns message to be displayed """
    processed_text = text.replace("-", " ")
    return f"C {processed_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
